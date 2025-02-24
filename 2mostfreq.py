def secondmf(numbers):
   from collections import Counter
   count_dict= Counter(numbers)
   valuess= count_dict.values()
   maxrem=list(map(int,valuess))
   if len(set(maxrem)) == 1:
      return "No second highest number"
   maxrem.remove(max(maxrem))
   max_value2=max(maxrem)
   mode=[]
   for x, y in count_dict.items():
      if y == max_value2:
         mode.append(x)
   return mode 
try:
    numbers=list(map(int,(input("Enter the set of numbers, separate by space").split())))
    print(secondmf(numbers))
except ValueError:
    print("Please enter a valid input")
