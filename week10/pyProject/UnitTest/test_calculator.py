"""
Unit tests for the calculator module.
"""

import unittest

import calculator


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """正常情况: Test that add returns the correct result."""
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_divide(self):
        """另一个正常情况: Test that divide returns the correct result."""
        result = calculator.divide(10, 2)
        self.assertEqual(result, 5) 
        # 我期望 result 等于 5

    def test_divide_by_zero(self):
        """异常测试:  Test that divide raises an exception when dividing by zero."""
        with self.assertRaises(ZeroDivisionError): 
            # 我期望这里产生 ZeroDivisionError.如果产生预期异常，pass 测试，否则 fail 测试 
            calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()