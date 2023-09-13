P=int(input("Enter the principal amount"))
R=int(input("Enter the rate of interest "))
N=int(input("Enter the loan of year"))
CI=P*(1+R/N)**N
print("Compound interest=",CI,"Principal amount=",P)