"""base list model
"""

from __future__ import annotations
from typing import Generic, TypeVar, Iterable, Callable
from pydantic.generics import GenericModel

T = TypeVar("T")
U = TypeVar("U")


class BaseListModel(GenericModel, Generic[T]):
    __root__: list[T]

    def __bool__(self) -> bool:
        return bool(self.__root__)

    def __len__(self) -> int:
        return len(self.__root__)

    def __iter__(self) -> Iterable[T]:
        return iter(self.__root__)

    def map(self, f: Callable[[T], U]) -> BaseListModel[U]:
        return BaseListModel[U](__root__=[f(it) for it in self])
