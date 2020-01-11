
FILE_LOCATION = 'D:\Study\Python\FileHandling'
try:

    file = open(fr"{FILE_LOCATION}\test.txt", 'r')
    line = file.readline()
    print (line)
except (FileNotFoundError, FileExistsError) as err:
    print("Some Error occured")
    raise err
finally:
    file.close()
