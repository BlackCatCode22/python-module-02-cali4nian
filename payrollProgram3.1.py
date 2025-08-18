# Daniel Soriano - Payroll Program Code Along

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40:
    print("Overtime")
    reg = fr * fh
    otp = (fh-40.0) * (fr + (fr * .5)) # fixed code from video
    print(reg, otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr
print("Pay:", xp)