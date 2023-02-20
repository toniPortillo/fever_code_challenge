import abc
from typing import List

from src.domain.event import Event


class EventRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def get_events_from_provider(self) -> List[Event]:
        raise NotImplementedError
