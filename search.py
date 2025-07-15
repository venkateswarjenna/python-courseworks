products=["mobiles","tabs","laptops","mouse"]
search_items=input("search the items")

for product in products:
    if product.lower()== search_items.lower():
        print(f"'{search_items}' is avaliable")
        break
else:
     print(f"sorry'{search_items}' are not avaliable")