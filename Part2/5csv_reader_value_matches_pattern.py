import csv
import re
import sys
# 1. csv 모듈과 sys 모듈을 추가

# import os
# 4.file 직접 위치 삽입을 위해 os 모듈 삽입

# help(os)
# 5. os 모듈 테스트
# curdir = os.getcwd()
# print(curdir) - 정상 작동 - 이제 os 모듈의 다른 기능들을 알아보자

input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number = row_list[1]
            # print(a_date) - a_date의 값은 정상적으로 수신중
            # 현재 if 코드 밑에 부분이 작동을 하지 않는다.
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)
                # 날짜를 못 받아 온 이유는 내가 위 쪽의 날짜 부분을 잘못 입력해서다.
                # 로우 데이터를 그대로 받아오는 거기 때문에 if문에 에러가 없다면
                # 데이터를 다시 한 번 확인해보자

# csv_in_file 테스트
''' 2. 파일 위치를 읽어오지 못하는 오류 발생 - 파이썬이 오퍼레이팅 시스템에 접근
파일과 관련된 내용을 볼 수 있도록 해야함 - os(operating stystem)모듈이 도와줄거임
'''
# 3. os module을 활용하는 법 공부 (https://www.youtube.com/watch?v=wgHeTJtth0w)
