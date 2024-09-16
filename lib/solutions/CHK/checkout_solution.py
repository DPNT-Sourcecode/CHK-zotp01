from collections import defaultdict
from solutions.CHK.models import ExtraItemOffer, GroupDiscount, Item, Offer


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    items = {
        "A": Item(price=50, offers=[Offer(quantity=5, price=200), Offer(quantity=3, price=130)]),
        "B": Item(price=30, offers=[Offer(quantity=2, price=45)]),
        "C": Item(price=20),
        "D": Item(price=15),
        "E": Item(price=40, extra_item_offers=[ExtraItemOffer(quantity=2, free_item="B")]),
        "F": Item(price=10, extra_item_offers=[ExtraItemOffer(quantity=2, free_item="F")]),
        "G": Item(price=20),
        "H": Item(price=10, offers=[Offer(quantity=10, price=80), Offer(quantity=5, price=45)]),
        "I": Item(price=35),
        "J": Item(price=60),
        "K": Item(price=70, offers=[Offer(quantity=2, price=120)]),
        "L": Item(price=90),
        "M": Item(price=15),
        "N": Item(price=40, extra_item_offers=[ExtraItemOffer(quantity=3, free_item="M")]),
        "O": Item(price=10),
        "P": Item(price=50, offers=[Offer(quantity=5, price=200)]),
        "Q": Item(price=30, offers=[Offer(quantity=3, price=80)]),
        "R": Item(price=50, extra_item_offers=[ExtraItemOffer(quantity=3, free_item="Q")]),
        "S": Item(price=20, in_group_discount=True),
        "T": Item(price=20, in_group_discount=True),
        "U": Item(price=40, extra_item_offers=[ExtraItemOffer(quantity=3, free_item="U")]),
        "V": Item(price=50, offers=[Offer(quantity=3, price=130), Offer(quantity=2, price=90)]),
        "W": Item(price=20),
        "X": Item(price=17, in_group_discount=True),
        "Y": Item(price=20, in_group_discount=True),
        "Z": Item(price=21, in_group_discount=True)
    }

    group_discounts = [
        GroupDiscount(skus={"S", "T", "X", "Y", "Z"}, quantity=3, price=45),
    ]

    item_counts = defaultdict(int)

    for sku in skus:
        if sku not in items:
            return -1
        item_counts[sku] += 1

    item_counts = _apply_extra_item_offers(item_counts, items)

    return _calculate_total(item_counts, items, group_discounts)


def _apply_extra_item_offers(
    item_counts: dict[str, int], items: dict[str, Item]
) -> dict[str, int]:
    """Apply extra item offers and return modified counts."""
    for item, count in item_counts.items():
        if items[item].extra_item_offers:
            for offer in items[item].extra_item_offers:
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

def _total_for_group_discount_items(
    item_counts: dict[str, int], items: dict[str, Item], group_discounts: list[GroupDiscount]
) -> int:
    """Apply group discounts and return the total price for all group discount items."""
    total = 0
    for discount in group_discounts:
        # basket items that ae in the group discount
        group_items = [(sku, items[sku].price) for sku in discount.skus if sku in item_counts]
        # sort the items in descending price order so the most expensive are included in the group offer
        group_items.sort(key=lambda x: x[1], reverse=True)

        total_applicable_items = sum(item_counts[sku] for sku, _ in group_items)

        # apply the group discount as many times as possible
        while total_applicable_items >= discount.quantity:
            total += discount.price
            total_applicable_items -= discount.quantity

            # discount items from highest priced to lowest to maximise savings
            for sku, _ in group_items:
                if item_counts[sku] > 0 and total_applicable_items < discount.quantity:
                    deduction = min(item_counts[sku], discount.quantity - total_applicable_items)
                    item_counts[sku] -= deduction
                    total_applicable_items -= deduction
                    if total_applicable_items == 0:
                        break

        # add the remaining items that did not fit into a group discount
        for sku, price in group_items:
            total += item_counts[sku] * price
            item_counts[sku] = 0

    return total


def _calculate_total(
    item_counts: dict[str, int], items: dict[str, Item], group_discounts: list[GroupDiscount]
) -> int:
    """Calculate the total price using item counts and applying applicable offers."""
    total = _total_for_group_discount_items(item_counts=item_counts, items=items, group_discounts=group_discounts)
    for item, count in item_counts.items():
        if items[item].in_group_discount:
            continue
        if items[item].offers:
            for offer in items[item].offers:
                num_offers = count // offer.quantity
                total += num_offers * offer.price
                count %= offer.quantity
        total += count * items[item].price
    return total



