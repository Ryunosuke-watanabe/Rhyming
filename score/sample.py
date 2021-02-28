import MeCab
import string
import unicodedata
import re
import itertools
from pykakasi import kakasi

# t = MeCab.Tagger()

class RhymeSearch():
    def __init__(self):
        self.kakasi = kakasi()

    def rhyme_to_ans(self, rhyme_dict, hira_list):
        rhyme_ans = {}
        for item in rhyme_dict.items():
            for i in range(len(item[1])):
                if rhyme_ans.setdefault(item[0]) == None:
                    rhyme_ans[item[0]] = hira_list[item[1][i][0]:item[1][i][1]]
                else:
                    ans = rhyme_ans[item[0]]
                    ans_list = []
                    if type(ans) == str:
                        rhyme_ans[item[0]] = [hira_list[item[1][i][0]:item[1][i][1]], ans]
                    else:
                        for l in range(len(ans)):
                            ans_list.append(ans[l])
                        rhyme_ans[item[0]] = ans_list + [hira_list[item[1][i][0]:item[1][i][1]]]

        return rhyme_ans

    def kana_to_roma(self, kana_list):
        self.kakasi.setMode('H', 'a')
        self.kakasi.setMode('K', 'a')
        self.kakasi.setMode('J', 'a')
        conv = self.kakasi.getConverter()
        roma_list = []
        for item in kana_list:
            roma_list.append(conv.do(item)[-1])
        moji = ''.join(roma_list)
        return moji

    def split_str(self, hira_txt):
        str_list = []
        for i in range(len(hira_txt)):
            if hira_txt[i] == 'ー':
                str_list.append(hira_txt[i-1])
            else:
                str_list.append(hira_txt[i])
        return str_list

    def main(self, txt):
        from pykakasi import kakasi
        ori = txt
        txt = unicodedata.normalize("NFKC", txt)
        table = str.maketrans("", "", string.punctuation  + "「」、。・")
        txt = txt.translate(table)
        txt = txt.replace('\ufeff', '')
        # txt = txt.translate(str.maketrans( '', '',string.punctuation))
        kakasi = kakasi()
        kakasi.setMode('J', 'H')
        conv = kakasi.getConverter()
        hira = conv.do(txt)

        hira_list = self.split_str(hira)

        boin = self.kana_to_roma(self.split_str(hira_list))

        hira_list = ''.join(hira_list)
        rhyme_dict = {}

        for i in range(3, 6+1):
            all = itertools.product('aiueo', repeat=i)
            for x in all:
                strig = ''.join(x)
                ans = [item.span() for item in re.finditer(strig, boin)]
                if len(ans) >= 2:
                    rhyme_dict[strig] = ans
        
        rhyme_ans = self.rhyme_to_ans(rhyme_dict, hira_list)

        return ori, rhyme_ans

RS = RhymeSearch()
a, b = RS.main('ライム　タイム　タイプ　ワイプ')
print(b)