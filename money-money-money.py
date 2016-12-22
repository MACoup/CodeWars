from math import ceil, log

def calculate_years(principal, interest_rate, tax, desired):
    count = 0
    interest = 0
    while desired > principal:
        count += 1
        interest = principal * interest_rate
        t = interest * tax
        interest -= t
        principal += interest
    return count


'''other solutions'''



def calculate_years2(principal, interest, tax, desired):
    if principal >= desired: return 0

    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))


if __name__ == '__main__':
    print calculate_years(1000, 0.05, 0.18, 1100)
    print calculate_years(1000,0.01625,0.18,1200)
    print calculate_years(1000,0.05,0.18,1000)
