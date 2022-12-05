# File objects

# USE THIS MODE
with open('test.txt', 'r') as f:
    for line in f:                  ## Efficent way to read a large file and load in memory line by line, not all at once
        print(line, end='')
    #f_contents = f.read()           ## reads entire file. All at once. That is an issue with very large files
    #f_contents = f.readlines()
    #f_contents = f.readline()       ## read only first line
    #print(f_contents, end='')       ## end removed the new line that is by default
    #f_contents = f.readline()       ## read only first line
    #print(f_contents, end='')


#print(f.closed)       # checking if the file is closed


