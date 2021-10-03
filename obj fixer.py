file = open("charmander.obj", "r")
lines = file.readlines()

for line in lines:
    values = line.split(" ")
    if values[0] == "f":
        print("f "+str(values[1].split("//")[0])+" "+str(values[2].split("//")[0])+" "+str(values[3].split("//")[0]))
