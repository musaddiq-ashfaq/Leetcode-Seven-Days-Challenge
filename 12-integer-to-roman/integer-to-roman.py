class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        integers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        i = len(integers) - 1
        ans = ""
        while(num>0):
            if(integers[i] <= num):
                num = num - integers[i]
                ans += roman[i]
            else:
                i-=1
        return ans
        