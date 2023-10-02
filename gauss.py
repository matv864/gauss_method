def find_nod(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return find_nod(a, b % a)

def find_nok(a, b):
    return (a * b) // find_nod(a, b)

def make_simple(arr):
    delit = 2
    min_arr = min(filter(bool, arr))
    while delit <= min_arr:
        new_arr = []
        for i in arr:
            if i % delit == 0:
                new_arr.append(i // delit)
        if len(new_arr) == len(arr):
            arr = new_arr
        else:
            delit += 1
    return arr




def prepare_matrix(matrix, from_str):
    if matrix[from_str][from_str] != 0:
        return 
    for st in range(from_str + 1, len(matrix)):
        if matrix[st][from_str] != 0:
            matrix[st], matrix[from_str] = matrix[from_str], matrix[st]
            return
    

def solve_string(matrix, from_str):
    first_coef = matrix[from_str][from_str]
    for st in range(from_str + 1, len(matrix)):
        now_coef = matrix[st][from_str]
        if now_coef == 0:
            continue
        nok = find_nok(abs(first_coef), abs(now_coef))
        multiple_start_str = abs(nok // first_coef)
        multiple_now_str = abs(nok // now_coef)
        # print(multiple_start_str, multiple_now_str)
        for id_ in range(from_str, len(matrix[st])):
            if (first_coef * now_coef <= 0):
                matrix[st][id_] = matrix[st][id_] * multiple_now_str + matrix[from_str][id_] * multiple_start_str 
            else:
                matrix[st][id_] = matrix[st][id_] * multiple_now_str - matrix[from_str][id_] * multiple_start_str

def get_answer(matrix):
    answ = [None for _ in range(len(matrix[0])-1)]
    for string_matrix in matrix[::-1]:
        coef = None
        id_x = None
        left_part = 0
        right_part = string_matrix[-1]
        for i in range(len(string_matrix)-1):
            if string_matrix[i] != 0:            
                if not(answ[i] is None):
                    left_part += (string_matrix[i] * answ[i])
                else:
                    if coef is None:
                        coef = string_matrix[i]
                        id_x = i
                    else:
                        # print("its bad")
                        # print(i, string_matrix, answ)
                        break # error                 
        else:
            if coef is None:
                if left_part != right_part:
                    print("несовместимая")
                    return []
            else:
                answ[id_x] = (right_part - left_part) / coef

        # print(string_matrix, answ)
    return answ




        

def solving_system(matrix):
    for i in range(len(matrix)):
        matrix[i] = make_simple(matrix[i])
    for st in range(len(matrix)):
        
        prepare_matrix(matrix, st)
        solve_string(matrix, st)


        for i in range(len(matrix)):
            matrix[i] = make_simple(matrix[i])

    print(*matrix, sep="\n")
        
    return get_answer(matrix)


if __name__ == "__main__":
    s = open("input.txt", "r").read().split("\n")
    n, m = map(int, s[0].split())
    matrix = [[int(j) for j in i.split()] for i in s[1:m+1]]
    print(*matrix, sep="\n")
    print("\n\n")
    print("answ:", solving_system(matrix))
    



