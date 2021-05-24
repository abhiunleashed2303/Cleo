input = ['a string', ['a','b',['1','2', ['5', '7'], '3']], 'spam', ['eggs']]

def itemizeListBacktrack(word, input, r):
    if len(input) == 0:
        return
    for i in range(len(input)):
        if type(input[i]) is list:
            itemizeListBacktrack(word, input[i], r+str(i)+".")
        else:
            print(word + r + str(i) + ":" + " " + input[i])

def itemizeList(word, input):
    itemizeListBacktrack(word, input, ".")

itemizeList("Example", input)


