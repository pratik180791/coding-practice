def solution(S):
    # write your code in Python 3.6
    pref = set()
    suff = set()
    ans = 0
    pref_arr, suff_arr = [0 for _ in range(len(S))], [0 for _ in range(len(S))]

    for i, j in enumerate(S):
        print(i, pref, pref_arr)
        if S[i] == "x" or S[i] == "y":
            pref.add(S[i])
        pref_arr[i] = len(pref)

    print(pref_arr, suff_arr)

    for i in range(len(S)-1, 0, -1):
        if S[i] == "x" or S[i] == "y":
            suff.add(S[i])
        suff_arr[i] = len(suff)

    print(pref_arr, suff_arr)
    for i in range(0, len(S)-1, 1):
        #print(i, pref_arr[i])
        if pref_arr[i] == 0 or pref_arr[i]==2 or suff_arr[i+1]==0 or suff_arr[i+1]==2:
            ans+=1
    print(pref_arr, suff_arr)
    return ans

#op =solution("xzzzy")
op =solution("ayxbx")
op =solution("apple")
op = solution("toyxmy")
print(op)
