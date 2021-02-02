small=None
large=-1
while True:
    x = input("Enter value:")
    if x == 'done':
        break
    try:
        ix=int(x)
    except:
        print("Invalid")
        quit()
    if small is None:
        small =ix
    elif ix < small:
        small=ix
    else:
        pass
    if ix > large:
        large =ix
    else:
        pass

    



print(f"{small}  {large}")
