fname=input("Enter filename:")
try:
    fhandle=open(fname)
except:
    print("Error in opening file")
    quit()
for line in fhandle:
    line=line.upper()
    line=line.strip()
    print(line)