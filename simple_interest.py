def simple_interest(p, r, t):
    return (p * r * t) / 100

principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

si = simple_interest(principal, rate, time)
print("Simple Interest =", si)
