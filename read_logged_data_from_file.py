f = open("logdata.txt", "r")

for record in f:
    record = record.replace("\n", "")
    print(record)

f.close()