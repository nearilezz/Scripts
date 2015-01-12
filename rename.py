import os

for file in os.listdir('./'):
    #print os.path.basename(file)
    dirtuple = os.path.splitext(file)
    #print dirtuple
    if '.tm3' in dirtuple[1]:
        #print dirtuple
        basename = dirtuple[0]
        expandname = '.mp3'
        newname = basename + expandname
        os.rename(file, newname)
        print file,'->',newname



