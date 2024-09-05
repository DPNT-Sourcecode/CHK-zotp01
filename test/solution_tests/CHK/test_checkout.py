from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        # # test case with an invald SKU
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
        # test case with extra item offers
        assert checkout_solution.checkout("EEB") == 80
        # test case with extra item offers and financial offers
        # should get one B free after the 2 for 45 B offer
        assert checkout_solution.checkout("EEBB") == 95
