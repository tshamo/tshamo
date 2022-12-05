import os

os.chdir('/Users/taulant.shamo/songs')
'''
rename files - Sample
from e.g:   B - opera - #1.txt 
to e.g:     01-opera-B.txt
'''
print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)     # split the file from extension - provides a tuple
    f_title, f_course, f_num = f_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2) ## strip emty spaces, remove first character # and fill with 0 at the begining. 1 becomes 01

    #print(f'{f_num}-{f_course}-{f_title}{f_ext}')
    new_name = f'{f_num}-{f_course}-{f_title}{f_ext}'
    print(new_name)

    os.rename(f, new_name)

    #print(f)