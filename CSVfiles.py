
import csv

with open('data.csv') as csv_file: #The open() function opens a file, and returns it as a file object.

    csv_reader = csv.reader(csv_file, delimiter=',')
    # the csv.reader() is used to read the file, which returns an iterable reader object.
    # delimiter specifies the character used to separate each field. The default is the comma (',').


    line_count = 0

    for row in csv_reader:

        if line_count == 0:
            print(f'{row[0]},{row[1]},{row[2]}')  #F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.
            line_count += 1

        else:
            print(f'\t{row[0]} is {row[1]} and {row[2]}.') #In Python strings, the backslash "\" is a special character, also called the "escape" character.
            # It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.
            line_count += 1




