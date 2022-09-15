# Class methods are a way to create alternate constructors, simple factories

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
    
    def __str__(self):
        return f"${self.dollars}.{self.cents}"

    @classmethod
    def from_pennies(cls, total_cents):
        dollars = total_cents / 100
        cents = total_cents % 100
        return cls(dollars, cents)

    @classmethod
    def from_string(cls, amount):
        return cls(dollars, cents)


class Drip(Money):
    def __str__(self):
        return f'I got got this much drip ${self.dollars}.{self.cents:.2f} bitch'


def main():
    my_money = Money(1, 25)
    print(my_money)
    my_penny = Money.from_pennies(1000)
    print(my_penny)
    my_drip = Drip.from_pennies(10000000000)
    print(my_drip)



if __name__ == '__main__':
    main()
