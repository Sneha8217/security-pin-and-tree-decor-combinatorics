def find_possible_combinations(n, b, c, a):
    """
    Write your logic here.
    Parameters:
        n (int): Number of accessories required
        b (int): Number of B accessories available
        c (int): Number of C accessories available
        a (int): Number of A accessories available
    Returns:
        list: List of strings, each string representing a valid combination
    """
    result = []
    
    def backtrack(current, remaining_b, remaining_c, remaining_a):
        if len(current) == n:
            result.append(current)
            return
        
        if remaining_b > 0:
            backtrack(current + "B", remaining_b - 1, remaining_c, remaining_a)
        if remaining_c > 0:
            backtrack(current + "C", remaining_b, remaining_c - 1, remaining_a)
        if remaining_a > 0:
            backtrack(current + "A", remaining_b, remaining_c, remaining_a - 1)
    
    backtrack("", b, c, a)
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    b = int(data[1])  # Second input is the integer B
    c = int(data[2])  # Third input is the integer C
    a = int(data[3])  # Fourth input is the integer A
    
    # Call user logic function and get the result
    result = find_possible_combinations(n, b, c, a)
    
    # Print each combination in a new line
    for combination in result:
        print(combination)

if __name__ == "__main__":
    main()