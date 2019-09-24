def AnaCheck(word1,word2):
    return sorted(word1) == sorted(word2)
W1 = input("elso:")
W2 = input("masodik:")
AN = AnaCheck(W1,W2)
print(str(AN))