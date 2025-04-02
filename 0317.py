print('fo','d','dd',sep=':')
#fo:d:dd
print('fo','d','dd',end='/n')
#fo d dd/n
print('fo','d','dd')
#fo d dd
# 공백 제거
print('foo','bar','egg',sep='')
# foobaregg
## 줄바꿈 제거
print('fo', end='')
print('d')
# fod
## 줄바꿈
print('fo', end='\n')
print('d')
# fo
# d

print('기본 for문')
for i in range(1,10):
    print('5','*',i,'=',i*5)
# 기본 for문
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
print('배열로')
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    print('5','*',i,'=',i*5)
# 배열로
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
print('증감연산자 쓰고싶어서')
x=5
for i in range(1,10):
    print('5','*',i,'=',x)
    x+=5
    i+=1
# 증감연산자 쓰고싶어서
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45

print('type 확인')
print(type(a))
print(type(10))
print(type(10.0))
print(type(10+10.0))
#int+float = int
print(10+10.0)
print(type(10+10.0))

s="hello \"easy\" python"
print(s)
ss='hello "easy" python'
print(ss)
sss='hello,\n "easy" python'
print(sss)
print(type(s))
print(type(ss))
print(type(sss))
ssss="""hello,
        "easy" python
    """
print(ssss)

print('F-string')
a=100
print(f"a:{a} SUCCESS")
b=100
c=a+b
print(f"{a}+{b}={c}")

print('소수점 이하 셋째 자리까지 부동 소수점 숫자 표시')
a=1.0/3
print(f'{a:.3f}')
print('11칸 채우고 가운데 정렬')
a='hahaha'
print('{:^11}'.format(a))
print(f'{a:_^11}')

print('\n반복 출력')
exstr="""
Python : Guido van Rossum
C++ : Bjarne Stroustrup
Java : Jame Gosling
Pascal : Niklaus Wirth
    """
print(exstr*3)

# 반복 출력
#     Python : Guido van Rossum
#     C++ : Bjarne Stroustrup
#     Java : Jame Gosling
#     Pascal : Niklaus Wirth

#     Python : Guido van Rossum
#     C++ : Bjarne Stroustrup
#     Java : Jame Gosling
#     Pascal : Niklaus Wirth

#     Python : Guido van Rossum
#     C++ : Bjarne Stroustrup
#     Java : Jame Gosling
#     Pascal : Niklaus Wirth

## 왜 공백이 출력될까?
## 코드에서 줄을 맞춘다고 들여쓰기가 자동으로 되었기 때문에 공백이 생김
word1="Python"
str1="Guido van Rossum"
word2="C++"
str2="Bjarne Stroustrup"
word3="Java"
str3="Jame Gosling"
sep=" : "
print(word1+sep+str1)
print(word1,str1,sep=":")
print(word1,str1,sep=sep)
print('가운데 정렬 반복 str')
print(f"{word1:>6}{sep}{str1}")
print(f"{word2:>6}{sep}{str2}")
print(f"{word3:>6}{sep}{str3}")

print('input함수')
name = input('이름을 입력하세요.: ')
color = input('좋아하는 색상을 입력하세요.: ')
input(f'{name}님이 가장 좋아하는 색상은 {color}입니다.')
print('\n')
num1=int(input('첫 번째 숫자를 입력해주세요.: '))
num2=int(input('두 번째 숫자를 입력해주세요.: '))
print('두 수의 합: ',num1+num2)
print('두 수의 차: ',num1-num2)
print('두 수의 곱: ',num1*num2)
print('두 수의 비: ',num1/num2)
# input으로 그대로 받으니 TypeError가 뜸.
# input은 문자열로 받는 함수기 때문에 int로 타입변환을 해줘야됨.

print('BMI 계산')
height=float(input('키: '))
weight=float(input('몸무게: '))
print('bmi: ', weight/height**2)

print('성적 처리기')
name=str(input('너의 이름: '))
KorScore=float(input('국어 점수: '))
EngScore=float(input('영어 점수: '))
MathScore=float(input('수학 점수: '))
total=KorScore+EngScore+MathScore
mean=total/3
print(f'{name}의 총점은 {total}이고 평균은 {mean}입니다.')

'''
composer1 = 'Beethoven'
 composer2 = 'Bach' #들여쓰기 에러
print(f"I love {composer1}'s Symphony No.3 'Eroica'.")
print(f"I love {composer2's Goldberg Variation.") #괄호 오류
print(f"I love {composer3}'s Die ZauberflÃ¶te") #변수 미생성 오류
'''

print('반지름 입력받아 원 둘레, 면적 계산하기')
radius=float(input("원의 반지름을 입력하세요: "))
area=radius**2*3.14
diameter=radius*2*3.14
print(f"반지름이 {radius}인 원의 면적은 {area:.2f}입니다.") 
print(f"이 원의 둘레는 {diameter}입니다.")
print(f"이 원의 지름은 {radius*2}입니다.")

print("수식 표현")
a=10
b=20
x=float(input('x= '))
y=a*x**2+b*x
print(f"y={y}")

print('확률밀도함수의 함숫값')
x=float(input("x: "))
u=float(input("u: "))
a=float(input("a: "))
z=-((x-u)**2)/(2*a**2)
func=(1/(a*2.506))*(2.718**z)
print(f"func: {func:.3f}")

t=True
f=False
print(type(t))
print(t and f) #둘 다 true
print(t or f) # 둘 중 하나가 true
print(not f) #f의 반대
