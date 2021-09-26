import os
import time

class Recursion:
    @staticmethod
    def fibanocci(n, memo = {}):
        if n in memo:
            return memo[n]
        if n==0:
            return 0
        if n > 1:
            memo[n] = Recursion.fibanocci(n-1, memo) + Recursion.fibanocci(n-2, memo)
            return memo[n]
        else:
            return 1

    @staticmethod
    def generate_map(n):
        result = []
        for i in range(n+2):
            result.append([])

        for i in range(len(result)):
            for j in range(len(result)):
                result[j].append(0)
        return result

    @staticmethod
    def generate_all_sides(i,j):
        result = []

        result.append([i, j-1])
        result.append([i, j+1])
        result.append([i-1, j])
        result.append([i+1, j])

        return result

    @staticmethod
    def validate_sides(size, i,j):
        result = []

        all_sides = Recursion.generate_all_sides(i,j)

        for k in range(len(all_sides)):
            if(not (all_sides[k][0] < 0 or all_sides[k][1] < 0 or all_sides[k][0] >= size or all_sides[k][1] >= size)):
                result.append(all_sides[k])

        return result

    @staticmethod
    def fill_fence(matrix):
        j = len(matrix)-1
        for i in range(len(matrix)):
            matrix[i][0] = Recursion.fibanocci(i)
            matrix[j-i][j] = Recursion.fibanocci(i)
            matrix[0][i] = Recursion.fibanocci(i)
            matrix[j][j-i] = Recursion.fibanocci(i)

    @staticmethod
    def draw_matrix(matrix):
        print()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(f' {matrix[j][i]};', end='')
            print()
        print()

    @staticmethod
    def make_csvformat(matrix):
        result = '"x", "y", "value"\n'
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result +=f'{i},{j},{matrix[j][i]}\n'
        return result

    @staticmethod
    def sum_all_sides(side_list, matrix):
        sum = 0
        for i in range(len(side_list)):
            sum += matrix[side_list[i][0]][side_list[i][1]]
        return sum / 4

    @staticmethod
    def fill_middle(matrix):
        for i in range(1,len(matrix)-1):
            for j in range(1, len(matrix)-1):
                all_sides = Recursion.generate_all_sides(i,j)
                matrix[j][i] = Recursion.sum_all_sides(all_sides, matrix)
                #print(matrix[j][i])

if __name__ == "__main__":
    rec = Recursion()
    map = rec.generate_map(100)
    rec.fill_fence(map)
    #rec.draw_matrix(map)
    #map[15][15] = 300


    for i in range(1000):
        rec.fill_middle(map)
        #rec.draw_matrix(map)
        #time.sleep(0.1)
        #os.system('clear')
    #rec.draw_matrix(map)
    result = rec.make_csvformat(map)
    f = open("data.csv", 'w')
    f.write(result)
    f.close()
