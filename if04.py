def main(a,b,c):
    """
    Find number of positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """

    sumx = 0
    if a > 0:
        sumx+=1
    if b >0 :
        sumx +=1
    if c > 0 :
        sumx +=1
    return sumx
print(main(1,2,-3))