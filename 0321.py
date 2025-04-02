# L = [4,5,6]
# for i in range(len(L)):
#     print(i)
# print()
# for i in L:
#     print(i)

# print('이차원 배열 평균 구하기')
# def func(x):
#     sum = 0
#     for j in range(len(x)):
#         for i in range(len(x[j])):
#             sum += x[j][i]
#         mean = sum / len(x[j])
#         print(f"{mean:.3f}")
#         sum = 0
#     return mean

# def Cfunc(x):
#     return [ for i in x]

# x = [[78, 80, 95, 55, 67, 43], [45, 67, 90, 87, 88, 93]]
# func(x)
# Cfunc(x)

# products = [
#     {
#         "category": "Electronics",
#         "items": [
#             {"name": "Laptop", "price": 1200, "stock": 5},
#             {"name": "Smartphone", "price": 800, "stock": 10}
#         ]
#     },
#     {
#         "category": "Home Appliances",
#         "items": [
#             {"name": "Vacuum Cleaner", "price": 150, "stock": 7},
#             {"name": "Air Conditioner", "price": 500, "stock": 3}
#         ]
#     }
# ]

# result = {
#     "Laptop": {"price": 1200, "stock": 5},
#     "Smartphone": {"price": 800, "stock": 10},
#     "Vacuum Cleaner": {"price": 150, "stock": 7},
#     "Air Conditioner": {"price": 500, "stock": 3}
# }

# def convert_data(products):
#     n = 0
#     addDict = {}
#     addValue = []
#     resultDic = {}
#     for i in products:
#             # 1번째 인덱스부터 가져와야함
#             # 딕셔너리 1번째 value값만 가져옴
#         for value in i.values():
#             arr = value
#             # 딕셔너리 값 추가
#         for n in range(len(arr)):
#             item = arr[n]
#             print(item)
#                 #0    # {'Laptop': {'price': 1200, 'stock': 5},
#                 #1    # 'Smartphone': {'price': 800, 'stock': 10},
#                 #2    # 'Vacuum Cleaner': {'price': 150, 'stock': 7},
#                 #3    # 'Air Conditioner': {'price': 500, 'stock': 3}}
#             for j in range(len(arr[n])):
#                 resultDic[item['name']] = {'price':item['price'], 'stock':item['stock']}
#     print(resultDic)
# convert_data(products)

# orders = [
#     {
#         "country": "USA",
#         "customers": [
#             {
#                 "customer_id": "C001",
#                 "orders": [
#                     {"product": "Laptop", "quantity": 1, "unit_price": 1200},
#                     {"product": "Mouse", "quantity": 2, "unit_price": 25}
#                 ]
#             },
#             {
#                 "customer_id": "C002",
#                 "orders": [
#                     {"product": "Smartphone", "quantity": 1, "unit_price": 800}
#                 ]
#             }
#         ]
#     },
#     {
#         "country": "Canada",
#         "customers": [
#             {
#                 "customer_id": "C003",
#                 "orders": [
#                     {"product": "Laptop", "quantity": 2, "unit_price": 1150},
#                     {"product": "Keyboard", "quantity": 1, "unit_price": 100}
#                 ]
#             }
#         ]
#     }
# ]


# result = {
#     "C001": {
#         "country": "USA",
#         "products": ["Laptop", "Mouse"],
#         "total_amount": 1250  # (1 x 1200) + (2 x 25)
#     },
#     "C002": {
#         "country": "USA",
#         "products": ["Smartphone"],
#         "total_amount": 800
#     },
#     "C003": {
#         "country": "Canada",
#         "products": ["Laptop", "Keyboard"],
#         "total_amount": 2400  # (2 x 1150) + (1 x 100)
#     }
# }

# def process_orders(orders):
#     result = {}
    
#     for country_data in orders:
#         country = country_data["country"]
        
#         for customer in country_data["customers"]:
#             customer_id = customer["customer_id"]
#             products = []
#             total_amount = 0
            
#             for order in customer["orders"]:
#                 products.append(order["product"])
#                 total_amount += order["quantity"] * order["unit_price"]
            
#             result[customer_id] = {
#                 "country": country,
#                 "products": products,
#                 "total_amount": total_amount
#             }
    
#     return result

# # 실행
# result = process_orders(orders)
# print(result)

# print("표준편차 구하기")
# import math
# import numpy as np
# def std(x):
#     std = []
#     result = {}
#     for i in x:
#         name = i['name']
#         arr = [i['math'], i['eng'], i['sci']]    
#         result[name] = np.std(arr)
#     return result
# data = [
#     {'name':'철수', 'math':85, 'eng':90, 'sci':75},
#     {'name':'준호', 'math':73, 'eng':85, 'sci':93},
#     {'name':'영희', 'math':92, 'eng':88, 'sci':90}
# ]
# print(std(data))

# print('로또 번호 추출기')
import random
# def rdDef():
#         # 6번 반복
#     for _ in range(6):
#             # 랜덤 숫자 뽑기
#         print(random.randrange(1,46))
#     return True

def no_reduplication():
    arr = [] 
    for _ in range(6):  # 6개의 숫자를 뽑음
        n = random.randrange(1, 46)
        while n in arr:  # 중복이면 다시 뽑음
            n = random.randrange(1, 46)
        arr.append(n)  # 중복이 아니면 추가
    return arr

def no_reduplication():
    arr = []  # 초기 배열 비워둠
    while len(arr) < 6:  # 6개의 숫자가 찰 때까지 반복
        n = random.randrange(1, 46)
        if n not in arr:  # 중복 체크
            arr.append(n)  # 중복이 아니면 추가
    return arr

print(no_reduplication())
   
# def game(n):
#     for _ in range(n):
#         print('겜 만들래')
#     return True

# rdDef()
# game(int(input('n: ')))
