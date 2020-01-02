def lengthOfLongestSubstring(s):
    temp = ''
    best=0
    for i in range(0,len(s)):
        while s[i] in temp:
            temp=temp[1:i+1]
        best = max(best,len(temp))
        temp+=s[i]
        
    return best


