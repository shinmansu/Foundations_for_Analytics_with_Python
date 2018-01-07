string1 = "my deliverable is due in may"
string1_list2 = string1.split(" ", 2)
print("FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2 = "your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("{0},{1},{2}".format(string2_list[1],string2_list[5],string2_list[-1]))

print("{0}".format(' '.join(string2_list)))
