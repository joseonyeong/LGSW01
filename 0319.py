# print("모든 구구단 출력_중첩 for문")
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j:>2}")
#     # 9단 아래에는 나타나지 않도록 하기 위해 if문 설정
#     if i <9:   
#         print("--------------")

# print("반쪽 별")
# for i in range(1,6):
#     print('*' * i)

# print('중첩 for문으로 반쪽 별')
# for j in range(5):
#     for i in range(j+1):
#         print('*', end='')
#     print()
    
# print("거꾸로 반쪽 별")
# for i in range(5,0,-1):
#     print('*' * i)
    
# for j in range(5,0,-1):
#     for i in range(j):
#         print('*', end='')
#     print()

# # print('별')
# # 공백 j개 i 공백 4개
# # 공백 j-1개 i+2 공백 3개
# # 공백 2개 ***** 공백 2개
# # 공백 1개  공백 1개
# # 공백 0개  공백 0개
# j = 4
# # 공백도 for문을 넣으면 원하는 모양이 안나옴
# # *만 for문을 넣고 공백을 j개 출력하는 변수는 따로 생성
# for i in range(1,11,2):
#     print(" " * j, end='')
#     print('*' * i)
#     j -= 1

# print('f-string 사용해서 별 찍기')
# n = int(input('별 개수: '))
# for i in range(1,n+1,2):
#     star = '*' * i
#     print(f"{star:^{n}}")

# # 2단 == 3개 차이 1개
# # 3단 == 5개 차이 2개
# # 4단 == 7개 차이 3개
# # 5단 == 9개 차이 4개
# print('f-string 사용해서 별 찍기')
# n = int(input('원하는 층수: '))
# i = 0
# for dan in range(1,n+1,1):
#     star = '*' * (dan+i)
#     # 입력받은 dan과 마지막 별 개수 차이는 단수 2배 - 1 규칙성을 가짐
#     print(f"{star:^{n*2-1}}")
#     i += 1

# sigletion = ('lion',)
# print(type(sigletion))
# # <class 'tuple'>

# teams = ['타이거즈','라이온즈','트윈스','베어스','위즈','랜더스']
# # enumerate() index와 요소 함께 리턴
# for index, baseball in enumerate(teams):
#     print(f"{index+1}순위: {baseball}")

# teams = ['타이거즈','라이온즈','트윈스','베어스','위즈','랜더스']
# i = 1
# for baseball in teams:
#     print(i, baseball)
#     i += 1
# for i in range(len(teams)):
#     print(i+1, teams[i])

# print("성적처리_리스트")
# jisoo = [90, 85, 93]
# mansoo = [78, 92, 89]
# kor = jisoo[0] + mansoo[0]
# math = jisoo[1] + mansoo[1]
# eng = jisoo[2] + mansoo[2]
# print(f"국어:{kor}, 수학:{math}, 영어:{eng}")

# print("배열로 총점 넣기")
# scores = []
# for i in range(3):
#     scores.append(jisoo[i]+mansoo[i])
# #print(scores)
# print(f"국어:{scores[0]}, 수학:{scores[1]}, 영어:{scores[2]}")

# # print('리스트 합계 구하기')
# nums = [10,4,5,-1,6,12,40]
# evenNum = 0 #짝수번째 합 넣을 변수
# for index, value in enumerate(nums):
#     # index가 짝수인 것만
#     if index % 2 == 0:
#         evenNum += value
# print(f"짝수번째 원소들의 합: {evenNum}")

# print('슬라이싱 사용해서')
# num = 0
# evenNums = nums[1::2]
# for index, value in enumerate(evenNums):
#     print(value)
#     num += value
# print(f"짝수번째 원소들의 합: {num}")  

# print("max값 찾기")
# nums = [-10,-4,-5,-1,-6,-12,-40]
# max = nums[0]
# for num in nums:
#     if max < num:
#         max = num
# print(max)

print("성적처리_이차원리스트")
scores = [[90,85,93],
          [78,92,89]]
row = []
# total = []
#     # 세로 버전 (각 과목 합합)
# row.append(scores[0])
# # print(row)  # 90,85,93
# for i in range(1,len(scores)):
#     for j in range(0,len(scores[i])):
#         row[i-1][j] = scores[i][j]+row[i-1][j]
#     total.append(row)
# print(f"각 과목 합 (세로합): {total}")


for i in range(len(scores[0])):
    S=0
    for j in range(len(scores)):
        S+=scores[j][i]
    row.append(S)
print(row)
       
width = [] 
for k in range(len(scores)):
    w = 0
    for z in range(len(scores[0])):
        w+=scores[k][z]
    width.append(w)    
print(width)    