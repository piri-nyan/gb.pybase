print("Sum of the biggest")

def max_sum(*nums) -> float:
    return sum(sorted(nums)[-2:])

if __name__=="__main__":
    print(max_sum(5, 7, 1, 7, 2, 5, 7, 7, 2, 9, 5, 3))