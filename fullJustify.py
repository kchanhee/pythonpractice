class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        final = list()
        this_word = list()
        if len(A) == 0:
            return []
        for i in A:
            if len(i) > B: # this is impossible to do
                return []
            # need at least 1 space between words
            l = sum(len(s) for s in this_word)
            if (l + len(i) + 1) <= B:
                this_word.append(i)
                this_word.append(' ')
            else:
                final.append(this_word)
                this_word = [i]
                this_word.append(' ')
        else:
            l = sum(len(s) for s in this_word)
            if (l + len(i) + 1) <= B:
                this_word.append(i)
                # this_word.append(' ')
                final.append(this_word)
            else:
                final.append(this_word)
        word_list = []
        print final
        for j in final:
            l = sum(len(j[s]) for s in range(0,len(j),2))
            # need to reprocess line to add padding
            word_list.append(self.processLine(j, l, B))

        return word_list

    def processLine(self, line, l, B):
        print line
        word = line[0]

        w_count = len(line) / 2 - 1
        sp_count = B - l # spaces left
        s = 1 # space
        for i in range(2, len(line), 2):
            if w_count > 0:
                if sp_count % w_count == 0:
                    s = sp_count / w_count
                    # print 's = ' + str(s)
                    sp_count -= s
                    word += s * ' '
                else:
                    s = sp_count / w_count + 1
                    # print 's = ' + str(s)
                    sp_count -= s
                    word += s * ' '

            w_count -= 1
            word += line[i]
        word += ' ' * sp_count
        return word
