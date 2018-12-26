list = []
while True:
    print ("enter a comment")
    com = input()
    print("previously entered comments")
    list.append(com)
    for com in list:
        i = 1 + list.index(com)
        print(str(i) + "." + com)