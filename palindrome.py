# the number is palindrome or not


def is_palindrome(num):
    
    n = num
    
    reverse = 0
    
    while n > 0:
        
        lastdigit = n % 10
        
        reverse = reverse * 10 + lastdigit
        
        n = n // 10
        
    return reverse == num

print(is_palindrome(129321))  # True