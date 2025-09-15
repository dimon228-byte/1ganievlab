print("x y z")
for x in range(0, 2):
    print("x y z")
    for y in range(0, 2):
        print("x y z")
        for z in range(0, 2):
            print("x y z")
            if not((x or y) <= (z == x)):
                print(x, y, z)