# from collections import defaultdict
# dd = defaultdict(int)
# print(dd)
#     # defaultdict(<class 'int'>, {})
# ddd = defaultdict(list)
# ddd['a'].append('a')
# print(ddd)
#     # defaultdict(<class 'list'>, {'a': ['a']})

# class Person:
#     def __init__(self,n,h,w):
#         self.name = n
#         self.height = h
#         self.weight = w
# p1 = Person('Tom',170,100)
# print(type(p1))  # <class '__main__.Person'>

# class BankAccount:
#     def __init__(self, owner, passwd, balance=0):
#         self.owner = owner
#         self.passwd = passwd
#         self.balance = balance
#         print(f"{owner}의 잔액 {balance}원 비밀번호 {passwd}")
    
#     def login(self, name, passwd):
#         print(name, passwd)      
    
#     def deposit(self, amount):
#         if amount>0:
#             self.balance += amount
#             print(f"{amount}원 입금")
#         else:
#             print("0보다 큰 금액을 입금해주세요.")
    
#     def get_balance(self):
#         print(f"현재 잔액 {self.balance}")
    
#     def withdraw(self, amount, inputPasswd):
#         if self.balance > 0:
#             self.balance -= amount
#             print(f"{amount} 출금")
#             print(f"현재 잔액 {self.balance}")
#         else:
#             print("잔액 부족") 
    
#     def remittance(self, amount, account):
#         self.withdraw(amount)
#         self.deposit(amount)
#         pass 
            
# account1 = BankAccount("길동", '1234', 10000)
# account2 = BankAccount("0길동", '1234', 10000)
# account1.deposit(5000)
# account1.get_balance()
# account1.withdraw(5000)
# account2.remittance(50000, account1)
# account1.get_balance()

# import random
# class Linear:
#     def __init__(self, in_feauture, out_feauture):
#         self.weight = []    # in_feauture행 out_feauture열
#         arr = []
#         for i in range(in_feauture):
#             for j in range(out_feauture):
#                 arr.append(random.randint(1,10))
#             self.weight.append(arr)    
#         self.bias = []  #out_feature개
#         for i in range(out_feauture):
#             self.bias.append(random.randint(1,10))
        
#     def matmul(self, A, B):
#         # 행렬 곱 A,B
#         # 결과인 C 반환
#         c = []
#         for i in range(len(A)):
#             row = []
#             # for j in range(len(B[i])):
#             #     sum = 0
#             #     for n in range(len(A[0])):
#             #         sum += A[i][n] * B[n][j]
#             #     row.append(sum)
#             sum = 0
#             for j in range(len(B[i])):
#                 sum += A[i][j] * B[j][i]
#                 row.append(sum)
#             c.append(row)
#         return c
        
#     def forward(self, x):
#         # x 행렬 곱 self.weight + self.bias
#         # [1+10 2+10 3+10]
#         # [1+10 2+10 3+10]
#         # [1+10 2+10 3+10]
#         c = linear.matmul(x, self.weight)
#         # c + self.bias
#         sum = 0
#         arr = []
#         finArr = []
#         for i in range(len(c)):
#             for j in range(len(self.bias)):
#                 sum = c[i][j] + self.bias[i]
#                 arr.append(sum)
#             finArr.append(arr)
#         return finArr 
    
# linear = Linear(3,2)
# x = [[1,2,3], [4,5,6]]
# print(linear.forward(x))    # (2,2)

# import ex_45
# s = input('평균을 구할 숫자 입력: ')
# L = [int(i) for i in  s.replace(',', ' ').split()]
# print(L)
# print(ex_45.mean(L))

