products = ["Laptop", "Phone", "Tablet", "Headphones", "Camera"]

search_item = input("Enter product to search: ")

for product in products:
    if product.lower() == search_item.lower():
        print(f"✅ '{search_item}' is available in stock!")
        break
else:
    print(f"❌ Sorry, '{search_item}' is not available.")
