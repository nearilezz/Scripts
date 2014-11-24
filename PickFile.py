#!/usr/bin/python

# Name: PickFile.py
# auther: Zhao Zhilong
# descripte: Read src file, pick the line which contains the DecKey and don't contains ShieldKey.
# date: 11/22, 2014, Sat

import os

def AutoDecName(srcFileName):
    nameTuple = os.path.splitext(srcFileName)
    baseName = nameTuple[0]
    expandedName = nameTuple[1]
    decFileName = baseName + '(Pick)' + expandedName
    return decFileName

newLines = '\r\n'
DecKeyList = []
ShieldKeyList = []


SrcFileName = raw_input('Src File name: ')
DecFileName = raw_input('Dec File name: ')

if len(DecFileName) == 0:
    DecFileName = AutoDecName(SrcFileName)

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

DecFile.write('Keywords:' + newLines)
DecFile.write('\tin: ' + str(DecKeyList) + newLines)
DecFile.write('\tnot in: ' + str(ShieldKeyList) + newLines)
SrcFile.close()
DecFile.close()

print 'Pick Complete.[Success]'
print DecFileName,'\t', os.path.getsize(DecFileName), 'Bytes'

