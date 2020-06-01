def computepay(i_hrs,i_rphr):
    if i_hrs <= 40 :
        gross_pay = i_hrs * i_rphr
    
    if i_hrs > 40 :
        gross_pay = 40 * i_rphr + (i_hrs - 40) * (1.5 * i_rphr)
    
    return gross_pay

s_hrs = input("Enter Hours:")
s_rphr = input("Enter Rate Per Hour:")

i_hrs = float(s_hrs)
i_rphr = float(s_rphr)

p = computepay(i_hrs,i_rphr)
print("Pay",p) 