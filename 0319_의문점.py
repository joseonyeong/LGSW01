print("모든 구구단 출력_중첩 for문")
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j:>2}")
    # 9단 아래에는 나타나지 않도록 하기 위해 if문 설정
    if i <9:   
        print("--------------")
        
j = 4
# 공백도 for문을 넣으면 원하는 모양이 안나옴
# *만 for문을 넣고 공백을 j개 출력하는 변수는 따로 생성
for i in range(1,11,2):
    print(" " * j, end='')
    print('*' * i)
    j -= 1
    
print('중첩 for문으로 반쪽 별')
for j in range(5):
    # 중첩 for문으로 사용하기 위해 i의 범위를 j를 사용해 설정
    for i in range(j+1):
        # 자동 줄바꿈 없애야 별모양 나옴옴
        print('*', end='')
    print()

# 2단 == 3개 차이 1개
# 3단 == 5개 차이 2개
# 4단 == 7개 차이 3개
# 5단 == 9개 차이 4개
print('f-string 사용해서 별 찍기')
n = int(input('원하는 층수: '))
i = 0
for dan in range(1,n+1,1):
    star = '*' * (dan+i)
    # 입력받은 dan과 마지막 별 개수 차이는 단수 2배 - 1 규칙성을 가짐
    print(f"{star:^{n*2-1}}")
    i += 1
    
print("행렬 덧셈")
a = [[1,0,1],[0,2,0],[1,2,1]]
b = [[2,3,1],[0,1,1],[1,1,1]]
c = []
for i in range(len(a)):
    row = []    # 똑같이 다차원으로 받기 위해선 행을 따로 지정해야함
    for j in range(len(a[i])):
        row.append(a[i][j] + b[i][j])   # row로 안 할 경우 1차원으로 append됨
    c.append(row)
print(c)

print('성적처리_이차원리스트')
scores = [[90,85,93],
          [78,92,89]]
row = []
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

# ver2
total = []
# 세로 버전 (각 과목 합합)
row.append(scores[0])
# print(row)  # 90,85,93
for i in range(1,len(scores)):
    for j in range(0,len(scores[i])):
        row[i-1][j] = scores[i][j]+row[i-1][j]
    total.append(row)
print(f"각 과목 합 (세로합): {total}")