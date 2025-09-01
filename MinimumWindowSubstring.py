t = "ABC"
s = "ADOBECODEBANC"

if t == "" :  print("t is empty")
count , window = {} , {}


for i in t:
    count[i] = 1 + count.get(i, 0)


have, need = 0 , len(count)  # have unique value of count so we can compare 

res , reslen = [-1 ,-1] , float("infinity")

l = 0

for r in range(len(s)):
    c = s[r]

    window[c] = 1 + window.get(c , 0)

    if c in count and window[c] == count[c]:
        have += 1

    while have == need:

        if (r -l + 1) < reslen:
            res = [l,r]
            reslen = (r - l +1)
        
        window[s[l]] -= 1
        if s[l] in count and window[s[l]] < count[s[l]]:
            have -=1
        
        l += 1
l,r =res
print(s[l:r+1]) if reslen != float("infinity") else  print("")


