def addStringsHelper(num1: str, num2: str, res: str):
    # base case, both are 0 or empty strings
    sum_is_zero = len(num1) <= 1 and num1 == num2 and num1 == "0"

    if sum_is_zero:
        return "0"

    # recursive case
    else:
        larger = num1
        smaller = num2

        if len(num2) > len(num1):
            larger = num2
            smaller = num1

        carry_digit = 0

        buffer = len(larger) - len(smaller)
        for i in range(len(smaller) - 1, 0 - 1, -1):
            this_sum = (ord(larger[i + buffer]) - ord("0")) + (ord(smaller[i]) - ord("0")) + carry_digit
            new_dig = this_sum % 10
            carry_digit = this_sum // 10
            res = chr(new_dig + ord("0")) + res

        if len(larger) > len(smaller):
            res = addStringsHelper(larger[:buffer], chr(carry_digit + ord("0")), res)
        elif carry_digit:
            res = chr(carry_digit + ord("0")) + res

        return res

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return addStringsHelper(num1, num2, "")
