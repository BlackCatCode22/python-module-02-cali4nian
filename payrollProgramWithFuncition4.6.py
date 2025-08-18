# Daniel Soriano - Payroll Program with Function code along
def computepay(hours, rate):
    # print('In computepay', hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate + (rate * .5))  # fixed code from video
        pay = reg + otp
    else:
        pay = hours * rate
    # print("Returning", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
xp = computepay(fh, fr)
print("Pay:", xp)