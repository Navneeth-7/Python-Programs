def computepay(fh, fr):
    if fh > 40:
        reg = fh * fr
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg + otp
        return xp
    else:
        xp = fh * fr
        return xp


#print(f"Output is :{xp}")

try:
    fh= float(input("Enter Hours:"))
    fr= float(input("Enter rate:"))
except:
    print("Invalid floating number")
    quit()
d=computepay(fh, fr)
print(d)
