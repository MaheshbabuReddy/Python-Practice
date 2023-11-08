class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        prev_value = 0  # To keep track of the previous numeral's value

        for char in s:
            value = translations[char]
            if value > prev_value:
                number += value - 2 * prev_value  # Subtract previous value twice to correct for addition in earlier step
            else:
                number += value
            prev_value = value

        return number

# Creating an instance of the Solution class
solution = Solution()

# Converting the Roman numeral "XXIV" to an integer
result = solution.romanToInt("VI")
print(result)  # Output will be 24
