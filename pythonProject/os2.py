import os
from datetime import datetime
#print(os.getcwd()) # get working dir

#print(dir(os))     # show all funcrions

os.chdir('/Users/taulant.shamo/ANDY-TEST/')   # change dir

# CREATE DIR
#os.mkdir('ANDY-TEST')
#os.mkdir('ANDY-TEST/1')
#os.mkdir('ANDY-TEST/2')
#os.makedirs('ANDY-TEST/2/3/4/5')  # level deep if they don't exists

#REMOVE DIR
#os.rmdir('ANDY-TEST/2/3/4')
#os.removedirs('ANDY-TEST/2')

#details about a file
print(os.stat('file1.txt'))
print('Size:',os.stat('file1.txt').st_size) # print file size
print(os.stat('file1.txt').st_mtime) # print last modification time UNIX FORMAT
mod_time = os.stat('file1.txt').st_mtime
print(datetime.fromtimestamp(mod_time)) # print last modification time readable format

#list files & dirs on a dir
print(os.listdir('/Users/taulant.shamo/ANDY-TEST/'))

#print(os.getcwd())