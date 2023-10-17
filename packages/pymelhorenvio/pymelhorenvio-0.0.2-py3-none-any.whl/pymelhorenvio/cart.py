from typing import Any, Optional
from uuid import UUID

from pymelhorenvio.config import Config
from pymelhorenvio.freight_item import FreightItem
from pymelhorenvio.receiver import Receiver
from pymelhorenvio.sender import Sender


class Cart:
    def __init__(self, http_client, config: Config) -> None:
        self.__http_client = http_client
        self.__config = config

    def add_item(
        self, item: FreightItem, sender: Sender, receiver: Receiver
    ) -> Optional[UUID]:
        url = f"{self.__config.get_base_url()}/api/v2/me/cart"
        payload = {
            "from": sender.asdict(),
            "to": receiver.asdict(),
            "service": item.service and item.service.id or None,
            "volumes": [
                {
                    "height": item.height,
                    "width": item.width,
                    "length": item.length,
                    "weight": item.weight,
                }
            ],
            "options": {
                "receipt": True,
                "own_hand": True,
                "reverse": True,
                "non_commercial": True,
            },
        }
        response = self.__http_client.post(
            url, headers=self.__config.get_headers(), json=payload
        )
        items = response.json()
        return UUID(items.get("id"))

    def list_items(self) -> Any:
        url = f"{self.__config.get_base_url()}/api/v2/me/cart"
        response = self.__http_client.get(url, headers=self.__config.get_headers())
        items = response.json()
        print(items)

    def detail_item(self, order_id: str) -> Any:
        url = f"{self.__config.get_base_url()}/api/v2/me/cart/{order_id}"
        response = self.__http_client.get(url, headers=self.__config.get_headers())
        items = response.json()
        print(items)

    def remove_item(self, order_id: str) -> Any:
        url = f"{self.__config.get_base_url()}/api/v2/me/cart/{order_id}"
        response = self.__http_client.delete(url, headers=self.__config.get_headers())
        items = response.json()
        print(items)
