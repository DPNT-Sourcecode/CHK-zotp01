from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
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


    free_items = []
    for item, counts in item_counts.items():
        item_extra_item_offers = extra_item_offers.get(item)
        item_offers = offers.get(item)

        # calculate the free items to be removed from the total after the financial offers
        if item_extra_item_offers:
            # apply the best offer first and then work down
            sorted_special_offers = sorted(item_extra_item_offers, key=lambda x: -x[0])
            for offer_count, offer_item in sorted_special_offers:
                free_item_count = counts // offer_count
                for i in range(free_item_count):
                    free_items.append(item)
                counts %= offer_count

        if item_offers:
            # apply the best offer first and then work down
            sorted_offers = sorted(item_offers, key=lambda x: -x[0])
            for offer_count, offer_price in sorted_offers:
                total += (counts // offer_count) * offer_price
                counts %= offer_count
        total += counts * prices[item]

    return total




