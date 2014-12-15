import md5
import os

from time import clock as now
def getmd5(filename):
    file_txt = open(filename, 'rb').read()
    m = md5.new(file_txt)
    return m.hexdigest()

def main():
    path = raw_input("Path: ")
    all_size = {}
    total_file = 0
    total_delete = 0
    start = now()

    for file in os.listdir(path):
        total_file += 1;
        real_path = os.path.join(path, file)
        if os.path.isfile(real_path) == True:
            filesize = os.stat(real_path).st_size
            name_md5 = [real_path, '']
            if filesize in all_size.keys():
                new_md5 = getmd5(real_path)
                if all_size[filesize][1] == '':
                    all_size[filesize][1] = getmd5(all_size[filesize][0])
                if new_md5 in all_size[filesize]:
                    total_delete += 1
                    os.remove(real_path)
                    print 'Delete ', file
                else:
                    all_size[filesize].append(new_md5)
            else:
                all_size[filesize] = name_md5
    end = now()
    time_last = end - start

    print 'File total: ', total_file
    print 'Del  total: ', total_delete
    print 'Time consuming: ', time_last, 's'

if __name__ == '__main__':
    main()

