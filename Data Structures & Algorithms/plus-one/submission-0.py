class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        first_sum = digits[-1] + 1
        carry = first_sum // 10
        digits[-1] = first_sum % 10

        for i in range(len(digits) - 2, -1, -1):
            sum = digits[i] + carry
            carry = sum//10
            digits[i] = sum%10
        if carry > 0:
            digits.insert(0, carry)
        return digits
