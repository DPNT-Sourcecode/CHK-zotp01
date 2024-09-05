from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    offers = {"A": (3, 130), "B": (2, 45)}
    item_counts = {}

    for sku in skus:
        if sku not in prices:
            return -1

    total = 0

