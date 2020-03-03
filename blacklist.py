arr=[]
with open("tmp.sys") as stream:
    for line in stream:
        arr.append(line)
        if line == "go\n":
            print("fff")
            stream.write("ff")
print(arr)
