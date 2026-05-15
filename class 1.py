import random

x, y, z = [random.randint(1, 100) for _ in range(3)]

print("Original:", x, y, z)

ans = []

if x >= y and x >= z:
    ans.append(x)

    if y >= z:
        ans.append(y)
        ans.append(z)
    else:
        ans.append(z)
        ans.append(y)

elif y >= x and y >= z:
    ans.append(y)

    if x >= z:
        ans.append(x)
        ans.append(z)
    else:
        ans.append(z)
        ans.append(x)

else:
    ans.append(z)

    if x >= y:
        ans.append(x)
        ans.append(y)
    else:
        ans.append(y)
        ans.append(x)

print("Descending:", ans)