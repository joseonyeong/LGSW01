# print("BMI 계산기_등급출력_숫자만 입력받을 수 있게")
# while True:
#     try:
#         weight = float(input("몸무게 입력: "))
#         break
#     except ValueError:
#         print("숫자로만 입력하세요.")

# while True:
#     try:
#         height = float(input("키 입력: "))
#         break
#     except ValueError:
#         print("숫자로만 입력하세요.")

# bmi = weight / height**2
# print(f'BMI: {bmi:.3f}')

# if bmi < 18.5:
#     print("저체중입니다.")
# elif bmi < 23:
#     print("정상입니다.")
# elif bmi < 25:
#     print("과체중입니다.")
# else:
#     print("비만입니다.")

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
# # 반복 번수 출력_끝내기 물어보기
# # 숫자를 입력하세요: 2
# # 2
# # 1
# # while문을 2번 반복했습니다.
# # 끝내시겠습니까? (Y/N): 2
# # Y 또는 N으로 입력하세요.
# # 끝내시겠습니까? (Y/N): ㅡ
# # Y 또는 N으로 입력하세요.
# # 끝내시겠습니까? (Y/N): y
# # while문을 1번 반복했습니다.

# print("반쪽 별")
# for i in range(1,6):
#     print('*'*i)
# # *
# # **
# # ***
# # ****
# # *****