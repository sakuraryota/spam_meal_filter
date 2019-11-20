import sys

args= sys.argv[1]
first_line_num = int(sys.argv[2])
second_line_num = int(sys.argv[3])
mails_list = []


with open(args,"r") as file:
	for line in file:
		line = line.rstrip()
		mails_list.append(line)

if first_line_num > second_line_num: 
	print(mails_list[second_line_num-1:])
	print(mails_list[:first_line_num-1])

elif second_line_num >= first_line_num:
	print(mails_list[first_line_num-1:second_line_num])
	
	

