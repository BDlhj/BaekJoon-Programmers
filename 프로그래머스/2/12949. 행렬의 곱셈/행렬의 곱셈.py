def solution(arr1, arr2):
    arr1_row_num, arr1_col_num = len(arr1), len(arr1[0])
    arr2_row_num, arr2_col_num = len(arr2), len(arr2[0])
    
    answer = [[0] * arr2_col_num for _ in range(arr1_row_num)]
    
    for i in range(arr1_row_num):
        for j in range(arr2_col_num):
            for k in range(arr1_col_num):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer