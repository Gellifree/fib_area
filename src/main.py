#!/usr/bin/python3

def fibanocci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n > 1:
        memo[n] = fibanocci(n-1, memo) + fibanocci(n-2, memo)
        return memo[n]
    else:
        return 1

def generate_data(n):
    result = []
    for i in range(n+2):
        result.append([])

    for i in range(len(result)):
        for j in range(len(result)):
            result[j].append(0)
    return result

def fill_fence(matrix):
    j = len(matrix)-1
    for i in range(len(matrix)):
        matrix[i][0] = fibanocci(i)
        matrix[j-i][j] = fibanocci(i)
        matrix[0][i] = fibanocci(i)
        matrix[j][j-i] = fibanocci(i)

def draw_matrix(matrix):
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(f' [{matrix[j][i]}]\t', end='')
        print()
    print()

def generate_sides(i,j):
    result = []
    result.append([i, j-1])
    result.append([i, j+1])
    result.append([i-1, j])
    result.append([i+1, j])
    return result

def valid_sides(size, i,j):
    end_result = []
    result = generate_sides(i,j)
    for k in range(len(result)):
        if(result[k][0] < 0 or result[k][1] < 0 or result[k][0] >= size or result[k][1] >= size):
            pass
        else:
            end_result.append(result[k])

    print(end_result)


def fill_middle(matrix):
    for i in range(1,len(matrix)-1):
        for j in range(1, len(matrix)-1):
            matrix[j][i] = 'F'


def main():
    valid_sides(4,0,0)

    n = 10 
    print(f'{n}*{n}-es mátrix reprezentációja (Kerítéssel)')
    test_array = generate_data(n)

    fill_fence(test_array)
    draw_matrix(test_array)
    fill_middle(test_array)
    draw_matrix(test_array)


if __name__ == "__main__":
	main()
