katz_deli = []

def line():
    if not katz_deli:
        print("The line is currently empty.")
    else:
        positions = [f"{index + 1}" for index, name in enumerate(katz_deli)]
        print("The line is currently: " + ", ".join(positions))

def take_a_number(name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving():
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Now serving {serving_person}.")

    
