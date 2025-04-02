orders = [
    {
        "country": "USA",
        "customers": [
            {
                "customer_id": "C001",
                "orders": [
                    {"product": "Laptop", "quantity": 1, "unit_price": 1200},
                    {"product": "Mouse", "quantity": 2, "unit_price": 25}
                ]
            },
            {
                "customer_id": "C002",
                "orders": [
                    {"product": "Smartphone", "quantity": 1, "unit_price": 800}
                ]
            }
        ]
    },
    {
        "country": "Canada",
        "customers": [
            {
                "customer_id": "C003",
                "orders": [
                    {"product": "Laptop", "quantity": 2, "unit_price": 1150},
                    {"product": "Keyboard", "quantity": 1, "unit_price": 100}
                ]
            }
        ]
    }
]


result = {
    "C001": {
        "country": "USA",
        "products": ["Laptop", "Mouse"],
        "total_amount": 1250  # (1 x 1200) + (2 x 25)
    },
    "C002": {
        "country": "USA",
        "products": ["Smartphone"],
        "total_amount": 800
    },
    "C003": {
        "country": "Canada",
        "products": ["Laptop", "Keyboard"],
        "total_amount": 2400  # (2 x 1150) + (1 x 100)
    }
}

def process_orders(orders):
    result = {}
    
    for country_data in orders:
        country = country_data["country"]
        
        for customer in country_data["customers"]:
            customer_id = customer["customer_id"]
            products = []
            total_amount = 0
            
            for order in customer["orders"]:
                products.append(order["product"])
                total_amount += order["quantity"] * order["unit_price"]
            
            result[customer_id] = {
                "country": country,
                "products": products,
                "total_amount": total_amount
            }
    
    return result

# 실행
result = process_orders(orders)
print(result)

import random
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
