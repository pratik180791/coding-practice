words = ["animosity", "encourage"]
words_to_syn = ["encourage:urge,boost,inspire", "animosity:hate"]
words_to_antonyms= ["animosity:amity,like"]

def word_splitter(word_to_split):
    split_dictionary = {}
    for i in word_to_split:
        wrd, sub_wrd = i.split(":")
        split_dictionary[wrd] = sub_wrd.split(",")
    return split_dictionary

def check_substr(substr, main_str):
    temp = []
    for i in substr:
        temp.append(i in main_str)
    return set(temp)

def findKangarooScore(words, wordsToSynonyms, wordsToAntonyms):
    synonyms = word_splitter(wordsToSynonyms)
    antonyms = word_splitter(wordsToAntonyms)
    cnt = 0
    for i, j in synonyms.items():
        if i not in words:
            continue
        for sub_wrd in j:
            #print([c in i for c in sub_wrd.split()])
            res = check_substr(sub_wrd, i)
            if len(res) == 1 and res.pop() == True:
                cnt+=1
    for i, j in antonyms.items():
        if i not in words:
            continue
        for sub_wrd in j:
            # print([c in i for c in sub_wrd.split()])
            res = check_substr(sub_wrd, i)
            if len(res) == 1 and res.pop() == True:
                cnt += 1
    return cnt
    #for i in words_to_antonyms:

    print(synonyms)
    print(antonyms)

findKangarooScore(words, words_to_syn,words_to_antonyms)
st = "abc"
st1 = "adbdcd"

temp = []
for i in st:
    temp.append(i in st1)
print(len(set(temp)))
#print(set(temp)[0])