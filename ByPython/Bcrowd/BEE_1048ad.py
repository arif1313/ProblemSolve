salary= float(input());

sarary_range=[0,400.00,800.00,1200.00,2000.00];
rate=[0.15, 0.12, 0.10, 0.07, 0.04];
for item in range(4, -1,-1):
   
    if salary>sarary_range[item]:
        myRate=rate[item] 
        break;
total_salary=salary+(myRate*salary);
print(round(salary, 2));
print(round(myRate*salary, 2))
print(round(myRate*100, 0))

print("hello world")


