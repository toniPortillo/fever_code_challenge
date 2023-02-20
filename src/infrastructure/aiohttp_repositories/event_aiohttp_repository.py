from typing import Dict, Any, List, Callable

from aiohttp import ClientSession

from src.domain.event import Event
from src.domain.event_factory_method import (
    EventFactoryMethod,
)
from src.domain.event_repository import (
    EventRepository,
)
from src.shared.application.application_exception import (
    ApplicationException,
)
from src.shared.config.provider_configuration_constants import PROVIDER_SERVICE_URL
from src.shared.domain.domain_exceptions import DomainException


class EventAiohttpRepository(EventRepository):
    def __init__(
        self,
        http_session: ClientSession,
        xml_to_dict_parser: Callable[[Any], Any],
    ) -> None:
        self.__http_session = http_session
        self.__xml_to_dict_parser = xml_to_dict_parser

    async def get_events_from_provider(
        self,
    ) -> List[Event]:
        try:
            async with self.__http_session.get(
                PROVIDER_SERVICE_URL,
            ) as response:
                if response.status != 200:
                    raise Exception
                event_list_xml: bytes = await response.read()
                event_list_orderdict: Dict[str, Any] = dict(
                    self.__xml_to_dict_parser(event_list_xml)
                )
                event_list: List[Event] = []

                for element in event_list_orderdict["eventList"]["output"][
                    "base_event"
                ]:
                    if element["@sell_mode"] == "online":
                        event_dict: Dict[str, Any] = {}
                        event_dict["id"] = element["@base_event_id"]
                        event_dict["title"] = element["@title"]
                        event_star_date: List[str] = element["event"][
                            "@event_start_date"
                        ].split("T")
                        event_dict["start_date"] = event_star_date[0]
                        event_dict["start_time"] = event_star_date[1]
                        event_end_date: List[str] = element["event"][
                            "@event_end_date"
                        ].split("T")
                        event_dict["end_date"] = event_end_date[0]
                        event_dict["end_time"] = event_end_date[1]
                        prices: List[float] = []
                        for zone in element["event"]["zone"]:
                            price: float
                            if zone == "@price":
                                price = float(element["event"]["zone"]["@price"])
                            if type(zone) == dict:
                                price = float(zone["@price"])
                            prices.append(price)
                            event_dict["min_price"] = min(prices)
                            event_dict["max_price"] = max(prices)
                        event: Event = await EventFactoryMethod.build_event(
                            event_dict["id"],
                            event_dict["title"],
                            event_dict["start_date"],
                            event_dict["start_time"],
                            event_dict["end_date"],
                            event_dict["end_time"],
                            event_dict["min_price"],
                            event_dict["max_price"],
                        )
                        event_list.append(event)

            return event_list
        except DomainException as domain_exception:
            raise ApplicationException(
                domain_exception.standard_exception,
                domain_exception.exception_message,
            )
        except Exception:
            return []
