from Color import Coloring

if __name__ == '__main__':
    Solver = Coloring(10)
    choices_of_ls = [
        [{1, 2, 3, 5, 6, 7, 8, 9}, {1, 2, 3, 6, 7, 8, 9}, {4}, {2, 3, 5, 6, 7, 8, 9}, {0}, {1, 2, 3, 5, 6, 7, 8, 9},
         {1, 2, 3, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9}, {1, 2, 5, 6, 7, 9}, {1, 2, 3, 5, 6, 8, 9}],
        [{0, 1, 2, 4, 6, 7, 8, 9}, {5}, {0, 1, 2, 6, 7, 8, 9}, {2, 4, 6, 7, 8, 9}, {1, 2, 6, 7, 8, 9},
         {0, 1, 2, 4, 6, 7, 8, 9}, {1, 2, 6, 7, 8, 9}, {0, 1, 2, 4, 6, 7, 8, 9}, {3}, {0, 1, 2, 4, 6, 8, 9}],
        [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 6, 7, 8, 9}, {0, 1, 2, 3, 5, 6, 7, 8, 9},
         {2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9},
         {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 4, 5, 6, 7, 9}, {0, 1, 2, 3, 4, 5, 6, 8, 9}],
        [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 6, 7, 8, 9}, {0, 1, 2, 3, 5, 6, 7, 8, 9},
         {2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9},
         {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 4, 5, 6, 7, 9}, {0, 1, 2, 3, 4, 5, 6, 8, 9}],
        [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9}, {2, 3, 4, 5, 6, 7, 8, 9},
         {1, 2, 3, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {0}, {1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 4, 5, 6, 7, 9},
         {1, 2, 3, 4, 5, 6, 8, 9}],
        [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 6, 7, 8, 9}, {0, 1, 2, 3, 5, 6, 7, 8, 9},
         {2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9},
         {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 4, 5, 6, 7, 9}, {0, 1, 2, 3, 4, 5, 6, 8, 9}],
        [{0, 2, 3, 4, 5, 6, 7, 9}, {0, 2, 3, 4, 6, 7, 9}, {0, 2, 3, 5, 6, 7, 9}, {1}, {2, 3, 5, 6, 7, 9},
         {0, 2, 3, 4, 5, 6, 7, 9}, {2, 3, 5, 6, 7, 9}, {0, 2, 3, 4, 5, 6, 7, 9}, {8}, {0, 2, 3, 4, 5, 6, 9}],
        [{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 6, 7, 8, 9}, {0, 1, 2, 3, 5, 6, 7, 8, 9},
         {2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 5, 6, 7, 8, 9},
         {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, {0, 1, 2, 4, 5, 6, 7, 9}, {0, 1, 2, 3, 4, 5, 6, 8, 9}],
        [{0, 1, 2, 3, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 6, 7, 8, 9}, {0, 1, 2, 3, 5, 6, 7, 8, 9}, {2, 3, 5, 6, 7, 8, 9},
         {1, 2, 3, 5, 6, 7, 8, 9}, {0, 1, 2, 3, 5, 6, 7, 8, 9}, {4}, {0, 1, 2, 3, 5, 6, 7, 8, 9}, {0, 1, 2, 5, 6, 7, 9},
         {0, 1, 2, 3, 5, 6, 8, 9}],
        [{1, 2, 3, 5, 6, 8, 9}, {1, 2, 3, 6, 8, 9}, {1, 2, 3, 5, 6, 8, 9}, {0}, {4}, {1, 2, 3, 5, 6, 8, 9},
         {1, 2, 3, 5, 6, 8, 9}, {1, 2, 3, 5, 6, 8, 9}, {1, 2, 5, 6, 9}, {7}]]
    solution = Solver.solve(choices_of_ls)
    print(solution)
