string2 = "Your,dliverabe,is,due,in,june"
string2_list = string2.split(",")
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1],string2_list[5],string2_list[-1]))
# list 에서 호출할 때 주의할 점은 0이 시작이고 -1이면 거꾸로 맨 마지막 함수를 가져온다는 점이다.
# 위 함수에서는 5가 6번재 함수를 지칭 june이며, -1또한 0에서 거꾸로 가기 때문에 june을 가리킨다.

print("Output #25: {0}".format(','.join(string2_list)))
