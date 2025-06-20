'''
1.Turn the following snippet into a function:

numbers = [1,2,3,4,5]
squares = []
for n in numbers:
squares.append(n*n)
print(squares)

Requirements:
Create def compute_squares(nums: list[int]) -> list[int]
Add a docstring and type hints
Call it on at least two different lists
'''


def compute_squares(nums: list[int]) -> list[int]:
    '''
    takes list as an argument
    appends the square of each number in square list
    returns the square list
    '''
    square= []
    for n in nums:
        square.append(n * n)
    return square


if __name__ == "__main__":

    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 10]
    print(compute_squares(l1))  
    print(compute_squares(l2))
