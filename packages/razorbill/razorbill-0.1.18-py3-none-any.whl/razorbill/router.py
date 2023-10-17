from enum import Enum
from fastapi import APIRouter, Path, Depends, Query, FastAPI
from typing import Optional
from razorbill.crud import CRUD
from razorbill.deps import (
    build_exists_dependency,
    build_last_parent_dependency,
    build_pagination_dependency,
    build_path_elements,
    init_deps,
    build_parent_populate_dependency,
    build_sorting_dependency,
)
from razorbill.exceptions import NotFoundError
from typing import Callable, Type
from pydantic import BaseModel
from razorbill.utils import (
    get_slug_schema_name,
    schema_factory,
    validate_filters,
    parent_schema_factory,
    create_schema_from_model_with_overwrite
)


def empty_dependency():
    return None


class Router(APIRouter):
    def __init__(
            self,
            crud: CRUD,
            items_per_query: int = 10,
            item_name: str | None = None,
            parent_item_name: str | None = None,
            count_endpoint: bool | list[Callable] = True,
            get_all_endpoint: bool | list[Callable] = True,
            get_one_endpoint: bool | list[Callable] = True,
            create_one_endpoint: bool | list[Callable] = True,
            update_one_endpoint: bool | list[Callable] = True,
            delete_one_endpoint: bool | list[Callable] = True,
            parent_crud: CRUD | None = None,
            path_item_parameter: Type[Path] | None = None,
            prefix: str = '',
            tags: list[str | Enum] | None = None,
            dependencies: list[Depends] | None = None,
            schema_slug: str | None = None,
            filters: list[str] = None,
            schema: Type[BaseModel] | None = None,
            create_schema: Type[BaseModel] | None = None,
            update_schema: Type[BaseModel] | None = None,
            overwrite_schema: bool = False,
            overwrite_create_schema: bool = False,
            overwrite_update_schema: bool = False,
            exclude_from_create_schema: list[str] = [],
            exclude_from_update_schema: list[str] = [],
            **kwargs,
    ):
        self.parent_prefix = ''
        self.crud = crud
        self.parent_dependencies = dependencies
        self.pk = crud.connector.pk_name
        self.overwrite_schema = overwrite_schema
        self.overwrite_create_schema = overwrite_create_schema
        self.overwrite_update_schema = overwrite_update_schema
        self.Schema = schema if schema is not None else crud.connector.schema
        self.exclude_from_create_schema = exclude_from_create_schema
        self.exclude_from_update_schema = exclude_from_update_schema
        self.filters = validate_filters(self.Schema,
                                        filters) if filters is not None else None  # TODO нигде не используется
        if create_schema:
            self.create_schema = (
                create_schema
                if overwrite_create_schema
                else create_schema_from_model_with_overwrite(self.Schema, create_schema, pk_field_name=self.pk,
                                                             prefix="Create")
            )
        else:
            self.create_schema = schema_factory(self.Schema, self.exclude_from_create_schema + [self.pk])
        if update_schema:
            self.update_schema = (
                update_schema
                if overwrite_update_schema
                else create_schema_from_model_with_overwrite(self.Schema, update_schema, pk_field_name=self.pk,
                                                             prefix="")
            )
        else:
            self.update_schema = schema_factory(self.Schema, self.exclude_from_update_schema + [self.pk], prefix="Update")

        self.parent_item_name = parent_item_name
        self.CreateSchema = self.create_schema
        self.UpdateSchema = self.update_schema

        self._parent_id_dependency = Depends(empty_dependency)
        self._parent_populate_dependency = Depends(empty_dependency)

        if item_name is None:
            item_name = self.Schema.__name__

        if schema_slug is None:
            self._schema_slug = get_slug_schema_name(item_name)
        fields_to_exclude = ["id", "_id"]
        self._sort_field_dependency = build_sorting_dependency(self.Schema)
        if parent_crud is not None:
            if parent_item_name is None:
                self.parent_item_name = parent_crud.connector.schema.__name__
            parent_item_tag, _, parent_item_path = build_path_elements(self.parent_item_name)
            self.CreateSchema = schema_factory(self.create_schema, self.exclude_from_create_schema + [parent_item_tag])
            self.UpdateSchema = schema_factory(self.update_schema, self.exclude_from_update_schema + [parent_item_tag], prefix='Update')

            self.Schema = parent_schema_factory(self.Schema, self.parent_item_name)
            parent_exists_dependency = build_exists_dependency(parent_crud, parent_item_tag)
            self._parent_id_dependency = build_last_parent_dependency(parent_item_tag, crud.connector.type_pk)
            self._parent_populate_dependency = build_parent_populate_dependency()

            fields_to_exclude.append(parent_item_tag)
            if dependencies is not None:
                self.parent_dependencies.append(parent_exists_dependency)
            else:
                self.parent_dependencies = [parent_exists_dependency]

            if prefix is None:
                self.parent_prefix = parent_item_path
            else:
                self.parent_prefix += parent_item_path

        if tags is None:
            tags = [self._schema_slug]

        self.FilterSchema = schema_factory(self.CreateSchema, prefix='Filter', filters=filters)
        item_tag, path, item_path = build_path_elements(item_name)
        self._path = path
        #self._path_without_parent = path
        self._item_path = item_path
        self._path_field = Path(alias=item_tag) if path_item_parameter is None else path_item_parameter
        self._pagination_dependency = build_pagination_dependency(items_per_query)

        super().__init__(
            dependencies=dependencies,
            prefix=prefix,
            tags=tags,
            **kwargs
        )
        if count_endpoint:
            self._init_count_endpoint(self.parent_dependencies if self.parent_dependencies is not None else None)

        if get_all_endpoint:
            self._init_get_all_endpoint(self.parent_dependencies if self.parent_dependencies is not None else None)

        if get_one_endpoint:
            self._init_get_one_endpoint(get_one_endpoint)

        if create_one_endpoint:
            self._init_create_one_endpoint(self.parent_dependencies if self.parent_dependencies is not None else None)

        if update_one_endpoint:
            self._init_update_one_endpoint(update_one_endpoint)

        if delete_one_endpoint:
            self._init_delete_one_endpoint(delete_one_endpoint)

    def _init_count_endpoint(self, deps: list[Callable] | bool):
        @self.get(
            self.parent_prefix + self._path + "count", response_model=int, dependencies=init_deps(deps)
        )
        async def count(
                parent: dict[str, int] = self._parent_id_dependency,
                user_filter: self.FilterSchema = Depends(self.FilterSchema),
        ) -> int:
            payload = user_filter.dict(exclude_none=True)
            if parent is not None:
                payload |= parent
            return await self.crud.count(payload)

    def _init_get_all_endpoint(self, deps: list[Callable] | bool):

        @self.get(
            self.parent_prefix + self._path,
            response_model=list[self.Schema],
            dependencies=init_deps(deps),
            response_model_exclude_none=True,
            response_model_exclude_defaults=True,
            response_model_exclude_unset=True
        )
        async def get_many(
                pagination: tuple[str, int] = self._pagination_dependency,
                parent: dict[str, int] = self._parent_id_dependency,
                populate_parent: bool = self._parent_populate_dependency,
                user_filter: self.FilterSchema = Depends(self.FilterSchema),
                sorting: tuple[str, bool] = self._sort_field_dependency,
        ):
            payload = user_filter.dict(exclude_none=True)
            if parent is not None:
                payload |= parent
            skip, limit = pagination

            sort_field, sort_desc = sorting
            sorting = {sort_field: sort_desc} if sort_field else None
            items = await self.crud.get_many(skip, limit, filters=payload, populate=populate_parent, sorting=sorting)
            return items

    def _init_create_one_endpoint(self, deps: list[Callable] | bool):
        @self.post(

            self.parent_prefix + self._path,
            response_model=self.Schema,
            dependencies=init_deps(deps),
            response_model_exclude_none=True,
            response_model_exclude_defaults=True,
            response_model_exclude_unset=True
        )
        async def create_one(
                body: self.CreateSchema,
                parent: dict[str, int] = self._parent_id_dependency,
        ):
            payload = body.dict()
            if parent is not None:
                payload = body.dict() | parent
            item = await self.crud.create(payload)
            return item

    def _init_get_one_endpoint(self, deps: list[Callable] | bool):
        @self.get(
            self._item_path,
            response_model=self.Schema,
            dependencies=init_deps(deps),
            response_model_exclude_none=True,
            response_model_exclude_defaults=True,
            response_model_exclude_unset=True
        )
        async def get_one(
                item_id: int | str = self._path_field,
                #parent: dict[str, int] = self._parent_id_dependency,
                populate_parent: bool | str = self._parent_populate_dependency,
        ):
            #item = await self.crud.get_one(item_id, parent, populate=populate_parent)
            item = await self.crud.get_one(item_id, populate=populate_parent)
            if item:
                return item
            raise NotFoundError(self.Schema.__name__, self._path_field.alias, item_id)


    def _init_update_one_endpoint(self, deps: list[Callable] | bool):
        @self.put(
            self._item_path,
            response_model=self.Schema,
            dependencies=init_deps(deps),
            response_model_exclude_none=True,
            response_model_exclude_defaults=True,
            response_model_exclude_unset=True
        )
        async def update_one(
                *,
                #parent: dict[str, int] = self._parent_id_dependency,
                item_id: int | str = self._path_field,
                body: self.UpdateSchema,
        ):
            payload = body.dict(exclude_unset=True)
            # if parent is not None:
            #     payload = body.dict(exclude_unset=True) | parent

            item = await self.crud.update(item_id, payload)  # type: ignore
            if item:
                return item
            raise NotFoundError(self.Schema.__name__, self._path_field.alias, item_id)

    def _init_delete_one_endpoint(self, deps: list[Callable] | bool):
        @self.delete(self._item_path, dependencies=init_deps(deps))
        async def delete_one(
                #parent: dict[str, int] = self._parent_id_dependency,
                item_id: int | str = self._path_field,
        ):
            item = await self.crud.delete(item_id)
            print(item)
            if item:
                return item
            raise NotFoundError(self.Schema.__name__, self._path_field.alias, item_id)
