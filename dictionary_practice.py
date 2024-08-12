# Build a menu that lists the price and type of cake.
# Put the dictionary in reverse alphabet order
def add_to_menu(inventory_num, flavor, price):
    cakes[inventory_num] = [flavor, price]
def build_menu(cakes):
    items = []
    for flavor, price in cakes.values():
        items.append(f"{flavor} Cake - ${price}")
    return list(reversed(sorted(items)))


cakes = {
    100: ["Carrot", 1.99],
    101: ["Chocolate", 1.99],
    102: ["Strawberry", 2.19],
    103: ["Spice", 2.29],
    104: ["Vanilla", 1.79]
}
add_to_menu(105, "Coffee", 1.49)
print(build_menu(cakes))