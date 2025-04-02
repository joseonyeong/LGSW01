# print('성적처리')
#     # xlsx read module
#     # xlsx 전용 라이브러리리
# from openpyxl import load_workbook
# wb = load_workbook(filename='scores.xlsx')
# print(wb)
#     DataFrame으로 변환하는 함수
# import pandas as pd
# filename = 'D:\Programs\LGU_Codes\LGSW\scores.xlsx'
# df = pd.read_excel(filename)
# print(df)

# import pandas as pd
# df = pd.read_excel("D:\Programs\LGU_Codes\LGSW\scores.xlsx")
# print(df)
# df = df.T.to_dict()
# data = [v for k, v in df.items()]
# print(data)

# print('성적 자동 처리')
# with open('filename.txt', 'r', encoding='utf-8') as f:
#     f.readlines()
    
# with open('./LGU_Codes/LGSW/file_w.txt', 'w',encoding='utf-8') as f:    # 상대경로로 작성
#     f.write("ddd")

# with open('./LGU_Codes/LGSW/file_w.txt', 'a',encoding='utf-8') as f:    # a == append
#     f.write("ddd")

# with open("./LGU_Codes/LGSW/file_w.txt", "r", encoding='utf-8') as f:
#     lines = f.readlines()
#     print(lines, type(lines))
    
#     for line in lines:
#         print(line, end='') # 줄바꿈이 자동으로 두 번됨. end로 막기
        
# print('성적 자동처리_파일로')
# import os   
# import pandas as pd
# import ex_45

# input_file = os.listdir('./LGU_Codes/LGSW/') # 파일명 리스트형식으로
# arr = []
# for file in input_file: # 파일들 중 필요 파일만 가져옴
#     # print(file)
#     # print(type(file)) # str
    
#     # 학생들 txt 파일만 가져옴
#     # os.path.splitext는 튜플형식으로 ('파일이름','확장자')로 저장됨됨
#     # endswith함수 사용 (txt파일만 가져옴)
#     if file.endswith('.txt'):    # txt 파일만
#         # print(file)        
#             # with로 읽어옴
#         with open(f"./LGU_Codes/LGSW/{file}", 'r', encoding='utf-8') as f:
#             lines = f.readlines()
#             # print(lines)
#                 # 캐스팅 (str -> int)
#             for line in lines:
#                 line = int(line)
#                 arr.append(line)
#                 # print(line)
#         # print(arr)
#             # ex_45에 작성된 mean함수 사용
#             # ex_45에 작성된 std함수 사용   
#         print(f"{os.path.basename(file)}의 평균: {ex_45.mean(arr)}, 표준편차: {ex_45.standard_deviation(arr):.3f}")    
#         arr = []            
#             # print(lines) 

# # 성적 자동처리_파일로
# # jisoo.txt의 평균: 91.5, 표준편차: 2.693
# # mansoo.txt의 평균: 87.25, 표준편차: 9.038

