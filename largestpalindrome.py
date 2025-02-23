def findlargest(numlist):
    pallist=[]
    for x in numlist:
        if str(x) == str(x)[::-1]:
            pallist.append(x)
    if pallist:
        return max(pallist,key=int)
    else:
        return "No palindrome wai" 

try:
    numlist= list(map(int,input("Enter your numbers, separated by space.").split()))
    print(findlargest(numlist))

except ValueError:
    print("Enter numbers separated by a space massa!")