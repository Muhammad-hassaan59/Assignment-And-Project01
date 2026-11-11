# Name : Muhammad Hassaan
# # Trainee ID: TRN-2026-000361
# Date: 08/11/2026



#******************************************** Warm-up — Add hints ******************************

# ***************************** Part05_functions.py ************************************
#Add type hints to all your Part 5 functions, including return types. Install mypy and run mypy part05_functions.py . Fix anything it reports.

# *************************************************************************************
# **************************************************************************************

# ************************************* Build — Product dataclass ******************************


from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    # Check price and stock
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative")


# Create 5 products
products = [
    Product("Laptop", 80000, 5, ["Electronics", "Computer"]),
    Product("Mouse", 1500, 0, ["Electronics", "Accessory"]),
    Product("Keyboard", 3000, 10, ["Electronics"]),
    Product("Headphones", 5000, 0, ["Audio", "Accessory"]),
    Product("Mobile", 60000, 3, ["Electronics", "Phone"])
]


# Print products that are out of stock
print("Out of Stock Products:")

for product in products:
    if product.stock == 0:
        print(product)



# *************************************************************************************
# **************************************************************************************



#***************************************** Challenge — Save and load *******************************



from dataclasses import dataclass, field, asdict
import json


@dataclass(order=True)
class Product:
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

        if self.stock < 0:
            raise ValueError("Stock cannot be negative")


# Create 5 products
products = [
    Product("Laptop", 80000, 5, ["Electronics", "Computer"]),
    Product("Mouse", 1500, 0, ["Electronics", "Accessory"]),
    Product("Keyboard", 3000, 10, ["Electronics"]),
    Product("Headphones", 5000, 0, ["Audio", "Accessory"]),
    Product("Mobile", 60000, 3, ["Electronics", "Phone"])
]


# Step 1: Save products to products.json
with open("products.json", "w") as file:
    json.dump([asdict(p) for p in products], file, indent=4)

print("Products saved successfully!")


# Step 2: Load products back from JSON
with open("products.json", "r") as file:
    data = json.load(file)

loaded_products = [Product(**d) for d in data]

print("\nLoaded Products:")
for product in loaded_products:
    print(product)


# Step 3: Sort products by price
sorted_products = sorted(
    loaded_products,
    key=lambda p: p.price
)

print("\nProducts sorted by price:")
for product in sorted_products:
    print(product)

#************************************* The End **********************************************************

































