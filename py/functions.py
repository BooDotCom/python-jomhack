# def greet_person(name):
#     print(f"Hi, {name}.")

# greet_person("Bob")

def add_scaling(current,stack):
    bonus = 10
    return current + bonus * stack

base_dmg = 50
for i in range(5):
    print(f"Damage at {i} stacks: {add_scaling(base_dmg,i)}")