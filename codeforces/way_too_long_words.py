n = int(input())

for i in range(n):

    word = input()

    lent = len(word)

    new_word = ""
    if lent > 10:
        new_word = word[0] + str(lent-2) + word[lent-1]
    else:
        new_word = word
    
    print(new_word)

        
        