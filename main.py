class BankAccount:

  def __init__(self, account_number, account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposite(self, amount):
    if amount > 0:
      self.__account_balance += amount
      #self._account_balance = self._account_balance+amount
      print("deposited ₹{}. New balance: ₹{}".format(amount, 
                                        self.__account_balance))
    else:
      print("invalid deposite amount. please deposite a positive amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      #self._account_balance = self._account_balance - amount
      print("withdraw ₹{}. New balance: ₹{}".format(amount, 
                                                    
self.__account_balance))
    else:
      print("invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
      print("Account balance for {} (Account #{}): ₹{}".format( 
      self.__account_holder_name, self.__account_number,
        self.__account_balance))
#create an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                     account_holder_name="sophika",
                     initial_balance=5000.0)

#test deposite and withdrawal functionality
account.display_balance()
account.deposite(500.0)
account.withdraw(200.0)
account.withdraw(10000.0)
account.display_balance()