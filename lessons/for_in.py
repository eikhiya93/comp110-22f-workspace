"""An example of for in syntax."""

names: list[str] = ["Tun", "Lisa", "Kendra", "Alex"] 

# Examples of iterating thorugh names using a while loop
print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for...in loop is the same as the while loop above 
print("for...in output:")
for x in names: 
    print(x)



# x: int = 1
# def fu(y: int) -> None: 
#     return x + y 

# print(fu(x + 1))