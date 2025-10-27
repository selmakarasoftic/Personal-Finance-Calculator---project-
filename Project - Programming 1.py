from datetime import datetime
#function to calculate monthly payment based on loan amount, interest rate and time
#using the formula for calculation, the function returns calculated monthly payment


def calculateMonthlyPayment(loanAmmount, interestRate, time):
  interestRateOneMonth = interestRate / 12 / 100
  timeMonths = time * 12
  monthlyPayment = (loanAmmount * interestRateOneMonth) / (
      1 - (1 + interestRateOneMonth)**-timeMonths)
  return monthlyPayment


#function that calculates total interest based on the loan amount, monthly payment, and time
#the loop in the dunction calculates interest for each month and updates the remaining loan amount
#when the loop is completed the
def calculateInterest(loanAmount, monthlyPayment, time):
  totalPayments = monthlyPayment * time * 12  # Total payments made over the loan duration
  totalInterest = totalPayments - loanAmount  # Total interest paid
  return totalInterest


#class that will represent a savings instance
class savings:

  #initializing the values over the constructor
  def __init__(self, initialAmmount, monthlyPayment, interest, time):
    self.initialAmmount = initialAmmount
    self.monthlyPayment = monthlyPayment
    self.interest = interest
    self.time = time

  #function to calculate the savings using the formula
  def calculateSavingsProjection(self):
    monthlyInterest = self.interest / 100 / 12
    months = self.time * 12
    savings = (self.initialAmmount * (1 + monthlyInterest)**months +
               self.monthlyPayment *
               ((1 + monthlyInterest)**months - 1) / monthlyInterest)

    return savings


#saving the data to a file
def save_data(data):
  current_time = datetime.today().isoformat()
  with open('C:\\Users\\selma\\Desktop\\history.txt', 'a') as file:
    file.write(current_time)
    file.write("\n")
    for key, value in data.items():
      file.write(f"{key}: {value}\n")
  print("Data saved successfully!")


#the start of the program and listing the options
print("📈🖥 Personal Finance Calculator 📈🖥")
while True:
  print(
      "Chose the option that you are interested in. The options are: \n 1 Loan payments💰 \n 2 Interest rates💸 \n 3 Savings projection💲 "
  )
  print(" 4 Saving the data💼 \n 5 Loading Data📜 \n 6 exit the calculator🏃\n")

  userPreference = input("Enter the number (1-6): ")

  if userPreference == '1':
    print(
        "\nYou have chosen Loan Payments💰. You should enter the information needed!"
    )

    #handling the possible error, for ecample if user enters the letter, it will print out the except
    try:
      #collecting important information before calling the function
      print("\nEnter three numbers.")
      print("\nloan ammount: ")
      loanAmmount = float(input())
      print("\nInterest rate in percentage: ")
      interestRate = float(input())
      print("\nYears for completing the loan: ")
      time = float(input())

      #calling the function to calculate the payment
      monthlyPayment = calculateMonthlyPayment(loanAmmount, interestRate, time)
      print("Your monthly payment is:", monthlyPayment, "\n")
    except ValueError:
      print("Invalid number entered!\n")

#the next part functions almost the same as the previous, only the next one is calculating
#the interest instead of monthly payment
  elif userPreference == '2':
    print(
        "You have chosen Interest Rates💸. You should enter the information needed!"
    )
    try:
      print("\nEnter three numbers.")
      print("\nloan ammount: ")
      loanAmmount = float(input())
      print("\nMonthly payment: ")
      monthlyPayment = float(input())
      print("\nYears for completing the loan: ")
      time = float(input())
      interest1 = calculateInterest(loanAmmount, monthlyPayment, time)
      print("The paid interest is:", interest1, "\n")
    except ValueError:
      print("Invalid number entered!\n")

#the next part also functions almost the same as the first part, only the next one is calculating
#savings amount instead of monthly payment
  elif userPreference == '3':
    print(
        "You have chosen Savings Projection💲. You should enter the information needed!"
    )
    try:
      print("\nEnter four numbers.")
      print("\nInital savings amount: ")
      initialAmmount = float(input())
      print("\nMonthly payment: ")
      monthlyPayment = float(input())
      print("\nInterest: ")
      interest = float(input())
      print("\nYears for completing the loan: ")
      time = float(input())
      savings_instance = savings(initialAmmount, monthlyPayment, interest,
                                 time)
      savingsProjection = savings_instance.calculateSavingsProjection()
      print("Savings would be: ", savingsProjection, "\n")
    except ValueError:
      print("Invalid number entered!\n")

#saving the data to a file, but only if every calculation is made until this option
  elif userPreference == '4':
    print("You have chosen Save Data💼.")
    try:
      data = {
          'loan_payment': loanAmmount,
          'total_interest': interest1,
          'savings': savingsProjection
      }
      save_data(data)
    except NameError:
      print("No data calculated yet!\n")

#the saved data will be read only if it exists, if not the exception will be shown
  elif userPreference == '5':
    print("You have chosen Load Data.📜")
    try:
      print("History: ")

      with open('C:\\Users\\selma\\Desktop\\history.txt', 'r') as file:
        history = file.read()  # Read the entire file content
        # Check if the file has content
        print(history)  # Print the entire content
    except FileNotFoundError:
      print("No saved data found.")

  elif userPreference == '6':
    print("Thank You for using the calculator! Have a nice day.👋")
    break

  elif userPreference != '1' or userPreference != '2' or userPreference != '3' or userPreference != '4' or userPreference != '5' or userPreference != '6':
    print("Invalid option entered! Try again.\n")
