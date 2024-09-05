from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        # test case with an invald SKU
        # assert checkout_solution.checkout("aabzc") == -1
        # # test case with no items
        # assert checkout_solution.checkout("") == 0
        # # test case with no special offers
        # assert checkout_solution.checkout("ABCD") == 115
        # # test case with special offers
        # assert checkout_solution.checkout("AAABBBC") == 225
        # # test case with lower case SKUs
        # assert checkout_solution.checkout("aaa") == -1
        # # test case with none alpha characters
        # assert checkout_solution.checkout("AAABBBC123@") == -1
        # # test case with extra item offers
        # assert checkout_solution.checkout("EEB") == 80
        # # test case with extra item offers and financial offers
        # # should get one B free after the 2 for 45 B offer
        # assert checkout_solution.checkout("EEBB") == 95
        # assert checkout_solution.checkout("EEEEBB") == 160
        # # test case with multiple financial offers for one sku
        # assert checkout_solution.checkout("AAAAAA") == 250
        # assert checkout_solution.checkout("AAAAAAAA") == 330
        # assert checkout_solution.checkout("AAAAAAAAA") == 380
        # test case with mixed SKUs and offers
        assert checkout_solution.checkout("AABBCCDDEE") == 280
        # 2 * a = 100
        # 2 * b = 30 (1 free from the 2Es offer)
        # 2 * B = 45
        # 2 * c = 40
        # 2 * d = 30
        # 2 * e = 80