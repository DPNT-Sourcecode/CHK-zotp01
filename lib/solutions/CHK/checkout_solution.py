from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    offers = {"A": [(3, 130), (5, 200)], "B": [(2, 45)]}
    special_offers = {"E": [(2, "B")]}
    item_counts = defaultdict(int)

    for sku in skus:
        if sku not in prices:
            return -1
        else:
            item_counts[sku] += 1

    total = 0

    for item, counts in item_counts.items():
        item_special_offers = special_offers.get(item)
        temp_count = counts
        if item_special_offers:
            # apply the best offer first and then work down
            sorted_special_offers = sorted(item_special_offers, key=lambda x: -x[0])
            for offer_count, offer_item in sorted_special_offers:
                if temp_count >= offer_count:
                    item_counts[offer_item] += counts // offer_count
                    counts %= temp_count

    for item, counts in item_counts.items():
        item_offers = offers.get(item)
        item_special_offers = special_offers.get(item)
        if item_offers:
            sorted_offers = sorted(item_offers, key=lambda x: -x[0])
            for offer_count, offer_price in sorted_offers:
                total += (counts // offer_count) * offer_price
                counts %= offer_count
        total += counts * prices[item]

    return total


