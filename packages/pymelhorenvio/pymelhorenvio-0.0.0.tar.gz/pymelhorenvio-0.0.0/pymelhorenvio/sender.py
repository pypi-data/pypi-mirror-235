from dataclasses import dataclass
from typing import Optional

from pymelhorenvio.address import Address


@dataclass
class Sender:
    name: str
    phone: str
    email: str
    document: str

    def __post_init__(self) -> None:
        self.__address: Optional[Address] = None

    def add_company_document(self, document: str, state_register: str) -> None:
        ...

    def set_address(self, address: Address) -> None:
        self.__address = address

    def get_address(self) -> Optional[Address]:
        return self.__address

    def asdict(self):
        asdict = dict(**vars(self), note="")
        del asdict[f"_{self.__class__.__name__}__address"]
        self.__address and asdict.update(self.__address.asdict())
        return asdict
