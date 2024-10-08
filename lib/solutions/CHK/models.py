import msgspec


class Offer(msgspec.Struct):
    quantity: int
    price: int


class ExtraItemOffer(msgspec.Struct):
    quantity: int
    free_item: str


class GroupDiscount(msgspec.Struct):
    skus: set[str]
    quantity: int
    price: int


class Item(msgspec.Struct):
    price: int
    offers: list[Offer] = []
    extra_item_offers: list[ExtraItemOffer] = []
    in_group_discount: bool = False
