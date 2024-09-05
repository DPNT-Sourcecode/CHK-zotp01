from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        # test case with an invald SKU
        assert checkout_solution.checkout("aabzc") == -1
        # test case with no items
        assert checkout_solution.checkout() == 0
        # test case with no special offers
        assert checkout_solution.checkout("ABCD") == 115