import csv
import glob
import os
import sys

input_path = sys.argv[1]

file_counter = 0
# 3. print(os.path.join(input_path,'sales_*'))
# 해당 함수는 디렉토리 + sales_*까지는 갖고 오고 있음
# sales 파일 명 오타 있어서 파일명 수정
# 2. print(glob.glob(os.path.join(input_path,'sales_*')))
#  해당 함수는 원래 파일 리스트 3가지를 변수로 담아야 하는데 그러지 못하고 있음
for input_file in glob.glob(os.path.join(input_path,'sales_*')):

    # 1.for in 뒤에 디렉토리가 붙는다면 변수는 파일이 된다.
    row_counter = 1
    with open(input_file, 'r', newline= '') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            row_counter += 1
            # row_counter는 +=을 해줘야 1이 더 더해짐
    print('{0!s}: \t{1:d} rows \t{2:d} colusms'.format(os.path.basename(input_file), row_counter, len(header)))
    file_counter += 1
print('Number of files: {0:d}'.format(file_counter))
