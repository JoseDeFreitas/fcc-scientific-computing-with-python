from math import floor

class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spent = 0  # used for the "create_spend_chart" function

    def __str__(self) -> str:
        item_list = []

        for item in self.ledger:
            digit = str(round(item["amount"], 2))
            # Adds another "0" if digit ends with "00"
            if isinstance(item["amount"], float) and len(digit.split(".")[1]) < 2:
                digit += "0"
            elif isinstance(item["amount"], int):
                digit += ".00"

            spaces = 30 - (len(item["description"][:24].strip()) + len(digit))
            length = 24  # where to stop the description string
            if spaces == 0:
                spaces = 1
                length = 23

            item_list.append(
                f"{item['description'][:length].strip()}{' ' * spaces}{digit}"
            )

        new_line = "\n"  # because backslashes can't be inside f-strings

        representation = (
            f"{self.name.center(30, '*')}\n"
            f"{new_line.join(item_list)}\n"
            f"Total: {self.balance}"
        )

        return representation

    def get_balance(self) -> float:
        """ Returns the current total balance of the account. """

        return self.balance

    def check_funds(self, amount: float) -> bool:
        """
        Returns whether the amount specified is greater or less than
        the actual balance of the account. This method is used by the
        withdraw and the transfer method to proceed.
        """

        result = False

        if self.balance >= amount:
            result = True

        return result

    def deposit(self, amount: float, description: str="") -> None:
        """
        Makes a deposit to the account specifying a custom amount
        and a custom description of what the deposit was for.
        """

        self.ledger.append(
            {"amount": amount, "description": description}
        )

        self.balance += amount

    def withdraw(self, amount: float, description: str="") -> bool:
        """
        Makes a withdraw from the account specifying a custom amount
        and a custom description of what the withdraw was for. If there
        are not enough funds, nothing gets as withdraw. Returns a
        boolean indicating if the withdraw was successful.
        """

        result = False

        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -1 * abs(amount), "description": description}
            )

            self.balance -= amount
            self.spent += abs(amount)
            result = True

        return result
    
    def transfer(self, amount: float, category: object) -> bool:
        """
        Transfers money to the category specified. Under the hood, what
        happends here is basically a withdrawal from the current
        category and a deposit to the specified category.
        """

        result = False

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")

            result = True

        return result


def create_spend_chart(categories: list) -> str:
    """
    Returns a bar chart showing how much percentage did every category
    spend based on the total amount spent by all categories. It is
    formatted in a way that illustrates a bar chart.
    """

    total_spent = sum([category.spent for category in categories])
    categories_spent = []

    # Get the percentage that each category spent
    for category in categories:
        categories_spent.append(
            floor(round((category.spent * 100) / total_spent) / 10.0) * 10
        )

    
    bars = ""  # each "o"s and spaces
    lines = []  # whole second lines
    for number in range(100, -1, -10):
        match = lambda value: value >= number  # tests each percentage
        o_or_white = list(map(match, categories_spent))  # "True" and "False" list
        percentages = ["o" if digit else " " for digit in o_or_white]

        bars = "  ".join(percentages)

        lines.append(
            f"{str(number).rjust(3)}| {bars}  "
        )

    new_line = "\n"  # because backslashes can't be inside f-strings

    dashes = f"    -{'-' * len(bars)}--"
    names = []  # each category name displayed vertically

    individuals = [category.name for category in categories]
    largest_length = len(max(individuals, key=len))

    listed = []
    for name in individuals:
        if len(name) < largest_length:
            listed.append(name + (" " * (largest_length - len(name))))
        else:
            listed.append(name)
    
    separated = list(map(list, listed))
    zipped = zip(*separated)  # all lists being mapped
    tupled = list(zipped)

    for values in tupled:
        names.append(f"     {'  '.join(values)}  ")

    bar_chart = (
        "Percentage spent by category\n"
        f"{new_line.join(lines)}\n"
        f"{dashes}\n"
        f"{new_line.join(names)}"
    )

    return bar_chart
