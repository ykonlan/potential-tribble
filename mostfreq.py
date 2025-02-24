#Write a function that takes a list of numbers as input and returns the number that appears most frequently. 
# If there is a tie, return any one of them.
def mode(numbers):
    from collections import Counter
    counted= Counter(numbers)
    max_vals= max(counted.values())
    mode=[]
    for x, y in counted.items():
        if y ==max_vals:
            mode.append(x)
    return mode

