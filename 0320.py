# print("성적_선생님.ver")
# scores = [[90,85,93],
#           [78,92,89]]
# total_by_student = [0,0]
# total_by_subject = [0,0,0]
# for st in range(len(scores)):
#     for sb in range(len(scores[0])):
#         total_by_student[st] += scores[st][sb]
#         total_by_subject[sb] += scores[st][sb]
# print(total_by_student)
# print(total_by_subject)

# print()
# a = [[1,0,1],[0,2,0],[1,2,1]]
# b = [[2,3,1],[0,1,1],[1,1,1]]        
# z = []
# for w in range(len(a)):
#     for h in range(len(a[0])):
#         z[w][h] = a[w][h] + b[w][h]
# print(z)       

# print("모든 원소에 곱하기 2")
# aa = [[1,2,3],[4,5,6],[7,8,9]]
# for w in range(len(aa)):
#     for h in range(len(aa[0])):
#         aa[w][h] *= 2
# print(aa) 
        
# print("행렬 덧셈")
# a = [[1,0,1],[0,2,0],[1,2,1]]
# b = [[2,3,1],[0,1,1],[1,1,1]]
# c = []
# if len(a) == len(b):
#     for i in range(len(a)):
#         row = []    # 똑같이 다차원으로 받기 위해선 행을 따로 지정해야함
#         if len(a[i]) == len(b[i]):
#             for j in range(len(a[i])):
#                 row.append(a[i][j] + b[i][j])
#             c.append(row)
#         else:
#             c = []  # 초기화
#             print("두 행렬의 열의 개수가 일치하지 않습니다.")
# else:
#     print("두 행렬의 행의 개수가 일치하지 않습니다.")
# print(c)     

# a = [1,2,3,4]
# b = [1,2,3,4]
# c = []
# num = 0
# for i in range(len(a)):
#     for j in range(len(b)):
#         num += a[i] * b[j]
#     c.append(num)
#     num = 0
# print(c)


# print("행렬 곱셈")
# a = [[1,0,1],[0,2,0],[1,2,1]]
# b = [[2,3,1],[0,1,1],[1,1,1]]
# c = []
# # num = 0

# # if len(a)>len(b):
# #     wc = len(a)
# # else:
# #     wc = len(b)
# # if len(a[0])>len(b[0]):
# #     hc = len(a[0])
# # else:
# #     hc = len(b[0])

# # # 00*00+01*10   00*01+01*11     00*02+01*12
# # # 10*00+11*10   10*01+11*11     10*02+11*12
# # for i in range(wc):
# #     for j in range(hc):
# #         num += a[i][j]*b[j][i]
# #         c.append(num)
# # print(c)
# tmp = []
# for i in range(len(a)):
#     row = []
#     for j in range(len(b[0])):
#         sum = 0
#         for n in range(len(a[0])):
#             sum += a[i][n] * b[n][j]
#         row.append(sum) # 원소 하나 (더해진 값)
#     tmp.append(row)   # 행 한 줄
# # tmp.append(row)   # 일차원 배열로 저장
# print(tmp) 

# print("딕셔너리")
# en2ko = {
#     'book' : '책',
#     'snake': '뱀',
#     'language': '언어'
# }
# ko2en = {}

# for k,v in en2ko.items():
#         # setdefault함수는 키-값 추가, 들어있는 값 수정 불가
#     ko2en.setdefault(v,k)
# print(ko2en)

# print('성적처리_딕셔너리.ver')

# data = [
#     {'name': '철수', 'math': 85, 'eng': 90, 'sci': 75},
#     {'name': '준호', 'math': 73, 'eng': 85, 'sci': 93},
#     {'name': '영희', 'math': 92, 'eng': 88, 'sci': 90}
# ]

# result = {}

# for d in data:
#     total = 0  # 총점 초기화
#     count = 0  # 과목 수 초기화
    
#     for k, v in d.items():
#         if k != 'name':  # 이름 제외하고 점수만 합산
#             total += v
#             count += 1
    
#     avg = total / count  # 평균 계산
    
#     result[d['name']] = {'total': total, 'average': round(avg, 4)}

# print(result)

# print('리스트 컴프리헨션')
# n = int(input("n: "))
# L = []
# for i in range(1, n+1):
#     L.append(i)
# print(L)

# L = [i for i in range(1, n+1)]

# print("몫과 나머지 구하는 함수")
# def func(n, k):
#     result = []
#     result.append(10 // k) # 몫
#     result.append(10 % k)  # 나머지
#     return result
# def func2(n,k):
#     while True:
#         if n < 0 or k < 0 :
#             print('양수로 입력하세요')
#         else:
#            result = []
#            result.append(10 // k) # 몫
#            result.append(10 % k)  # 나머지
#            return result    
# n = int(input('나눠질 수 입력: '))
# k = int(input('나눌 수 입력: '))
# print(func(n,k))
# print(func2(n,k))

# print("평균 구하는 함수")
# def func(arr):
#     sum = 0
#     for i in arr:
#         i = int(i)
#         sum += i
#     mean = sum // len(arr)
#     return mean
# arr = input("리스트 또는 튜플 입력(숫자 사이는 공백으로 입력): ")
# arr = arr.split()
# print(func(arr))