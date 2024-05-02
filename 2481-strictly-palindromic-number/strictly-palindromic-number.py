class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range (2,n-1):
            number = find_base(n,i)
            if (check_palindrome(number)):
                continue
            else:
                return False
        return True

def find_base(n,b):
    if n == 0:
        return "0"
    number = ""
    while(n>0):
        num = n%b
        n = n//b
        number+=str(num)
    return number[::-1]

def check_palindrome(number):
    left = 0 
    right = len(number)-1
    while(left<=right):
        if(number[left]==number[right]):
            left+=1
            right-=1
        else:
            return False
    return True
        
