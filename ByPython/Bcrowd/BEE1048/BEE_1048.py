salary=float(input());

def salarycal(salary):
    rate=0;
    if salary>2000:
        rate=0.04
    elif salary>1200 and salary<=2000:
        rate=0.07
    elif salary<=1200 and salary>800:
        rate=0.10
    elif salary<=800 and salary>400:
        rate=0.12
    elif salary>0 and salary<=400:
        rate=0.15
    return rate;
my_rate=salarycal(salary);

total_salary=salary+(my_rate*salary);
print(f"Novo salario: {total_salary:.2f}");
print(f"Reajuste ganho: {my_rate*salary:.2f}");
print(f"Em percentual: {my_rate*100:.0f} %") ; 


# # Read the employee's salary
# salary = float(input())

# # Define the salary ranges and corresponding readjustment rates
# ranges = [0, 400.00, 800.00, 1200.00, 2000.00]
# rates = [0.15, 0.12, 0.10, 0.07, 0.04]

# # Find the appropriate range and corresponding rate
# for i in range(4, -1, -1):
#     if salary > ranges[i]:
#         rate = rates[i]
#         break

# # Calculate new salary, money earned, and percentage increase
# new_salary = salary * (1 + rate)
# money_earned = new_salary - salary
# percentage_increase = rate * 100

# # Print the results with 2 decimal places
# print(f"Novo salario: {new_salary:.2f}")
# print(f"Reajuste ganho: {money_earned:.2f}")
# print(f"Em percentual: {percentage_increase:.0f} %")



