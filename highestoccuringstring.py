def higoc(thetext):
    from collections import Counter
    textcount_dict=Counter(thetext)
    freqs=textcount_dict.values()
    maxfreq=max(freqs)
    mode=[]
    for x, y in textcount_dict.items():
        if y ==maxfreq:
            mode.append(x)
    return mode












thetext= input("Put your sentence here wai").lower()
import re
thecleantext = re.sub(r'[^a-z]','',thetext)
print(higoc(thecleantext))
