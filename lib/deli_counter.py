katz_deli = []

def take_a_number(deli_list, name):
    deli_list.append(name)
    position = len(deli_list)
    print(f"Welcome, {name}. You are number {position} in line.")

def line(deli_list):
    if not deli_list:
        print("The line is currently empty.")
    else:
        positions = [f"{index + 1}. {name}" for index, name in enumerate(deli_list)]
        print("The line is currently: " + " ".join(positions))

def now_serving(deli_list):
    if not deli_list:
        print("There is nobody waiting to be served!")
    else:
        serving_person = deli_list.pop(0)
        print(f"Currently serving {serving_person}.")

    
# This code defines a deli called "Katz Deli" using a list called katz_deli 
# to keep track of the names of customers waiting in line. The code also defines three functions:

# line(): This function prints out the current state of the line by 
# iterating over the katz_deli list and creating a list of positions 
# (1-indexed) for each customer in line. If the list is empty, it 
# prints a message indicating that the line is currently empty.
# take_a_number(name): This function takes a customer's name as
# an argument and adds it to the katz_deli list. It then calculates 
# the customer's position in line by finding the length of the list 
# and prints out a message indicating their position.
# now_serving(): This function checks if there is anyone waiting in 
# line. If there is, it removes the first customer from the katz_deli 
# list and prints out a message indicating who is currently being served.
# If there is no one waiting in line, it prints a message indicating that 
# there is nobody waiting to be served.
# Overall, this code simulates a simple queue for a deli and provides
# functions to add customers to the queue, print out the current state of the queue, and serve the next customer in line.