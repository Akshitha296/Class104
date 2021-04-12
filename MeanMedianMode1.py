import csv

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

    print(file_data)