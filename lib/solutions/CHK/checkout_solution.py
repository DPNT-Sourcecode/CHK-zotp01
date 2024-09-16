from collections import defaultdict
from solutions.CHK.models import ExtraItemOffer, Offer


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    offers = {
        "A": [Offer(quantity=5, price=200), Offer(quantity=3, price=130)],
        "B": [Offer(quantity=2, price=45)]
    }
    extra_item_offers = {
        "E": [ExtraItemOffer(quantity=2, free_item="B")],
        "F": [ExtraItemOffer(quantity=2, free_item="F")]
    }
    item_counts = defaultdict(int)

    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] += 1

    item_counts = _apply_extra_item_offers(item_counts, extra_item_offers)

    return _calculate_total(item_counts, prices, offers)


def _apply_extra_item_offers(
    item_counts: dict[str, int], extra_item_offers: dict[str, list[ExtraItemOffer]]
) -> dict[str, int]:
    """Apply extra item offers and return modified counts."""
    for item, count in item_counts.items():
        if item in extra_item_offers:
            for offer in extra_item_offers[item]:
                if offer.free_item in item_counts:
                    free_items = count // offer.quantity
                    # check if the qualifying item and free item are the same
                    if item == offer.free_item:
                        # ensure that we have at least the sum of the items needed for the offer and the free items
                        applicable_free_items = count // (offer.quantity + 1)
                        item_counts[item] -= applicable_free_items
                    else:
                        # standard case where qualifying and free items are different
                        item_counts[offer.free_item] = max(item_counts[offer.free_item] - free_items, 0)

    return item_counts


def _calculate_total(
    item_counts: dict[str, int], prices: dict[str, int], offers: dict[str, list[Offer]]
) -> int:
    """Calculate the total price using item counts and applying applicable offers."""
    total = 0
    for item, count in item_counts.items():
        if item in offers:
            for offer in offers[item]:
                num_offers = count // offer.quantity
                total += num_offers * offer.price
                count %= offer.quantity
        total += count * prices[item]
    return total
