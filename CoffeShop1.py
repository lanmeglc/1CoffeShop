print("Hello, welcome to Lan's Coffe shop!!!!!!!!")

name = input("What is your name?\n")

print("Hello " + name + " thank you so much for coming in tonight.")

menu = "Menu: coffe and sandwich or coffe and eggs on our menu"

print(name, "here is your menu. \n" + menu)

order = input("What do you want " + name + "? \n")

print("We will have your" + order + "ready")

price = 10

quantity = input("How many menus would you like?\n")

total = price * int(quantity)

print("Your total is: " + "$" + str(total))

print("Thank you very much for your order, hope to see you again soon. ")
