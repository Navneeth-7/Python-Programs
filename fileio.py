print('this is my first file IO')
myfile=open('C:\\Users\\Navneeth\\PycharmProjects\\untitled1\\myfile.txt')
myfile.seek(0)
a=myfile.read()
print(a)
myfile.close()

