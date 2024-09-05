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
        offer = offers.get(item)
        special_offer = special_offers.get(item)
        if offer:

            offer_count, offer_price = offer
            total += (counts // offer_count) * offer_price
            counts %= offer_count
        if special_offers:
            for i in range(len(special_offers), 0, -1):

            special_offer_count, special_offer_item = special_offer
            total += counts * prices[special_offer_item]
            counts %= special_offer_count
        total += counts * prices[item]

    return total
