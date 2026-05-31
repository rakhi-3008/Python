data =True
line =1
with open(r"d:\Desktop\python\Python\file_io\data.txt", "r") as f :
    while data:
        data=f.readline()

        if("Python" in data):
            print(f"word found at line {line}")
            break

        line+=1