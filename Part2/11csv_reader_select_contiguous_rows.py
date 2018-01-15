import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow([value.strip() for value in row])
            row_counter += 1
        # 여기서  왜 row counter를 세는지 궁금할 수 있음
        # 그것은 행의 수를 세는 것이기 때문임 특정 값을 사용한다면 for문내에서
        # 하겠지만 특정 row를 선택하기에는 row_counter 같이 변수를 하나 넣어줌
        
