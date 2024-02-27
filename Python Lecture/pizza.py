def makePizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for toppings in toppings:
        print(f"- {toppings}")

makePizza(16, "chicken")
makePizza(12, "Mushroom", "Green Pepper", "extra cheese")  


# * is arbitrary argument jis se hm jitny marzi arguments pass kr sakty hain