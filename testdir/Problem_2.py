import os
def find_files(suffix, path):
    if len(os.listdir(path)) == 0:
        #return if the length of the list is 0
        return []
    Allfiles=os.listdir(path)
    a=[i for i in Allfiles if suffix in i]
    Alldir=[i for i in Allfiles if '.' not in i]
    for dir in Alldir:
        a.extend(find_files(suffix,path=path+'/'+dir))
    return a
path=(os.getcwd())
print(find_files('.c',path))
# its expected output is list of t1.c,a.c,b.c,a.c: as all these files have suffix .c
print(find_files('.h',path))
#its expected out put is list of t1.h,a.h,b.h,a.h
print(find_files('.i',path))
# its output should be an empty list as there is no file with suffix .i in the given folder(directory)
print(find_files('',path))
# its output should be list of all files and directories in the given directory as all these files have a empty string as a suffix



# we have two a.c and two a.h files because these are in different directory