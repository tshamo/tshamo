import os

#os.chdir('/Users/taulant.shamo')

#print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'text.txt')

print(file_path)

print(os.path.basename('/tmp/test.txt'))    # filename only
print(os.path.dirname('/tmp/test.txt'))     # dir of file
print(os.path.split('/tmp/test.txt'))       # both: dir & file
print(os.path.exists('/tmp/test.txt'))      # Check if a path exists
print(os.path.isdir('/tmp'))                # Check if that is a dir
print(os.path.isfile('/tmp'))               # Check if that is a file
print(os.path.splitext('/tmp/test.txt'))    # .extension and filename
print(dir(os.path))

