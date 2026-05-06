class Solution:
    def intToRoman(self, num):

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        ans = ""

        for i in range(len(values)):

            while num >= values[i]:
                ans += symbols[i]
                num -= values[i]

        return ans


# VS Code Testing
num = int(input("Enter an integer (1 to 3999): "))

obj = Solution()
result = obj.intToRoman(num)

print("Roman numeral is:", result)