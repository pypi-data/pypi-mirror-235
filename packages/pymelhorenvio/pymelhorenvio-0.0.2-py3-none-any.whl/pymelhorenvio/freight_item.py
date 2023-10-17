from dataclasses import dataclass
from typing import Optional

from pymelhorenvio.freight_service import ShippingService


@dataclass(unsafe_hash=True)
class FreightItem:
    height: int
    width: int
    length: int
    weight: float
    service: Optional[ShippingService] = None
    insurance_value: float = 0
