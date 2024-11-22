def integer_square_root(n):
    """
    Calculate the integer square root of a non-negative number using bit manipulation.

    Args:
    n (int): Non-negative integer to find the square root of.

    Returns:
    int: The integer square root of n.
    """
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    # Start with the result as 0
    result = 0
    
    # Mask to determine where to place the next bit (highest possible bit position)
    bit = 1 << (n.bit_length() - 1)  # Start with the highest power of 2 <= n
    
    while bit > 0:
        # Test whether adding this bit to the result will keep it under the square root
        temp = result + bit
        if temp * temp <= n:
            result = temp
        # Shift the bit one position to the right
        bit >>= 1
    
    return result


# Example usage
if __name__ == "__main__":
    num = 4  # Replace with any number you'd like to compute the square root for
    sqrt_result = integer_square_root(num)
    print(f"The integer square root of {num} is {sqrt_result}.")
