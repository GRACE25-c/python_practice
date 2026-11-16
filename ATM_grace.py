total_amound=5000
widraw_amount=1350

#print("total_amound",'=',total_amound)
#print("widraw_amount",'=',widraw_amount)

#calculating the remainning balance
remaining_balance=total_amound-widraw_amount
print("Remaining Balance of the customer: ",remaining_balance)


 #check whether the widrawl amount is < the available balance

print(" the withdrawal amount is less than the available balance",widraw_amount,'<',remaining_balance,widraw_amount<remaining_balance)
print(" the remaining balance is greater than ₹1,000:",remaining_balance,'>',1000,remaining_balance>1000)

#Calculate how many ₹500 notes and how much remainder will be needed to represent the remaining balance.
fivehundrad_notes= remaining_balance//500

print(" how many ₹500 notes we want to get the remainig balance:",fivehundrad_notes," 500 notes")

print(' how much remainder will be needed to represent the remaining balance is',remaining_balance%500)

