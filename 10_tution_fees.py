
# Tution Fees taking input from user 

'''Total_Fees = int(input ("Enter your tution fees: "))
Diposit = float(input ("Enter deposite (%): "))

After_Diposit = Total_Fees * Diposit / 100
print("After Deposite fees:",After_Diposit)

Remaining_fees = Total_Fees - After_Diposit
print("Remaining fees:",Remaining_fees)

installment_1 = int(input("Enter your first installment: "))
After_first_installment = Remaining_fees - installment_1;
print("After first installment fees:",After_first_installment)

installment_2 = int(input("Enter your second installment: "))
After_second_installment = Remaining_fees - installment_2;
print("After second installment fees:",After_second_installment)

installment_3 = int(input("Enter your third installment: "))
After_third_installment = Remaining_fees - installment_3;
print("Total fees paid:",After_third_installment)'''

Total_Fees = int(input ("Enter your tution fees: "))
Diposit = float(input ("Enter deposite (%): "))

After_Diposit = Total_Fees * Diposit / 100
print("After Deposite fees:",After_Diposit)

Remaining_fees = Total_Fees - After_Diposit
print("Remaining fees:",Remaining_fees)

installment_1 = int(input("Enter your first installment: "))
Remaining_fees = Remaining_fees - installment_1
print("After first installment fees:",Remaining_fees)

installment_2 = int(input("Enter your second installment: "))
Remaining_fees = Remaining_fees - installment_2
print("After second installment fees:",Remaining_fees)

installment_3 = int(input("Enter your third installment: "))
Remaining_fees = Remaining_fees - installment_3
print("Total fees paid:",Remaining_fees)
