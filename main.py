pizzas = ["4 cheeses", "vegeterian", "hawai", "calzone", "four seasons"]
empty = ()

def display(collection):
    collection.sort()
    nb_pizza = len(collection)
    if nb_pizza == 0:
        print("No Pizza")
    else:
        print(f"--Pizza ({nb_pizza})--")
        for i in collection:
            print(i)
        print(f"First Pizza is {collection[0]} Last Pizza is {collection[-1]}")

def add_pizza(collection):
    p = input("Add your Pizza: ")
    # if pizza_exists(p, collection):
    if p.lower() in collection:
        print("Error: Pizza already exists.")
    else:
        collection.append(p)

      


add_pizza(pizzas)
display(pizzas)


