import main_test

print("Top level in 2.py")

main_test.myfunc()

if __name__ == '__main__':
    print("2.py is directly")
else:
    print("2.py is run indirectly")
