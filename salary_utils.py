def gross_salary(basic):
    return basic + basic * 0.20 + basic * 0.10

def deductions(gross):
    return gross * 0.05

def net_salary(gross, deduction):
    return gross - deduction\n