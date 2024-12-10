# Logging Data to File:

# Typically you want to write multiple data to the, e.g., assume you read some temperature data at regular intervals
# and then you want to save the temperature values to a File.

data = [1.6, 3.4, 5.5, 9.4]

f = open("logdata.txt", "x")

for value in data:
    record = str(value)
    f.write(record)
    f.write("\n")

f.close()

# Read logged data from file

f = open("logdata.txt", "r")

for record in f:
    record = record.replace("\n", "")
    print(record)

f.close()