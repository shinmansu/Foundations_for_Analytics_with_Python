import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

# for 문의 중복 for문이 어떻게 순환하는지 이해해야 한다.
first_file = True
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline= '') as csv_in_file:
        with open(output_file, 'a', newline= '') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader)
                #next(리스트) 해당 리스트의 첫번째 값을 변수에 넣고, 해당 리스트의
                # 첫 번째 열을 삭제하고 다시 해당 파일을 저장한다.
                # 이해가 안간다면 아래 2열을 실행해 보자
                # print(header)
                # header2 = next(filereader)
                # print(header2)
                for row in filereader:
                    filewriter.writerow(row)
