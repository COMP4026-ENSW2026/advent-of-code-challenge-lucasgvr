with open("sample.in") as file:
    commands = file.readlines()

dirs = {"/home":0}
path = "/home"

for command in commands:
    if command[0] == "$":
        if command[2:4] == "ls":
            pass
        elif command[2:4] == "cd":
            if command[5:6] == "/":
                path = "/home"
            elif command[5:7] == "..":
                path = path[0:path.rfind("/")]
            else:
                dir_name = command[5:]              
                path = path + "/" + dir_name        
                dirs.update({path:0})               
    elif command[0:3] == "dir":
        pass
    else:
        size = int(command[:command.find(" ")])     
        
        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]

total = 0
limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []

for dir in dirs:
    if dirs[dir] < 100000:
        total += dirs[dir]
    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])

smallest = min(valid_dirs)

print(smallest)