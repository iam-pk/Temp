import os
# ---------------- AI FOOD DATABASE ---------------- #
food_db = [
    {"name": "Margherita Pizza", "price": 250, "taste": "cheesy", "mood": "happy", "type": "veg"},
    {"name": "Peri Peri Pizza", "price": 320, "taste": "spicy", "mood": "excited", "type": "veg"},
    {"name": "Veg Burger", "price": 180, "taste": "crispy", "mood": "hungry", "type": "veg"},
    {"name": "White Sauce Pasta", "price": 220, "taste": "creamy", "mood": "relaxed", "type": "veg"},
    {"name": "Cold Coffee", "price": 120, "taste": "sweet", "mood": "tired", "type": "drink"},
    {"name": "Chocolate Brownie", "price": 150, "taste": "sweet", "mood": "romantic", "type": "dessert"}
]
# ---------------- AI ASSISTANT ---------------- #

def ai_recommend():
    print("\n==========  AI FOOD ASSISTANT ==========\n")

    budget = int(input("Enter your budget (₹): "))
    taste = input("Taste (spicy/sweet/cheesy/creamy/crispy): ").lower()
    mood = input("Mood (happy/relaxed/tired/excited/hungry/romantic): ").lower()

    recommendations = []

    for food in food_db:
        if food["price"] <= budget:
            if food["taste"] == taste or food["mood"] == mood:
                recommendations.append(food)

    print("\n🍽 Recommended Dishes\n")

    if recommendations:
        for item in recommendations:
            print(f"✔ {item['name']}  - ₹{item['price']}")
    else:
        print("❌ No matching food found.")
        print("Try increasing your budget.")


# ---------------- MAIN ---------------- #

print(" WELCOME TO PAUSE N PEACE")
print("\nWho are you?\n")

print("Customer")
print("Staff")
print("AI Assistant")
print("Exit")

a = input("\nEnter your choice : ").lower()

# ---------------- CUSTOMER ---------------- #

if a == "customer":

    print("\nWelcome Customer ❤️\n")

    p = input("Enter your Name : ")
    c = input("Enter Table Number : ")

    menu_path = r"D:\code\python\menu.png"

    if os.path.exists(menu_path):
        os.startfile(menu_path)
    else:
        print("Menu image not found!")

    f = input("\nEnter your Order : ")

    with open("order1.txt", "w") as h:
        h.write("Customer : " + p + "\n")
        h.write("Table : " + c + "\n")
        h.write("Order : " + f + "\n")

    with open("order2.txt", "w") as s:
        s.write(f)

    print("\n✅ Order Placed Successfully!")
    print("Our chef has received your order.\n")


# ---------------- STAFF ---------------- #

elif a == "staff":

    print("\nWelcome Staff 👨‍🍳")

    s = input("Choose (Kitchen Staff / Working Staff): ").lower()

    if s == "kitchen staff":

        print("\nToday's Kitchen Orders\n")

        try:
            with open("order2.txt", "r") as m:
                print(m.read())
        except FileNotFoundError:
            print("No Orders Yet.")

    elif s == "working staff":

        print("\nCustomer Details\n")

        try:
            with open("order1.txt", "r") as mn:
                print(mn.read())
        except FileNotFoundError:
            print("No Customer Orders.")

    else:
        print("Invalid Staff Type.")


# ---------------- AI ---------------- #

elif a == "ai assistant":
    ai_recommend()


# ---------------- EXIT ---------------- #

elif a == "exit":
    print("\n🙏 Thank You For Visiting Pause N Peace.")

else:
    print("❌ Invalid Choice.")
   
