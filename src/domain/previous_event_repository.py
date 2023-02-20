import abc
from typing import List, Dict, Any

from src.domain.event import Event


class PreviousEventRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def insert_events(
        self,
        events_list: List[Event],
    ) -> None:
        raise NotImplementedError

    async def update_events(
        self,
        event_list: List[Event],
    ) -> List[Event]:
        raise NotImplementedError

    async def read_events(
        self,
    ) -> Dict[str, Any]:
        raise NotImplementedError
