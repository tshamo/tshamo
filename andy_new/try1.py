


try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception                 ## generic exception you ca raise yourself
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error!")
else:                           ## Runs only if sucessful
    print(f.read())
    f.close()

finally:                        ## Run regardless of status
    print("Executing Finally ...")


