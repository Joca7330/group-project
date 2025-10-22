# Given an integer n, return a string array answer where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
# Example:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]


def fizzBuzz(n):
    """
    Returns a string array where:
    - "FizzBuzz" if i is divisible by both 3 and 5
    - "Fizz" if i is divisible by 3
    - "Buzz" if i is divisible by 5
    - String of i otherwise
    
    Args:
        n: Integer representing the range [1, n]
    
    Returns:
        List of strings following FizzBuzz rules
    """
    answer = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    
    return answer


# Test with the example
if __name__ == "__main__":
    n = 5
    result = fizzBuzz(n)
    print(f"Input: n = {n}")
    print(f"Output: {result}")
    
    # Additional test case
    n = 15
    result = fizzBuzz(n)
    print(f"\nInput: n = {n}")
    print(f"Output: {result}")