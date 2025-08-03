# I see a lot of jokes about this on reddit,
# so I thought I would try it out
def iseven(n):
    """
    Check if a number is even.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if n is even, False otherwise.
    """

    if isinstance(n, int):
        ns = str(n)
        if ns.endswith("0") or ns.endswith("2") or ns.endswith("4") or ns.endswith("6") or ns.endswith("8"):
            return True
        elif ns.endswith("1") or ns.endswith("3") or ns.endswith("5") or ns.endswith("7") or ns.endswith("9"):
            return False
        else:
            raise ValueError("Input is not a valid integer well it shouuld be but it somehow doesn't end with an number")
    else:
        raise TypeError("Input must be an integer")

if __name__ == "__main__":
    n = input("Enter a interger: ")
    try:
        n = int(n)
    except ValueError:
        print("Please enter a valid integer.")
        exit(1)
    print(iseven(n))