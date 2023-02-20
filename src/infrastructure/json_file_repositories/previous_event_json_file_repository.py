import copy
from typing import List, Dict, Any

from src.domain.event import (
    Event,
)
from src.domain.event_factory_method import (
    EventFactoryMethod,
)
from src.domain.previous_event_repository import (
    PreviousEventRepository,
)
from src.shared.application.application_exception import (
    ApplicationException,
)
from src.shared.domain.domain_exceptions import (
    DomainException,
)
from src.shared.config.provider_configuration_constants import (
    PREVIOUS_EVENTS_JSON_FILE,
)
from src.shared.domain.exceptions import (
    DEPENDENCY_PROBLEM,
)


class PreviousEventJsonFileRepository(PreviousEventRepository):
    def __init__(
        self,
        json_dump: Any,
        json_load: Any,
    ) -> None:
        self.__json_dump = json_dump
        self.__json_load = json_load

    async def insert_events(
        self,
        events_list: List[Event],
    ) -> None:
        try:
            event_dict_list: Dict[str, Any] = {}
            event_dict_list["events"] = []
            with open(PREVIOUS_EVENTS_JSON_FILE, "w") as fp:
                for event in events_list:
                    data: Dict[str, Any] = {
                        "id": event.event_id,
                        "title": event.title,
                        "start_date": event.start_date,
                        "start_time": event.start_time,
                        "end_date": event.end_date,
                        "end_time": event.end_time,
                        "min_price": event.min_price,
                        "max_price": event.max_price,
                    }
                    event_dict_list["events"].append(data)
                self.__json_dump(event_dict_list, fp, indent=4)

        except Exception:
            raise ApplicationException(
                DEPENDENCY_PROBLEM,
                "A problem occurred inserting event in the json file",
            )

    async def update_events(
        self,
        event_list: List[Event],
    ) -> List[Event]:
        try:
            event_dict: Dict[str, Any] = await self.read_events()
            if "events" not in event_dict.keys():
                event_dict = {"events": []}
            updated_event_dict: Dict[str, Any] = copy.deepcopy(event_dict)
            element_exist: bool = False
            for event in event_list:
                for element in event_dict["events"]:
                    if (
                        element["id"] == event.event_id
                        and element["start_date"] == event.start_date
                        and element["end_date"] == event.end_date
                    ):
                        element_exist = True
                if not element_exist:
                    updated_event_dict["events"].append(
                        {
                            "id": event.event_id,
                            "title": event.title,
                            "start_date": event.start_date,
                            "start_time": event.start_time,
                            "end_date": event.end_date,
                            "end_time": event.end_time,
                            "min_price": event.min_price,
                            "max_price": event.max_price,
                        }
                    )
                element_exist = False

            with open(PREVIOUS_EVENTS_JSON_FILE, "w") as fp:
                self.__json_dump(updated_event_dict, fp, indent=4)

            updated_events: List[Event] = [
                await EventFactoryMethod.build_event(
                    event_element["id"],
                    event_element["title"],
                    event_element["start_date"],
                    event_element["start_time"],
                    event_element["end_date"],
                    event_element["end_time"],
                    int(event_element["min_price"]),
                    int(event_element["max_price"]),
                )
                for event_element in updated_event_dict["events"]
            ]

            return updated_events
        except DomainException as domain_exception:
            raise ApplicationException(
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
        except Exception:
            raise ApplicationException(
                DEPENDENCY_PROBLEM,
                "A problem occurred updating the json file",
            )

    async def read_events(
        self,
    ) -> Dict[str, Any]:
        try:
            event_dict: Dict[str, Any]
            with open(PREVIOUS_EVENTS_JSON_FILE, "r") as fp:
                event_dict = self.__json_load(fp)

            return event_dict
        except Exception:
            event_dict_list: Dict[str, Any] = {}
            event_dict_list["events"] = []
            with open(PREVIOUS_EVENTS_JSON_FILE, "w") as fp:
                self.__json_dump(event_dict_list, fp, indent=4)

            return event_dict_list
