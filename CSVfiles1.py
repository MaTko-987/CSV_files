
import csv


with open("data.csv",) as csv_file:
    csv_lines = csv_file.split()
    print(csv_lines)

    for line in csv_lines:
        print(line)




with open("ninja.txt", "r") as ninja_file:
    ninja_lines = ninja_file.read().splitlines() #lanac funkcija, čitanje iz fajla i splitaju se linije u isto vrijeme
    print(ninja_lines)

    for line in ninja_lines: #line je linija unutar ninja.txt --- for petlja prolazi kroz cijeli file i u svakom krugu će biti jedna linija file --- line ili x ili item
        print(line)

