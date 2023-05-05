import dataclasses

@dataclasses.dataclass
class Card:
    title: str
    photo: str
    link: str



@dataclasses.dataclass
class SectionCard(Card):
    description: str
    worked_time: str


@dataclasses.dataclass
class ServiceCard(Card):
    description: str
    price: str
    order_command: str


@dataclasses.dataclass
class Page:
    title: str
    description: str
    photo: str
