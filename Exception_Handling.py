#file hanflind 
#file = oopen('requirements.txt', 'r')
#print(file.read())
#file.close()
# ====================== write operation ========================== #
#file = open('example.txt', 'w')
#file.write('python class')
#file.close
# ====================== append operation ========================== #
#with open('example.txt', 'a') as file:
#    file.write(' to work with keywords')
# read a csv file using file handling concept

#file = open('breast-cancer.csv', 'r')
#print(file.read())
#file.close()

# ====================== excpeption handling ========================== #
# try, except, finally
try:
    a = 5 / 0
    print(a)
except Exception as e:
    print("hey, you cant divide a number by zero", e)
finally:
    print("this block will always execute")
