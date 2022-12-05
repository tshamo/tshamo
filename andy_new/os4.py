import os

print(os.getcwd()) # get working dir

os.chdir('/Users/taulant.shamo/ANDY-TEST')

print(os.getcwd())

for dirpath, dirnames, filenames in os.walk('/Users/taulant.shamo/ANDY-TEST'):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
