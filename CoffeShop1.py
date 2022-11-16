print("Hello, welcome to Lan's Coffe shop!!!!!!!!")

name = input("What is your name?\n")

if name == "Mark" or name == "Mod" or name == "Loki":
  evil_status = input("Are you evil?\n")
  good_jobs = int(input("How many good jobs did you do today?\n"))
  if evil_status == "Yes" and good_jobs < 4:
    print("You are not welcome here " + name + "get outta here!!.")
    exit()
  else: print("Hello " + name + " thank you so much for coming in tonight")

else: print("Hello " + name + " thank you so much for coming in tonight")

menu = "Menu: coffe and eggs, coffe and sandwich, frappucino, black coffe, cake"

print(name, "here is your menu. \n" + menu)

order = input("What do you want " + name + "? \n")

quantity = input("How many menus/coffes/cakes would you like?\n") 


print("We will have your " + order + " ready ")

coffe_and_sandwich = 10
coffe_and_eggs = 15
black_coffe = 3
frappucino = 6
cake = 4


total_sandwich = coffe_and_sandwich * int(quantity)
total_eggs = coffe_and_eggs * int(quantity)
total_black_coffe = black_coffe * int(quantity)
total_frappucino = frappucino * int(quantity)
total_cake = cake * int(quantity)

if order == "coffe and eggs":
    print("Your total is: " + "$" + str(total_eggs))
elif order == "coffe and sandwich":
    print("Your total is: " + "$" + str(total_sandwich))
elif order == "black coffe":
    print("Your total is: " + "$" + str(total_black_coffe))
elif order == "frappucino":
    print("Your total is: " + "$" + str(total_frappucino))
elif order == "cake":
    print("Your total is: " + "$" + str(total_cake))
else:
    print("We don't have this item on out menu, please select something different")


print("Thank you very much for your order, hope to see you again soon. ")
