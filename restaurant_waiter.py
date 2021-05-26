# User Stories
# 1
# AS a User I want to be able to see the menu in a formatted way, so that I can order my meal.
# 2
# AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten
# 3
# As a user, I want to have my order read back to me in formatted way so I know what I ordered.

class OrderHelper:

    def __init__(self):
        self.order_active = True
        self.order_contents = []


    def show_menu(self):
        for item in menu.values():
            print(item)

    def add_item(self):
        print("Here's what's on the menu")
        self.show_menu()

        item = input("Please type your order. Type 'nothing' to add nothing: ")
        if item in menu.values():
            self.order_contents.append(item)
            print(f"{item} added to order.")
        else:
            return

