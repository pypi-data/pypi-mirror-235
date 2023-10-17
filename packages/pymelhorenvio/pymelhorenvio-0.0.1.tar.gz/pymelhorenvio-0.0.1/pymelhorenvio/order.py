from typing import Dict, Literal, Union
from uuid import UUID

from pymelhorenvio.config import Config

ALLOWED_STATUS = Literal[
    "Pending",
    "Released",
    "Posted",
    "Delivered",
    "Cancelled",
    "Not Delivered",
    "",
    "pending",
    "released",
    "posted",
    "delivered",
    "cancelled",
    "not delivered",
]


class Order:
    def __init__(self, http_client, config: Config) -> None:
        self.__http_client = http_client
        self.__config = config

    def search(
        self, q: Union[str, UUID], status: ALLOWED_STATUS = ""
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/orders/search?q={q}"
        if status:
            url = f"{url}&status={status}"
        response = self.__http_client.get(
            url,
            headers=self.__config.get_headers(),
        )
        return response.json()

    def list(
        self, status: ALLOWED_STATUS = ""
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/orders?status={status}"
        response = self.__http_client.get(
            url,
            headers=self.__config.get_headers(),
        )
        return response.json()

    def detail(
        self, order_id: Union[str, UUID]
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/orders/{order_id}"
        response = self.__http_client.get(
            url,
            headers=self.__config.get_headers(),
        )
        return response.json()
