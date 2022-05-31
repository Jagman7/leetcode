class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.upper()
        roman_mapper = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        # print(roman_mapper)
        subtraction = {
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }
        # print("Input", s)
        # MCMXCIV

        total_int = 0

        for key in subtraction:
            if key in s:
                # print(subtraction[key])
                total_int += subtraction[key]
                s = s.replace(key, '')

        for char in s:
            total_int += roman_mapper[char]

        # print("Final: ",total_int)
        return s
        pass



