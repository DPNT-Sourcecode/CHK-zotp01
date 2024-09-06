from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    offers = {"A": [(5, 200), (3, 130)], "B": [(2, 45)]}
    extra_item_offers = {"E": [(2, "B")]}
    item_counts = defaultdict(int)

    for sku in skus:
        if sku not in prices:
            return -1
        item_counts[sku] += 1

    item_counts = _apply_extra_item_offers(item_counts, extra_item_offers)

    total = _calculate_total(item_counts, prices, offers)

    return total


def _apply_extra_item_offers(item_counts, extra_item_offers):
    """Apply extra item offers and return modified counts."""
    adjusted_counts = item_counts.copy()

    for item, count in item_counts.items():
        if item in extra_item_offers:
            for offer_count, offer_item in extra_item_offers[item]:
                if offer_item in adjusted_counts:
                    free_items = count // offer_count
                    adjusted_counts[offer_item] = max(adjusted_counts[offer_item] - free_items, 0)

    return adjusted_counts


def _calculate_total(item_counts, prices, offers):
    """Calculate the total price using item counts, applying applicable offers."""
    total = 0
    for item, count in item_counts.items():
        if item in offers:
            for offer_count, offer_price in offers[item]:
                num_offers = count // offer_count
                total += num_offers * offer_price
                count %= offer_count
        total += count * prices[item]
    return total


