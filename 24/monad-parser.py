import re
import random

f = "input.txt"

monad = [1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 9, 9, 9, 9]

row = 0
var = {}
zmin = 99999999999999


program = []
for line in open(f).readlines():
    
    l = line.strip().split()
    program.append(l)
    

while True:
    
    start = random.randrange(11111111111111, 99999999999999)
    #start = 23492989573778 # renders 2 in z
    #start = 13492999573778 # renders 1 in z
    #       134929*9573778 # renders 2 in z
    
    #start = 82391861162377 # renders 0
    #start = 82391861162377 # renders 0
    #start = 34578438495188
    
    monad = list(map(int,list(str(start))))
    #start -= 1
    
    if 0 not in monad:
    
        var["w"] = var["x"] = var["y"] = var["z"] = var["stack"] = 0
        
        for line in program:
            l = line.copy()
            
            if len(l) == 3:
                if re.match(r'^[-0-9]+$', l[2]):
                    var["stack"] = int(l[2])
                    l[2] = "stack"
                
            if l[0] == "inp":
                var[l[1]] = monad.pop(0)
                
            elif l[0] == "add":
                var[l[1]] += var[l[2]]
            elif l[0] == "mul":
                var[l[1]] *= var[l[2]]
            elif l[0] == "mul":
                var[l[1]] *= var[l[2]]
            elif l[0] == "div":
                var[l[1]] = int(var[l[1]]/var[l[2]])
            elif l[0] == "mod":
                var[l[1]] = var[l[1]] % var[l[2]]
            elif l[0] == "eql":
                if var[l[1]] == var[l[2]]:
                    var[l[1]] = 1
                else:
                    var[l[1]] = 0
            
            row += 1
            var["stack"] = 0
        
        if var["z"] < zmin:
            zmin = var["z"]
            print(start,var["z"])
        
        if var["z"] == 0:
            print(start,var)
            break
     
    break
