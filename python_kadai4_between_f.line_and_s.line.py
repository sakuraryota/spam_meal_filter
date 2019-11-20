#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
args= sys.argv[1]
first_line_num = int(sys.argv[2])
second_line_num = int(sys.argv[3])
mails_list = []


with open(args,"r") as file:
	for line in file:
		line = line.rstrip()
		mails_list.append(line)
if second_line_num > first_line_num: 
	print(mails_list[first_line_num-1:second_line_num])
else:
	print('erorr')

