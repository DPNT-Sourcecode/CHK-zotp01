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

    free_items = defaultdict(int)
    for item, count in item_counts.items():
        item_extra_item_offers = extra_item_offers.get(item)
        if item_extra_item_offers:
            sorted_special_offers = sorted(item_extra_item_offers, key=lambda x: -x[0])
            for offer_count, offer_item in sorted_special_offers:
                free_count = count // offer_count
                free_items[offer_item] += free_count
                count %= offer_count

    adjusted_counts = item_counts.copy()
    for free_item, free_count in free_items.items():
        # discount up to the amount ordered
        adjusted_counts[free_item] = max(0, item_counts[free_item] - free_count)

    total = 0
    for item, count in adjusted_counts.items():
        item_offers = offers.get(item)
        if item_offers:
            sorted_offers = sorted(item_offers, key=lambda x: -x[0])
            for offer_count, offer_price in sorted_offers:
                total += (count // offer_count) * offer_price
                count %= offer_count
        total += count * prices[item]

    return total

    # for item, count in item_counts.items():
    #     item_extra_item_offers = extra_item_offers.get(item)
    #     item_offers = offers.get(item)
    #
    #     # calculate the free items to be removed from the total after the financial offers
    #     if item_extra_item_offers:
    #         temp_count = count
    #         # apply the best offer first and then work down
    #         sorted_special_offers = sorted(item_extra_item_offers, key=lambda x: -x[0])
    #         for offer_count, offer_item in sorted_special_offers:
    #             free_item_count = temp_count // offer_count
    #             free_items[offer_item] += free_item_count
    #             temp_count %= offer_count
    #
    #     if item_offers:
    #         # apply the best offer first and then work down
    #         sorted_offers = sorted(item_offers, key=lambda x: -x[0])
    #         for offer_count, offer_price in sorted_offers:
    #             total += (count // offer_count) * offer_price
    #             count %= offer_count
    #     total += count * prices[item]
    #
    # # remove the free items from the total
    # for free_item, free_item_count in free_items.items():
    #     number_of_item_type_ordered = item_counts[free_item]
    #     number_of_item_type_to_discount = min(free_item_count, number_of_item_type_ordered)
    #     total -= prices[free_item] * number_of_item_type_to_discount
    #
    # return total




