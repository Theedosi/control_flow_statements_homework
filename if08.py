def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 0 and a%2==1 :
        return  "positive odd number"
    if a > 0 and a%2==0 :
        return "positive even number"
    if a%2==1 and a<0 :
        return "negative odd number"
    if a%2==0 and a<0 :
        return  "negative even number"
    if a==0 :
        return "the number is zero"
    