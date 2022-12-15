import csv

dic = {1:[["car",1,2,3,4],["bloom",11,2,3,22]],2:[["mouse",1,2,3,4],["vie",11,2,3,22]]}

with open("test.csv","w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["frameID","name","xmin","ymin","xmax","ymax"])
    for i in dic:
        for j in dic[i]:
            writer.writerow([i,*j])

