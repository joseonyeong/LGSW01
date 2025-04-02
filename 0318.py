# print("로그인 로직")
# passwd = 1234
# inputpasswd = int(input("패스워드 입력: "))
# if passwd == inputpasswd:
#     print("로그인 성공")
# else:
#     print("비번이 틀렸습니다.")
    
# print('for문으로 기회 3번')
# i = 0
# passwd2 = 1111
# for i in range(0,3):
#     inputpasswd2 = int(input(f"비밀 번호를 입력하세요. ({3-i}번 남았습니다.)"))
#     if passwd2 == inputpasswd2:
#         print('로그인 성공')
#         break
#     else:
#         print('틀렸습니다.')      
# # for문으로 기회 3번
# # 비밀 번호를 입력하세요. (3번 남았습니다.)2222
# # 틀렸습니다.
# # 비밀 번호를 입력하세요. (2번 남았습니다.)1234
# # 틀렸습니다.
# # 비밀 번호를 입력하세요. (1번 남았습니다.)1111
# # 로그인 성공
        
# print("BMI 계산기_등급출력")
# weight = float(input("몸무게 입력: "))
# height = float(input("키 입력: "))
# bmi = weight / height**2
# print(f'{bmi:.3f}')
# if bmi < 18.5:
#     print("저체중입니다.")
# elif bmi >= 18.5 and bmi < 23:
#     print("정상입니다.") 
# elif bmi >= 23 and bmi < 25:
#     print("과체중입니다.")
# else:
#     print("비만입니다.")
# # BMI 계산기_등급출력
# # 몸무게 입력: 70
# # 키 입력: 1.65 
# # 25.712
# # 정상입니다.    
 
# print("BMI 계산기_등급출력_조건 하나만 사용")
# weight = float(input("몸무게 입력: "))
# height = float(input("키 입력: "))
# bmi = weight / height**2
# print(f'{bmi:.3f}')
# if bmi < 18.5:
#     print("저체중입니다.")
# elif bmi < 23:
#     print("정상입니다.") 
# elif bmi < 25:
#     print("과체중입니다.")
# else:
#     print("비만입니다.")   
    
# print("while문으로 반복 번수 출력")
# num = int(input("숫자를 입력하세요: "))
# i = 0
# while num > 0: #조건은 해당 코드가 돌 수 있는 조건
#     print(num)
#     num -= 1
#     i += 1
# print(f"while문을 {i}번 반복했습니다.")
    
# print("반복 번수 출력_끝내기 물어보기")
# j = 0
# k = 0
# while True:
#     num = int(input("숫자를 입력하세요: "))
#     while num > 0: #조건은 해당 코드가 돌 수 있는 조건
#         print(num)
#         num -= 1
#         k += 1
#     print(f"while문을 {k}번 반복했습니다.")
#     j += 1
    
#     while True:
#         answer = input('끝내시겠습니까? (Y/N): ').strip().upper()
#         if answer in ['Y', 'N', 'YES', 'NO']:
#             break
#         else:
#             print('Y 또는 N으로 입력하세요.')
            
#     if answer == 'Y' or answer == 'YES':
#         break
#     else:
#         k = 0
#         continue
# print(f"while문을 {j}번 반복했습니다.")            

# print("3의 배수 출력")
# for i in range (1,34):
#     print(i*3, end=' ')
# print('\n')
# for i in range (3, 100, 3):
# 		print(i)

# print("3의 배수 출력_while 버전")
# j = 0
# j *= 0
# while j <100:
#     print(j, end=' ')
#     j += 1

# print("구구단 출력_사용자에게 숫자 받기")
# dan = int(input("단수를 입력하세요: "))
# for i in range(1,11):
#     print(f"{dan} * {i} = {dan*i}")

# # 무한루프로 돌리되, 0을 누르면 끝내게 만들어보자    
# while True:
#     dan2 = int(input("단수를 입력하세요(끝내려면 0을 누르세요.): "))
#     if dan2==0:
#         break
#     for i in range(1,11):
#         print(f"{dan2} * {i} = {dan2*i}")

# print("1에서 n까지 합")
# n = int(input('임의의 자연수를 입력해주세요: '))
# for i in range(1, n+1):
#     i += i
# print(f'1에서 {n}까지 합산한 값은 {i}입니다.')

# print('아이디와 비번을 모두 검사하는 로그인 로직')
# userID = 'love'
# userPASSWD = 1111
# id = input('아이디를 입력해주세요: ')
# if id == userID:
#     passwd = int(input('비밀번호를 입력해주세요: '))
#     if passwd == userPASSWD:
#         print("로그인 성공")
#     else:
#         print("비밀번호가 틀립니다.")
# else:
#     print("해당 아이디가 존재하지 않습니다.")
#     print("다시 입력하세요.")

# print("사용자가 성공할 때까지 입력받는 로그인 로직")
# userPasswd = 1111
# while True:
#     while True:
#         try:
#             passwd = input("비밀번호를 입력하세요: ")
#             passwd = int(passwd)
#             break
#         except ValueError:
#             print("숫자로만 입력하세요.")
    
#     if passwd == userPasswd:
#         print("패스워드가 일치합니다.")
#         break
#     else:
#         print("패스워드가 틀립니다.")
#         continue
    
# print("for문을 이용한 로그인 로직_기회 5번")
# userPasswd = 1111
# success = False
# for i in range(0,5):
#     # str로 친 것도 틀린 거로 인식
#     try:
#         passwd = input(f"비밀번호를 입력하세요({5-i}번 남았습니다.): ")
#         passwd = int(passwd)
#     except ValueError:
#         print("숫자로만 입력하세요.")
        
#     if passwd == userPasswd:
#         print("비밀번호가 일치합니다.")
#         success = True
#         break
#     else:
#         print("비밀번호가 틀립니다.")
# if success == False:
#     print("비밀번호를 5회 틀려서 로그인이 불가능합니다.(잠김)")

print("무한 루프 메뉴 구성")
while True:
    print("[메뉴를 입력하세요]")
    print('1.게임시작','2.랭킹보기','3.게입종료', end=' ')
    userChoose = int(input(' >>> '))
    if userChoose == 1:
        print("-> 게임을 시작합니다.")
        continue
    elif userChoose == 2:
        print("-> 실시간 랭킹")
        continue
    else:
        print("-> 게임을 종료합니다.")
        break
# # 무한 루프 메뉴 구성
# # [메뉴를 입력하세요]
# # 1.게임시작 2.랭킹보기 3.게입종료  >>> 1
# # -> 게임을 시작합니다.
# # [메뉴를 입력하세요]
# # 1.게임시작 2.랭킹보기 3.게입종료  >>> 1
# # -> 게임을 시작합니다.
# # [메뉴를 입력하세요]
# # 1.게임시작 2.랭킹보기 3.게입종료  >>> 2
# # -> 실시간 랭킹
# # [메뉴를 입력하세요]
# # 1.게임시작 2.랭킹보기 3.게입종료  >>> 3
# # -> 게임을 종료합니다.