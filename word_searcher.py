import enchant

# Stores necessary information about the puzzle
class Puzzle():
    MIN_STR_LENGTH = 4

    def __init__(self, matrix, word_bank):
        # An array of equal-length strings where each string represents one row of the puzzle 
        self.matrix = matrix
        # Stores the english dictionary
        self.d = enchant.Dict("en_US")
        # Stores solutions in the format [start_row, end_row, start_column, end_column]
        self.solution = self.solve()
        # An array of the words in the puzzle.
        self.word_bank = set(self.solution.keys())

    def solve(self):
        # Horizontal Search
        solution = {}
        for row_num in range(len(self.matrix)):
            for col_num in range(len(self.matrix[0])):
                for str_length in range(Puzzle.MIN_STR_LENGTH, len(self.matrix[0]) - col_num + 1):
                    test_string = self.matrix[row_num][col_num: col_num + str_length]
                    if (self.d.check(test_string)):
                        solution[test_string] = [row_num, row_num, col_num, col_num + str_length]
                    if (self.d.check(test_string[::-1])): 
                        solution[test_string[::-1]] = [row_num, row_num, col_num + str_length, col_num]
        
        # Vertical Search
        for col_num in range(len(self.matrix[0])):
            for row_num in range(len(self.matrix)):
                for str_length in range(Puzzle.MIN_STR_LENGTH, len(self.matrix) - row_num + 1):
                    test_string = ""
                    for i in range(row_num, row_num + str_length):
                        test_string += self.matrix[i][col_num]
                    if (self.d.check(test_string)):
                        solution[test_string] = [row_num, row_num + str_length, col_num, col_num]
                    if (self.d.check(test_string[::-1])):
                        solution[test_string[::-1]] = [row_num + str_length, row_num, col_num, col_num]
         
        # Diagonal Search 
        for col_num in range(len(self.matrix[0])):
            for row_num in range(len(self.matrix)):
                # Forward Direction
                for str_length in range(Puzzle.MIN_STR_LENGTH, min(len(self.matrix) - row_num + 1, len(self.matrix[0]) - col_num + 1)):
                    test_string = ""
                    for i in range(row_num, row_num + str_length):
                        test_string += self.matrix[i][col_num + (i - row_num)]
                    if (self.d.check(test_string)):
                        solution[test_string] = [row_num, row_num + str_length, col_num, col_num + str_length]
                    if (self.d.check(test_string[::-1])):
                        solution[test_string[::-1]] = [row_num + str_length, row_num, col_num + str_length, col_num]
                # Backward Direction
                for str_length in range(Puzzle.MIN_STR_LENGTH, min(row_num + 1, col_num + 1)):
                    test_string = ""
                    for i in range(row_num - str_length, row_num):
                        test_string += self.matrix[row_num - i][i]
                    if (self.d.check(test_string)):
                        solution[test_string] = [row_num, row_num - str_length, col_num, col_num - str_length]
                    if (self.d.check(test_string[::-1])):
                        solution[test_string[::-1]] = [row_num - str_length, row_num, col_num - str_length, col_num]
        return solution

    def print_puzzle(self):
        for word in self.matrix:
            print(word)

    def print_solution(self):
        print(self.solution)

    def found_entire_word_bank(self):
        return self.word_bank == self.solution.keys()


p1 = Puzzle(["dessemmotivatesd", "highlightedjstoe", "ebefogviolinists", "mhbspnnijbobdeaa", "asctpieiuikonuge", "ureaotsrsctvares", "neccrnesaoaesoli", "dhyctaubsdprstzd", "essaucewdacviesm", "rottnseeivwilrfq", "skioienabajegsse", "macstddsdrowyeky", "cillydielbasysir", "zxyqsestimatetty"], ["pa", "apple", "beep", "weed", "weeds", "beds", "bee", "me", "male"])
p1.print_puzzle()
