def square(num):
    return num*num
g=11
def even(num):
    g=9
    return num%2 ==0
a=[1,2,3,4,5,6]
''''
print(list(map(square,a)))
'''
#print(list(filter(even,a)))
#for x in map(square,a):
 #   print(x)
#print(g)
#print(list(map(lambda num:num**2,a)))
#print(list(filter(lambda num:num%2==0,a)))

#q=[2,2,4,53,3,6,32,3,2,2]
#print(set(q))


def ispangram(st):
    print((st.lower()))
    print(set(st.lower()))
    print(''.join(set(st.lower())))
     #print(set(string.lower()))
    #print("".join(set(string.lower())))
    return "".join(set(st.lower())) == st.lower()

print(ispangram("asqwecvb"))