import csv
import sys
# 1. csv 모듈과 sys 모듈을 추가

import os
# 4.file 직접 위치 삽입을 위해 os 모듈 삽입

# 5. os 모듈 테스트
# curdir = os.getcwd()
# print(curdir) - 정상 작동 - 이제 os 모듈의 다른 기능들을 알아보자



input_file = "./supplier_data1.csv"
output_file = "./output4.csv"

with open(input_file, 'r', newline='') as csv_in_file:
    print(csv_in_file)
# csv_in_file 테스트
''' 2. 파일 위치를 읽어오지 못하는 오류 발생 - 파이썬이 오퍼레이팅 시스템에 접근
파일과 관련된 내용을 볼 수 있도록 해야함 - os(operating stystem)모듈이 도와줄거임
'''
# 3. os module을 활용하는 법 공부 (https://www.youtube.com/watch?v=wgHeTJtth0w) 
