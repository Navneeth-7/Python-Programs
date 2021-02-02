# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"): 
       count= count+1
       line=float(line[21:])
       total=line+total



print(total/count)
