def transform_to_dual(dec: int) -> str:
    """Transforms a given decimal number to it's dual representation."""
    if dec == 0:
        return "0"
    outputstring = ""
    while dec > 0:
        remainder = dec % 2
        outputstring = str(remainder) + outputstring
        dec = dec // 2
        
    return outputstring
    raise NotImplementedError()  # TODO: Add implementation


if __name__ == "__main__":
    print(transform_to_dual(13))
    print(transform_to_dual(7))
    print(transform_to_dual(4))
    print(transform_to_dual(9))
    
