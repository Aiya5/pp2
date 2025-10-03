employees = {
    "Aia": 5000,
    "Aiya": 6000,
    "Aliya": 5500
}

for name, salary in employees.items():
     if salary>5500:
      employees[name] = salary + (salary * 0.1)

print(employees)
