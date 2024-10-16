import numpy as np
from numpy import ndarray


def fuzzify( matrix : ndarray , answers : ndarray, total_respondents : int) -> ndarray:
    choices = []
    for i in answers:
        choices.append(i/total_respondents)

    print("choices", choices)
    row, col = matrix.shape

    for i in range(row):
        for j in range(col):
            matrix[i][j] = choices[i]/choices[j]

    return matrix


def matrix_to_csv(matrix : ndarray , filename : str) -> None:
    np.savetxt(filename, matrix, delimiter=",")


def main():
    total_respondents = 9
    answers = np.array([2,4,6,2,7])
    matrix = np.zeros((len(answers),len(answers)))
    print(fuzzify(matrix, answers, total_respondents))
    matrix_to_csv(matrix, filename="matrix.csv")


if __name__ == '__main__':
    main()
