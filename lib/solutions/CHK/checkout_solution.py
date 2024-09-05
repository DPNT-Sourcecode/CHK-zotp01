from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    offers = {"A": [(3, 130), (5, 200)], "B": [(2, 45)]}
    extra_item_offers = {"E": [(2, "B")]}
    item_counts = defaultdict(int)

    for sku in skus:
        if sku not in prices:
            return -1
        else:
            item_counts[sku] += 1

    total = 0

    for item, counts in item_counts.items():
        item_extra_item_offers = extra_item_offers.get(item)
        if item_extra_item_offers:
            # apply the best offer first and then work down
            sorted_special_offers = sorted(item_extra_item_offers, key=lambda x: -x[0])
            for offer_count, offer_item in sorted_special_offers:
                free_items = counts // offer_count
                updated_item_count = item_counts[offer_item] - free_items
                item_counts[offer_item] = updated_item_count if updated_item_count > 0 else 0
                counts %= offer_count

    for item, counts in item_counts.items():
        item_offers = offers.get(item)
        if item_offers:
            # apply the best offer first and then work down
            sorted_offers = sorted(item_offers, key=lambda x: -x[0])
            for offer_count, offer_price in sorted_offers:
                total += (counts // offer_count) * offer_price
                counts %= offer_count
        total += counts * prices[item]

    return total



