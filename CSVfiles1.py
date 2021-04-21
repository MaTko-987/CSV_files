
import csv


with open("data.csv",) as csv_file:
    csv_lines = csv_file.read().split()
    print(csv_lines)

    for line in csv_lines:
        print(line)








