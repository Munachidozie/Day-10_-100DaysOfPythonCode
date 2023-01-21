print ("== Tip Calculator ==")
print (" ")
total = float(input ("What is the total amount of the bill?  "))
print (total)
print (" ")
percentage = float(input ("What percentage of the bill do you want to tip the waiter?  "))
print (percentage,"%")
people = int(input("How many people are in the group?  "))
print (people)
answer = (percentage / 100 * total) + total
final_answer = answer / people
print ("You each owe", final_answer)