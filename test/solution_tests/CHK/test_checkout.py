from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        # test case with an invald SKU
        assert checkout_solution.checkout("aabzc") == -1
        # test case with no items
        assert checkout_solution.checkout("") == 0
        # test case per sku with no offers
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("E") == 40
        # test case with no special offers
        assert checkout_solution.checkout("ABCD") == 115
        # test case with special offers
        assert checkout_solution.checkout("AAABBBC") == 225
        # test case with lower case SKUs
        assert checkout_solution.checkout("aaa") == -1
        # test case with none alpha characters
        assert checkout_solution.checkout("AAABBBC123@") == -1
        # test case with extra item offers
        assert checkout_solution.checkout("EEB") == 80
        # test case with extra item offers and financial offers
        # should get one B free after the 2 for 45 B offer
        assert checkout_solution.checkout("EEBB") == 110
        assert checkout_solution.checkout("EEEEBB") == 160
        assert checkout_solution.checkout("BBEEEE") == 160
        # test case with multiple financial offers for one sku
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        # test case with mixed SKUs and offers
        assert checkout_solution.checkout("AABBCCDDEE") == 280
        assert checkout_solution.checkout("ABCDEABCDE") == 280
        assert checkout_solution.checkout("CCADDEEBBA") == 280
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455
        assert checkout_solution.checkout("ABCDECBAABCABBAAAEEAA") == 665

    def test_extra_item_offers(self):
        # test adding extra item offers with the free item in the basket
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFFF") == 40
        # test adding extra item offers without the free item in the basket
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("FFA") == 70
        # test adding extra item offers with one complete and a partial set of items in the basket
        assert checkout_solution.checkout("FFFFF") == 40


