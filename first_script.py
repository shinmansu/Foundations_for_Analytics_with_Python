from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta

print("Output #1: I'm excited to learn Python")

# 두 수를 더한다
x = 4
y = 5
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))

# 두 리스트를 더한다
a = [1, 2, 3, 4]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a, b, c))

# 정수
x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
# 3의 4제곱이다. [제곱할 수]**[제곱할 횟수]
print("Output #6: {0}".format(int(8.3)/int(2.7)))

# 실수
# 실수를 float라고 한다. .f는 소수점 몇 자리까지 표현할지를 결정한다.
print("Output #7: {0:.3f}".format(200.3/2.7))
y = 2.5*4.8
print("Output #8: {0:.1f}".format(y))
r = 8 / float(3)
print("Output #9: {0:.2f}".format(r))
print("Output #10: {0:.4f}".format(8.0/3))

from math import exp, log, sqrt
# 메스 모듈값을 가져온다.

print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))

# 문자열(string)
print("Output #14: {0:s}".format('I\'m enjoying learning Python.'))

print("Output #15: {0:s}".format("This is a long string. without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller strings on separate lines so that the whole string is easy\
to view in teh text editor"))
# /를 이용하여 한 번에 긴 문장을 작성한다. 엔터키를 포함하지 않는다는 특성을 가진다(개행 x)
print("Output #16: {0:s}".format('''You can use triple single quotes for multi-line content strings.'''))
# '''나 """는 엔터키도 인식한다. 만약 엔터키를 포함해야만 한다면 '''나 """를 활용하자
print("Output #17: {0:s}".format("""You can also use triple double quotes for multi-line contetn strings."""))

# 함수 +,*,len
string1 = "This is a"
string2 = "short string"
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("she is","very "*4, "beautiful."))
# *을 단순히 반복되기 때문에 띄워쓰기를 신경써줘야 한다.
m = len(sentence)
# len은 띄워쓰기도 초함해서 글자수를 세는가? - 공백문자나 마침표를 포함해서 글자수를 센다.
print("Output #20: {0:d}".format(m))

# split - 문자열을 나눌 때 사용하는 함수
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ", 2)
# split("분할 기준", 분할 횟수) /분할 횟수 +1이 총 분할되는 갯수이다. 2개로 나누결우 3개로 분할된다. / ""혹은 ''으로 감싸도 상관없다
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}".format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2 = "Your,dliverabe,is,due,in,june"
string2_list = string2.split(",")
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1],string2_list[5],string2_list[-1]))
# list 에서 호출할 때 주의할 점은 0이 시작이고 -1이면 거꾸로 맨 마지막 함수를 가져온다는 점이다.
# 위 함수에서는 5가 6번재 함수를 지칭 june이며, -1또한 0에서 거꾸로 가기 때문에 june을 가리킨다.

print("Output #25: {0}".format(','.join(string2_list)))
# join 함수는 문자 리스트를 다시 합칠 수 있게 도와준다. ('기준'.join(변수))

# strip 개행,공백, 탭 문자를 각각 왼쪽 끝, 오른쪽 끝, 양쪽 끝에서 삭제할 수 있도록 도와주는 함수
# lstrip - 왼쪽 rstip - 오른쪽 strip 양쪽끝 strip()
string3 = " Remove Unwanted characters from this string.\t\t   \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: string3: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: string3: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: string3: {0:s}".format(string3_strip))

# 특정 문자를 원하지 않을 때 쓰는 strip 함수
# 변수.strip('원하지 않는 문자들') '' 혹은 "" 특이점은 한 번에 모아써도 된다는 것 ,를 안 넣는 이유는 아마도,도 처리해야 할 일이 생기기 때문인듯 함
string4 = "$$Here's another striong that has unwanted characters.__---++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted charactershave been removed.__---++"
string4_strip = string4.strip("$_-+")
print("Output #31: {0:s}".format(string4_strip))

# replace 하나의 문자 혹은 문자 집합을 다른 문자 혹은 다른 문자 집합으로 치환해주는 함수
# 변수.replace("변화의 대상인 문자","변화 후의 문자")
string5 = "Let's replace the spaces in this sentnece wiht ohter characters."
string5_replace = string5.replace(" ","!@!")
print("Output #32: (with!@!):{0:s}".format(string5_replace))
string5_replace2 = string5.replace(" ",", ")
print("Output #33: (with commas):{0:s}".format(string5_replace2))

# lower, upper, capitalize
# lower - 모든 문자 소문자 / upper - 모든 문자 대문자 / capiltalize - 첫 문자 대문자 나머지 소문자
# 변수.lower()
string6 = "Here's WHAT happens WHEN You Use lower"
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You use UPPER"
print("Output #35: {0:s}".format(string7.upper()))
string8 = "here's what happens WHEN you use Capiltalize"
print("Output #36: {0:s}".format(string8.capitalize()))
string5_list = string5.split()
print("Output #37 (on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))


# 문자열 내에 등장하는 패턴의 횟수를 세기
# re.complie(찾을 패턴,패턴 조건) / compil은 필수가 아니나 텍스티 기반의 패턴을 정규표현식으로 컴파일 하는 것을 의미
# re.complile로 정의내린 변수는 search, result 함수 등에서 사용가능하다.
# 100% 이해가 안가지만 패스 - 다시 공부!
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The",re.I)
# r은 raw의 r The의 원형임을 표현 re.I는 대소문자 구별없는 조건
count = 0
for word in string_list:
    if pattern.search(word):
    # search 문은
        count += 1
print("Output #38: {0:d}".format(count))

# 문자열 내에서 발견된 패턴 출력하기
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
# ?P<이름>찾을 패턴 - 찾을 패턴의 그룹 명을 지정하는 메타 문자
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))
        # group 함수가 사용된 예이며,search 뒤에 group이 붙으므로써 해당 패턴을 찾고 그 값을 출력할 수 있게 만든다.
        # 즉 search만 있다면 단순히 검색만 한 상태이며, group이 붙어야 해당 값이 출력될 수 있는 값이 된다.

# 문자열 내 "a"를 "the"로 대체하기
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"the"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)))
# 정규표현식.sub("변경 원하는 문자","변수")
# 정규표현식에 다라서 변수에서 값을 찾을 찾아 변경을 원하는 문자로 변경하는 함수

# 오늘 날짜와 년, 월, 일 요소들을 출력하기
today = date.today()
print("Output #41: today:{0}".format(today))
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))

# date는 년,월,일,날짜만 , date time은 date + 시간을 갖는다.
# 0 뒤에 있는 !s 는 0으로 나오는 내용이 숫자요도 문자로 처리하라는 의미이다.

# timedelta 함수를 이용여 새로운 날짜 계산하기
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

# 두 날짜 사이의 날짜 차이를 계산하기
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))
# str은  결과를 하나의 문자열로 만든다. 문자열로 만든 것을 split하고 그 첫번 재 열을 출력하라는 코드다.

# date 객체를 특정 형식의 문자열으로 만들기
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))

# 날짜 문자열로부터 특정 형식의 datetime 객체를 생성하기
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
# 변수.strftime('출력을 원하는 표현방식')
# strftime은 시간과 관련된 표현방식을 결정하는 함수
# %m = 숫자 달(1,2) %d= 날짜 %Y=풀 년도(2017) %b = 달의 영어 약자(Jan Feb) %B= 달의 영어 풀네임(January  February)

# 다른 date 형식을 지닌 4가지 문자열에 기반한
# 각각 2종류의 datetime 객체들과 date 객체들
print("Output #54: {!s})".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s})".format(datetime.strptime(date2, '%b %d, %Y')))
# (time.strptime(date_string, format)). / 시간 뒤에 포멧을 붙여줌으로써 다시 문장열로 된 시간을 날짜 형식으로 변경
# 날짜 부분만 출력하기
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))
# datetime.date(날짜 값)  날짜 값에서 날짜만 추출

# 리스트 만들기
# 리스트를 만들기 위해 대괄호를 사용한다.
# len() 함수를 통해 리스트 내 원소의 수를 센다.
# max() 함수와 min() 함수는 최대/최소값을 찾는다.
# count() 함수는 리스트 내의 특정 값이 등장한 횟수
a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))
# count만 사용법이 좀 다름 변수.count(찾기를 원하는 값) - 해당 변수에서 해당 값이 나온 횟수

# 리스트내 특정 원소에 접근하려면 인덱스 이용하기
# [0]은 첫뻔재 원소이다. [-1]은 마지막 원소이다.
print("Output #65: {}".format(a_list[0]))
print("Output #66: {}".format(a_list[1]))
print("Output #67: {}".format(a_list[2]))
print("Output #68: {}".format(a_list[-1]))
print("Output #69: {}".format(a_list[-2]))
print("Output #70: {}".format(a_list[-3]))
print("Output #71: {}".format(another_list[2]))
print("Output #72: {}".format(another_list[-1]))

# 리스트 분할하기 
# 리스트 분할을 사용하여 리스트 원소들의 부분집합 만들기 
# 맨 앞부터 분할하는 경우, 최초 인덱스를 생략한다. 
# 맨 뒤까지 리스트를 분할하는 경우, 마지막 인덱스를 생략한다. 
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))


# [:]를 이용하여 리스트를 복사하기 
a_new_list = a_list[:]
print("Output #77: {}".format(a_list[:]))

# + 연산자를 이용하여  2개 이상의 리스트를 병합하기 
a_longer_list = a_list + another_list
print("Output #78: {}".format(a_longer_list))

# in과 not in을 이용하여 특정 원소의 리스트 내 포함 여부를 확인하기 
a = 2 in a_list
print("Output #79: {}".format(a))

if 2 in a_list:
  print("Output #80: 2 is in {}".format(a_list))


b = 6 not in a_list
if 6 not in a_list:
  print("Output #81: 6 is not in{}".format(a_list))
  

# append() 함수를 이용하여 리스트이 마지막에 원소를 추가하기
# remove() 함수를 이용하여 리스트 내 특정 원소를 제거하기
# pop() 함수를 이용하여 리스트의 마지막 원소를 제거하기 

a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85: {}".format(a_list))

# append(추가할 값) / remove(제거할 값) /  pop() - 뒤에서부터 순차적으로 제거

# reverse()함수를 이용하여 리스트 반전하기
# 해당 리스트 내에서(인플레이서) 변경이 일어나므로
# 기존 리스트를 변경하지 않고 반전하려면 먼저 사본을 만들어둬야 한다. 
a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))

