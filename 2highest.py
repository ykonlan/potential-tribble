#Given a list of numbers, find the first number that appears only once in the list. 
# If all numbers repeat, return "No unique number found".


def justonce(numlist):
    from collections import Counter
    num_dict = Counter(numlist)
    for x in numlist:
        if num_dict[x] == 1:
            return f"{x} is the first number that occurs once" 
    return "None found"


numlist = list(map(int,input("Enter numbers, sep by space\n").split()))
print(justonce(numlist))
    