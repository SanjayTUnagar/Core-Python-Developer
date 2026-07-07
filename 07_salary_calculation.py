#Salary Calculation Program

'''
Basic Salary = 50000
TDS = 50000 × 5% = 2500
After TDS = 50000 − 2500 = 47500
Gross Salary = 47500 − 200 = 47300
Pf Tax = 47300 * 5 / 100 = 2365 
Net Salary = 47300 - 2365 = 44935
'''
Basic_Salary = int(input("Enter Your Basic Salary: ")) 
Tds_Percent = float(input("Enter TDS (5%): "))

Tds_Amount = Basic_Salary * Tds_Percent / 100
Salary_After_Tds = Basic_Salary - Tds_Amount

Professional_Tax = int(input("Enter Professional Tax: "))
Gross_Salary = Salary_After_Tds - Professional_Tax

print("You Gross Salary is: ", Gross_Salary)  #Final Salary : 47300

Pf_Tax = int(input("Enter PF Tax (5%): "))  # PF Tex = 5%
Pf_Amount = Gross_Salary * Pf_Tax / 100     #47300 * 5 / 100 =  2365

Net_Salary = Gross_Salary - Pf_Amount   # 47300 - 2365 = 44935 
print("Your Net Salary After PF Tax is:", Net_Salary)


