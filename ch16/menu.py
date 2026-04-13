class food_item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"
    def get_price(self):
        return self.price
    
class burger(food_item):
    def __init__(self,name,price):
        super(burger, self).__init__(name,price)
        self.condiments = []

    def add_condiment(self,condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)

    def __str__(self):
        s = super(burger, self).__str__()
        s = s + "Condiments: " + ", ".join(self.condiments)
        return s

class drink(food_item):
    def __init__(self,name,size,price):
        super(drink, self).__init__(name,price)
        self.size = size

    def __str__(self):
        s = super(drink, self).__str__()
        s = s + "Size: " + str(self.size) + "oz"
        return s

class combo(food_item):
    def __init__(self,name,b,d,s,discount):
        self.name = name
        self.burger = b
        self.drink = d
        self.side = s 
        self.discount = discount
        self.price = self.burger.get_price() + self.drink.get_price() + self.side.get_price() -self.discount
    
    def __str__(self):
        s = ""
        s = s + "Combo: "+ self.name + "\n"
        s = s + str(self.burger) + "\n" + str(self.drink) + "\n" + str(self.side) + "\n" + str(self.burger.get_price() + self.drink.get_price() + self.side.get_price()) + "\n"
        s = s + "Discount: $" + str(self.discount) + "\n"
        s = s + "Combo Price After Discount: $"  + str(self.price) + "\n"

        return s
    
class side(food_item):
    def __init__(self,name,price):
        super(side, self).__init__(name,price)

class order:
    def __init__(self,name):
        self.name = name
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)
    
    def get_price(self):
        price = 0.0
        for item in self.items:
            price = price + item.get_price()
        return price

    def display(self):
        print(self)
    
    def __str__(self):
        lines = []
        lines.append("=" * 30)
        lines.append("Here is a summary of your order")
        lines.append("Order for " + self.name)
        lines.append("Here is a list of items in the order")

        for item in self.items:
            lines.append("=" * 30)
            lines.append(str(item))
        lines.append("=" * 30)
        lines.append("Total Order Amount :$" + str(self.get_price()))
        lines.append("=" * 30)
        return "\n".join(lines)
