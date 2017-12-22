import csv

with open("food.csv", 'r') as csvInput:
    with open("food2.csv", 'w') as csvOutput:
        reader = csv.reader(csvInput, delimiter=',', quotechar='"')
        writer = csv.writer(csvOutput, delimiter=',', quotechar='"')
        row0 = next(reader) #Go to the first line of the csv, which is the title
        row0.append("Quantity")
        writer.writerow(row0)
        for item in reader:
            item.append(1)
            writer.writerow(item)
            print(item)
