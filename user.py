class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f'{self.name} ${self.account_balance}')

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

guido = User("Guido Van Rossum", "guido@dojo.com")
monty = User("Monty Python", "monty@python.com")
logan = User("Logan Domingo", "logankdoming@dojo.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(500)
guido.make_withdrawal(150)

guido.display_user_balance()

monty.make_deposit(500)
monty.make_deposit(200)
monty.make_withdrawal(100)
monty.make_withdrawal(300)

monty.display_user_balance()

logan.make_deposit(1000)
logan.make_withdrawal(500)
logan.make_withdrawal(200)
logan.make_withdrawal(300)

logan.display_user_balance()

guido.transfer_money(logan, 300)

guido.display_user_balance()
logan.display_user_balance()




