class Category:
    # class creats a ledger of a specific category
    # with an arrey of actions in the category
    # EXAMPLE:
    # clothes category will have a deposit and the amount to use in the category
    # and specifaid puechase of cloths and there cost
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        # appends to the ladger a deposit in a dic form
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # appends to the ladger a withdraw in a dic form
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        # adds to one category and withdraws from they other
        # return a boolean if the action want through
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # returns a strig of all the actions in the ledger
        output = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            description = item["description"][:23]
            amount = "{:.2f}".format(item["amount"])
            output += f"{description} {amount.rjust(30 - len(description))}\n"
        total = "{:.2f}".format(self.get_balance())
        output += f"Total: {total}"
        return output

    
def create_spend_chart(categories):
    # returns a simple chart of the precentage of every category 
    chart = "Percentage spent by category\n"
    sum = 0
    spent_percentages = []
    # backend
    for category in categories:
        temp_sum = 0
        for item in category.ledger:
            
            if item['amount'] > 0:
                sum += item['amount']
                temp_sum += item['amount']
        spent_percentages.append(temp_sum)

    for i in range(len(spent_percentages)):
        spent_percentages[i] = (spent_percentages[i] / sum)*100

    # chart
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in spent_percentages:
            if abs(percentage) >= i:
                chart += "o" 
            else:
                " "
            chart += "  "
        chart += "\n"
    
    chart += "    ----------\n     "
    
    max_length = max(len(category.category) for category in categories)
    
    for i in range(max_length):
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i < max_length - 1:
            chart += "\n     "
    
    return chart

# Example usage:
food_category = Category("Food")
clothing_category = Category("Clothing")
auto_category = Category("Auto")

food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
clothing_category.deposit(100, "initial deposit")
clothing_category.withdraw(50, "Transfer to Auto")
auto_category.deposit(100, "initial deposit")
auto_category.transfer(50, clothing_category)

categories = [food_category, clothing_category, auto_category]

print(create_spend_chart(categories))
