from solutions.CHK import checkout_solution

class TestCheckout():
    def test_invalid_baskets(self):
        # test case with an invald SKU
        assert checkout_solution.checkout("aabzc") == -1
        # test case with lower case SKUs
        assert checkout_solution.checkout("aaa") == -1
        # test case with none alpha characters
        assert checkout_solution.checkout("AAABBBC123@") == -1

    def test_empty_basket(self):
        assert checkout_solution.checkout("") == 0

    def test_valid_skus(self):
        # test case per sku with no offers
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("G") == 20
        assert checkout_solution.checkout("H") == 10
        assert checkout_solution.checkout("I") == 35
        assert checkout_solution.checkout("J") == 60
        assert checkout_solution.checkout("K") == 70
        assert checkout_solution.checkout("L") == 90
        assert checkout_solution.checkout("M") == 15
        assert checkout_solution.checkout("N") == 40
        assert checkout_solution.checkout("O") == 10
        assert checkout_solution.checkout("P") == 50
        assert checkout_solution.checkout("Q") == 30
        assert checkout_solution.checkout("R") == 50
        assert checkout_solution.checkout("S") == 20
        assert checkout_solution.checkout("T") == 20
        assert checkout_solution.checkout("U") == 40
        assert checkout_solution.checkout("V") == 50
        assert checkout_solution.checkout("W") == 20
        assert checkout_solution.checkout("X") == 17
        assert checkout_solution.checkout("Y") == 20
        assert checkout_solution.checkout("Z") == 21

    def test_mixed_basket_with_no_special_offers(self):
        assert checkout_solution.checkout("ABCD") == 115
        assert checkout_solution.checkout("VWXY") == 107

    def test_with_standard_discount_offers(self):
        # test case with special offers
        assert checkout_solution.checkout("AAABBBC") == 225
        # test case with multiple financial offers for one sku
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    def test_extra_item_offers_with_different_qualifying_and_free_items(self):
        # test case with extra item offers
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EE") == 80
        # test case with extra item offers and financial offers
        # should get one B free after the 2 for 45 B offer
        assert checkout_solution.checkout("EEBB") == 110
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("BBEEEE") == 160

    def test_extra_item_offers_with_identical_qualifying_and_free_items(self):
        # test adding extra item offers with the free item in the basket
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFFF") == 40
        # test adding extra item offers without the free item in the basket
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFA") == 70
        # test adding extra item offers with one complete and a partial set of items in the basket
        assert checkout_solution.checkout("FFFFF") == 40

    def test_mixed_extra_item_offers(self):
        assert checkout_solution.checkout("FFFEEB") == 100

    def test_group_discounts(self):
        assert checkout_solution.checkout("ZZZ") == 45
        assert checkout_solution.checkout("STX") == 45
        assert checkout_solution.checkout("STXYZS") == 90
        # as the policy should always favour the customer, we should use the most expensive items available in the group
        # discount
        assert checkout_solution.checkout("ZZZS") == 65
        assert checkout_solution.checkout("XZYT") == 62
        assert checkout_solution.checkout("XTYSZ") == 82

    def test_combined_basket(self):
        # test case with mixed SKUs and offers
        assert checkout_solution.checkout("AABBCCDDEE") == 280
        assert checkout_solution.checkout("ABCDEABCDE") == 280
        assert checkout_solution.checkout("CCADDEEBBA") == 280
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665
        assert checkout_solution.checkout("ZZZA") == 95
        assert checkout_solution.checkout("ZZZAAA") == 175
        assert checkout_solution.checkout("ZZZAAAFFF") == 195
        assert checkout_solution.checkout("XTYSZZZZAAA") == 257
