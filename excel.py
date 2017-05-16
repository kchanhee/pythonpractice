class Solution:
    # @param A : integer

    # @return a strings
    def convertToTitle(self, A):
        from string import ascii_uppercase as au
        alpha_dic = {i % 26 : x for i, x in enumerate(au, 1)}

        digits = []

        while A:
            d = A % 26
            digits.append(d)
            A //= 26
            # print A

        print digits

        print alpha_dic
        final_str = ""
        for n in reversed(digits):
            final_str += alpha_dic[n]
        return final_str

    # def get_digit(self, num):
    #     while num:
    #         num, remainder = divmod(num, 26)
    #         print remainder




print Solution().convertToTitle(943566)
# print Solution().get_digit(943566)