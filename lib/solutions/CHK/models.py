import msgspec


class Offer(msgspec.Struct):
    quantity: int
    price: int


class ExtraItemOffer(msgspec.Struct):
    quantity: int
    free_item: str
