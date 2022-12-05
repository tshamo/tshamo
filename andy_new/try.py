


try:
    f = open('test_file.txt')
#    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:                           ## Runs only if sucessful
    print(f.read())
    f.close()

finally:                        ## Run regardless of status
    print("Executing Finally ...")


