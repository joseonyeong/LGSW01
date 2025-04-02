# 공백 제거
print('foo','bar','egg',sep='')
# foobaregg

print('증감연산자 쓰고싶어서')
x=5
for i in range(1,10):
    print('5','*',i,'=',x)
    x+=5
    i+=1

ssss="""hello,
        "easy" python
    """
print(ssss)

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
## 왜 공백이 출력될까?
## 코드에서 줄을 맞춘다고 들여쓰기가 자동으로 되었기 때문에 공백이 생김

# 무한루프로 돌리되, 0을 누르면 끝내게 만들어보자    
while True:
    dan2 = int(input("단수를 입력하세요(끝내려면 0을 누르세요.): "))
    if dan2==0:
        break
    for i in range(1,11):
        print(f"{dan2} * {i} = {dan2*i}")
