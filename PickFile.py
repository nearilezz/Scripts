#!/usr/bin/python

# Name: PickFile.py
# auther: Zhao Zhilong
# descripte: Read src file, pick the line which contains the DecKey and don't contains ShieldKey.
# date: 11/22, 2014, Sat

import os


DecKeyList = []
ShieldKeyList = []

SrcFileName = raw_input("Src file name:")
DecFileName = raw_input("Dec file name:")
if len(DecFileName) == 0 or len(SrcFileName) == 0:
	print 'File name is empty.[fail]'
	exit()
	

while True:
    temp = raw_input("Input Dec Key:")
    if len(temp) == 0:
        break
    DecKeyList.append(temp)

while True:
	temp = raw_input("Input Shield Key:")
	if len(temp) == 0:
		break
	ShieldKeyList.append(temp)

SrcFile = open(SrcFileName, 'r')
DecFile = open(DecFileName, 'w')

while True:
	line = SrcFile.readline()

	if len(line) == 0:
		break

	for DecStr in DecKeyList:
		if DecStr in line:
			flag = True
			for ShiStr in ShieldKeyList:
			    if ShiStr in line:
			    	flag = False
			    	break
			if flag == True:
				DecFile.write(line)

SrcFile.close()
DecFile.close()

print 'Pick Complete.[Success]'
print DecFileName,'\t', os.path.getsize(DecFileName), 'Bytes'

