from typing import Any, Dict, List, Union
from uuid import UUID

from pymelhorenvio.config import Config
from pymelhorenvio.freight_item import FreightItem
from pymelhorenvio.freight_service import ShippingCompany, ShippingService
from pymelhorenvio.package import Package

try:
    from typing import Literal  # type: ignore
except ImportError:
    from typing_extensions import Literal  # type: ignore


class Shipment:
    def __init__(self, http_client, config: Config) -> None:
        self.__http_client = http_client
        self.__config = config

    def tracking(
        self, orders_id: List[Union[str, UUID]]
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/tracking"
        payload = {"orders": [*orders_id]}
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        return response.json()

    def cancel(
        self, order_id: Union[str, UUID], description: str
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/cancel"
        payload = {
            "order": {
                "reason_id": "2",
                "id": f"{order_id}",
                "description": f"{description}",
            }
        }
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        return response.json()

    def generate_tag(
        self, orders_id: List[Union[str, UUID]]
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/generate"
        payload = {"orders": [*orders_id]}
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        return response.json()

    def print_tag(
        self,
        orders_id: List[Union[str, UUID]],
        mode: Literal["private", "public", ""] = "",
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/generate"
        payload: Dict[str, Any] = {"orders": [*orders_id]}
        default_modes = mode and self.print_tag.__defaults__
        if default_modes and mode in default_modes:
            payload["mode"] = mode
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        return response.json()

    def preview_tag(
        self,
        orders_id: List[Union[str, UUID]],
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/preview"
        payload: Dict[str, Any] = {"orders": [*orders_id]}
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        return response.json()

    def checkout(
        self, orders_id: List[Union[str, UUID]]
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/checkout"
        payload = {"orders": [*orders_id]}
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        return response.json()

    def is_callable(
        self, orders_id: List[Union[str, UUID]]
    ) -> Dict[str, Union[bool, int, float, str]]:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/cancellable"
        payload = {"orders": [*orders_id]}
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        return response.json()

    def simulate_freight(
        self, cep_origin: str, cep_destin: str, *freight_items: FreightItem
    ) -> Any:
        url = f"{self.__config.get_base_url()}/api/v2/me/shipment/calculate"
        package = Package()
        package.bulk_add_items(freight_items)
        payload: Dict[str, Any] = {
            "from": {"postal_code": cep_origin},
            "to": {"postal_code": cep_destin},
            **package.asdict(),
        }
        response = self.__http_client.post(
            url,
            headers=self.__config.get_headers(),
            json=payload,
        )
        items = response.json()
        return self.__create_freight_items(items)

    def __create_freight_items(self, items) -> List[FreightItem]:
        freight_items = []
        for item in items:
            if "error" in item:
                continue
            freight_items += self.__create_freight_item(item)
        return freight_items

    def __create_freight_item(self, item) -> List[FreightItem]:
        items: List[FreightItem] = []
        service = self.__create_shipping_service(item)
        for pkg in item.get("packages"):
            freight_item = FreightItem(
                pkg.get("dimensions", {}).get("height"),
                pkg.get("dimensions", {}).get("width"),
                pkg.get("dimensions", {}).get("length"),
                float(pkg.get("weight")),
                service=service,
            )
            freight_item.set_delivery_days(
                item.get("delivery_range", {}).get("min", -1),
                item.get("delivery_range", {}).get("max", -1),
            )
            items.append(freight_item)
        return items

    def __create_shipping_service(self, item) -> ShippingService:
        return ShippingService(
            name=item.get("name"),
            price=float(item.get("price")),
            id=item.get("id"),
            company=self.__create_shipping_company(item),
        )

    def __create_shipping_company(self, item) -> ShippingCompany:
        id, company_name, image = item.get("company").values()
        return ShippingCompany(name=company_name, image=image, id=id)
