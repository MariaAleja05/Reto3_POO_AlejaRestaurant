class MenuItem:                                          

    def __init__(self, name, price):
        self.name = name       
        self.price = price  

class Appetizer(MenuItem):                              # Clase appetizer hereda name y price de ManuItem
    def __init__(self, name):
        super().__init__(name, price=0)
    
    def item_selected(self):                            # Se definen los elementos que puede elegir el usuario con su precio correspondiente
        name = self.name
        if name == "bruschetta":
            return 7.99
        elif name == "spinach and artichoke dip":
            return 8.49
        elif name == "caprese salad":
            return 9.99
        elif name == "stuffed mushrooms":
            return 10.49
        elif name == "shrimp cocktail":
            return 12.99
        else:
            return 0

class MainCourse(MenuItem):                             # Mismo sentido que la clase Appetizer
    def __init__(self, name):
        super().__init__(name, price=0)
    
    def item_selected(self):
        name = self.name
        if name == "grilled salmon":
            return 16.99
        elif name == "chicken parmesan":
            return 14.99
        elif name == "beef tenderloin steak":
            return 22.99
        elif name == "vegetable stir fry":
            return 12.99
        elif name == "pasta with grilled chicken":
            return 15.49
        else:
            return 0

class SideDish(MenuItem):                               # Mismo sentido que la clase Appetizer
    def __init__(self, name):
        super().__init__(name, price=0)
    
    def item_selected(self):
        name = self.name
        if name =="french fries":
            return 3.99
        elif name =="mashed potatoes":
            return 4.49
        elif name =="steamed vegetables":
            return 5.29
        elif name =="garlic bread":
            return 3.99
        elif name =="onion rings":
            return 4.99
        else:
            return 0

class Dessert(MenuItem):                                # Mismo sentido que la clase Appetizer
    def __init__(self, name):
        super().__init__(name, price=0)
    
    def item_selected(self):
        name = self.name
        if name=="chocolate cake":
            return 6.99
        elif name=="cheesecake":
            return 5.49
        elif name=="tiramisu":
            return 7.99
        elif name=="apple pie":
            return 4.99
        elif name=="ice cream":
            return 4.79
        else:
            return 0

class Beverage(MenuItem):                               # Mismo sentido que la clase Appetizer
    def __init__(self, name):
        super().__init__(name, price=0)
    
    def item_selected(self):
        name = self.name
        if name=="soda":
            return 1.99
        elif name=="juice":
            return 2.49
        elif name=="coffee":
            return 2.99
        elif name=="iced tea":
            return 2.29
        elif name=="smoothie":
            return 4.99
        else:
            return 0

class Order:                                            # En esta clase se define el menu, lo que ingresa el usuario, el total, del recibo, descuentos e imprime la factura
    def __init__(self):
        self.items = [] 
        self.prices=[]

    def show_menu(self):                                # Se muestra el menu
        print("Alejas Restaurant")

        print("\nAppetizer:")
        print("Bruschetta..............................7.99")
        print("Spinach and artichoke dip...............8.49")
        print("Caprese salad...........................9.99")
        print("Stuffed mushrooms......................10.49")
        print("Shrimp cocktail........................12.99")
        
        print("\nMain Course:")
        print("Grilled salmon.........................16.99")
        print("Chicken parmesan.......................14.99")
        print("Beef tenderloin steak..................22.99")
        print("Vegetable stir fry.....................12.99")
        print("Pasta with grilled chicken.............15.49")

        print("\nSide Dish")
        print("French fries............................3.99")
        print("Mashed potatoes.........................4.49")
        print("Steamed vegetables......................5.29")
        print("Garlic bread............................3.99")
        print("Onion rings.............................4.99")

        print("\nDessert")
        print("Chocolate cake..........................6.99")
        print("Cheesecake..............................5.49")
        print("Tiramisu................................7.99")
        print("Apple pie...............................4.99")
        print("Ice cream...............................4.79")

        print("\nBeverage")
        print("Soda...................................1.99")
        print("Juice..................................2.49")
        print("Coffee.................................2.99")
        print("Iced tea...............................2.29")
        print("Smoothie...............................4.99")

        print("\n")

    def order_items(self):                              # Es todo lo que ingresa el usuario
        items=self.items
        prices=self.prices

        quantity_appetizer=int(input("Insert the quantity of appetizer: "))
        for i in range (quantity_appetizer):
            name_appetizer = input("Insert your Appetizer: ").lower()
            appetizer=Appetizer(name_appetizer)
            items.append(appetizer)
            price=appetizer.item_selected()
            prices.append(price)

        quantity_maincourse=int(input("Insert the quantity of main course: "))
        for i in range (quantity_maincourse):
            name_maincourse=input("Insert your MainCourse: ").lower()
            maincourse=MainCourse(name_maincourse)
            items.append(maincourse)
            price=maincourse.item_selected()
            prices.append(price)

        quantity_sidedish=int(input("Insert the quantity of side dish: "))
        for i in range (quantity_sidedish):
            name_sidedish=input("Insert your SideDish: ").lower()
            sidedish=SideDish(name_sidedish)
            items.append(maincourse)
            price=sidedish.item_selected()
            prices.append(price)

        quantity_dessert=int(input("Insert the quantity of dessert: "))
        for i in range (quantity_dessert):
            name_dessert=input("Insert your Dessert: ").lower()  
            dessert=Dessert(name_dessert)
            items.append(dessert)
            price=dessert.item_selected()
            prices.append(price)

        quantity_beverage=int(input("Insert the quantity of beverage: "))
        for i in range (quantity_beverage):
            name_beverage=input("Insert your Beverage: ").lower() 
            beverage=Beverage(name_beverage)
            items.append(beverage)
            price=beverage.item_selected()
            prices.append(price)

    def calculate_total_bill(self):                     # Se calcula el total de la factura
        total_bill=0
        prices=self.prices
        for i in prices:
            total_bill=total_bill+i
        return total_bill

    def discounts(self):                                # Se evalua si tiene descuentos
        total_bill=self.calculate_total_bill()
        if total_bill>40.00:
            bill_with_discounts=total_bill-((total_bill*5)/100)
            return bill_with_discounts
        else:
            return total_bill
    
    def print_bill(self):                               # Se imprime la factura
        items=self.items
        total_bill=self.calculate_total_bill()
        discounts=self.discounts()

        print("Your bill:\n")
        for item in items:
            name = item.name
            price = 0.0
            if name == "bruschetta":
                price = 7.99
            elif name == "spinach and artichoke dip":
                price = 8.49
            elif name == "caprese salad":
                price = 9.99
            elif name == "stuffed mushrooms":
                price = 10.49
            elif name == "shrimp cocktail":
                price = 12.99
            elif name == "grilled salmon":
                price = 16.99
            elif name == "chicken parmesan":
                price = 14.99
            elif name == "beef tenderloin steak":
                price = 22.99
            elif name == "vegetable stir fry":
                price = 12.99
            elif name == "pasta with grilled chicken":
                price = 15.49
            elif name == "french fries":
                price = 3.99
            elif name == "mashed potatoes":
                price = 4.49
            elif name == "steamed vegetables":
                price = 5.29
            elif name == "garlic bread":
                price = 3.99
            elif name == "onion rings":
                price = 4.99
            elif name == "chocolate cake":
                price = 6.99
            elif name == "cheesecake":
                price = 5.49
            elif name == "tiramisu":
                price = 7.99
            elif name == "apple pie":
                price = 4.99
            elif name == "ice cream":
                price = 4.79
            elif name == "soda":
                price = 1.99
            elif name == "juice":
                price = 2.49
            elif name == "coffee":
                price = 2.99
            elif name == "iced tea":
                price = 2.29
            elif name == "smoothie":
                price = 4.99
            print("{:<27}{}".format(name.capitalize(), "{:.2f}".format(price)))        # El format es para que se formatee cada vez
        print("\n")
        print("Your order costs: " + str(total_bill))
        if discounts!=total_bill:
            print("\n")
            print("Congrats! You obtain a discount of 5% in your bill")
            print("Your total cost is: " + str(discounts))

my_order = Order()
my_order.show_menu()
my_order.order_items()
print("\n")
my_order.print_bill()