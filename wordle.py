import word
import random

green = (61, 145, 64)
yellow = (255, 215, 0)
gray = (192, 192, 192)
dark_gray = (128, 138, 135)


class Wordle:

    def __init__(self):
        self.words = [['' for _ in range(5)] for _ in range(6)]
        self.colors = [[gray for _ in range(5)] for _ in range(6)]
        self.__word_set = word.getWordSet()
        print(self.__word_set)
        self.__ans = self.__pickWord()


    def __pickWord(self):
        size = len(self.__word_set)
        return self.__word_set[random.randint(0, size - 1)]


    def enter(self, i, j, ch):
        if ch == '-':
            if j > 0:
                j -= 1
                self.words[i][j] = ''
        elif ch == '=':
            if j == 5:
                j += 1
        elif ch != '.':
            if j < 5:
                self.words[i][j] = ch
                j += 1
        return j


    def __check_set(self, i):
        value = ''.join(self.words[i])
        print(value)
        for word in self.__word_set:
            if word == value:
                print(word)
                return True
        return False


    def check(self, i):
        if not self.__check_set(i):
            for j in range(5):
                self.colors[i][j] = gray
                self.words[i][j] = ''
            return -1
        num_correct = 0
        for j in range(5):
            if self.words[i][j] == self.__ans[j]:
                self.colors[i][j] = green
                num_correct += 1
        if num_correct == 5:
            return 1
        for j in range(5):
            if self.colors[i][j] != green:
                for k in range(5):
                    if self.words[i][k] == self.__ans[j]:
                        if self.colors[i][k] == gray:
                            self.colors[i][k] = yellow
                            break
        for j in range(5):
            if self.colors[i][j] == gray:
                self.colors[i][j] = dark_gray
        return 0