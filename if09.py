def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    x1 = a//10 #5
    x2 = a%10 # 7
    y = x2*10+x1 
    
    if y <= a :
        return True
    if y > a :
        return False
print(main(57))

