from pprint import pprint

for num in range(2, 11, 2):
    print(f"The number is: {num}")

colors = ["Red", "Green", "Blue", "Orange"]

for index, item in enumerate(colors):
    print(f"{index}: {item}")

hex_colors = {
    "Red": "#FF0000",
    "Green": "#008000",
    "Blue": "#0000FF",
}

for color, hex_value in hex_colors.items():
    print(f"For color {color}, the hex value is: {hex_value}")


for i, num in enumerate(range(0, 21, 2)):
    print(f"{i}: {num}")


names = ["John", "Paul", "George", "Ringo"]
my_list = []
for name in names:
    my_list.append(len(name))
print("Before:", my_list)

print("After:", [len(name) for name in names])

my_list = [name for name in names if len(name) % 2 != 0]
print(f"Odd names: {my_list}")

print(" - ".join(("John,Paul,George,Ringo").split(",")))
pprint([("double length", len(name) * 2) for name in names])

squares = {num: num * num for num in range(10)}
pprint(squares)

scores = {f"player-{num}": 0 for num in range(0, 5)}
pprint(scores)

my_list = [(f"player-{num}", num * 2) for num in range(0, 5)]
pprint(my_list)

scores = {key: value for (key, value) in my_list}
pprint(scores)

# List comprehension
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
print(list_comp)

# Generator expression
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(gen_exp)

for num in gen_exp:
    print(num)

for num in gen_exp:
    print(num)  # nothing happens. Generator is exhausted
