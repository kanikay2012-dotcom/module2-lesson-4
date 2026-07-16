products = ["Widgets", "Gadgets", "Gizmos"]
total_quantities = [45, 72, 30]
box_size = 10  
stock_report = []
print("--- Packing Inventory ---")
product_index = 0
while product_index < len(products):
    current_product = products[product_index]
    remaining_items = total_quantities[product_index]
    packed_boxes = 0
    loose_items = 0
    while remaining_items > 0:
        if remaining_items >= box_size:
            remaining_items -= box_size
            packed_boxes += 1
        else:
            loose_items = remaining_items
            remaining_items = 0
            
    print(f"Packed {current_product}: {packed_boxes} boxes and {loose_items} loose items left.")
    stock_report.append([current_product, packed_boxes, loose_items])
    product_index += 1
print("\n--- Final Stock Report ---")
for row in stock_report:
    for detail in row:
        print(detail, end=" | ")
    print() 