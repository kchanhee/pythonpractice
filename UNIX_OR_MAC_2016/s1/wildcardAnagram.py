def isWildCardAnagram(in_word, out_word):
    in_word_d = letterDict(in_word)
    out_word_d = letterDict(out_word)
    for i in out_word_d.keys():
        if i == "*": # ignore wild-card chars
            continue
        if i in in_word_d:
            # if there are more of the same letter in out-word then it's not an anagram
            if out_word_d[i] > in_word_d[i]: 
                return "N"
        else: # if letter isn't in the in-word then it's not an anagram
            return "N"
    return "A"


def letterDict(word):
    word_d = {}
    for c in word:
        if c in word_d:
            word_d[c] += 1
        else:
            word_d[c] = 1
    return word_d

for i in range(18):
    infile = open("s1." + str(i+1) + ".in","r")
    outfile = open("s1." + str(i+1) + ".out","r")
    in_word = infile.readline().rstrip()
    out_word = infile.readline().rstrip()
    print "input:  |" + in_word
    print "output: |" + out_word
    answer = outfile.readline().rstrip()
    print "                    Checking Algo                  "
    print "---------------------------------------------------\n"
    print isWildCardAnagram(in_word, out_word) == answer
    print
    print "---------------------------------------------------\n"
