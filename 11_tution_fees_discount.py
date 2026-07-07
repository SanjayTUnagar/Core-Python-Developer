
# Tution Fees Discount taking input from user 

Total_Fees = int(input ("Enter your tution fees: "))
Diposit = float(input ("Enter deposite (%): "))

After_Diposit = Total_Fees * Diposit / 100
print("After Deposite fees:",After_Diposit)

Remaining_fees = Total_Fees - After_Diposit
print("Remaining fees:",Remaining_fees)

Fees_Diposit = Remaining_fees * 50 / 100
print("After Diposit remainig fees:", Fees_Diposit)

installment_1 = int(input("Enter your first installment: "))
Fees_Diposit = Fees_Diposit - installment_1
print("After first installment fees:",Fees_Diposit)

installment_2 = int(input("Enter your second installment: "))
Fees_Diposit = Fees_Diposit - installment_2
print("After second installment fees:",Fees_Diposit)

installment_3 = int(input("Enter your third installment: "))
Fees_Diposit = Fees_Diposit - installment_3
print("Total fees paid:",Fees_Diposit)
