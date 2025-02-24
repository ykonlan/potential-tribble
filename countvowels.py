def countvowels(phrase):
    vocount=0
    for character in phrase:
        if character in ["a","e","i","o","u"]:
            vocount += 1
    return vocount



phrase=input("Enter your phrase here\n").lower()
if phrase.replace(" ","").isalpha():
    print(countvowels(phrase))
else:
    print("Enter no numbers abeg")

