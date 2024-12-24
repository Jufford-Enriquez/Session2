
import argparse
import csv                              # Import the CSV module to handle CSV file reading.

parser = argparse.ArgumentParser()

args = parser.parse_args()


with open("data.csv","r") as f:         # Create a CSV reader object to process the file.
    reader = csv.reader(f)              # Loop through each row in the file, with `i` as the row index and `row` as the row data.
    for i, row in enumerate(reader):    # Check if it's the first row (header row).

        if i ==0:
            print(f"|{'|'.join(row)}|") # Format and print the header row, joining column names with ' | '.

        else:                           # If it's not the first row (data row).
            print(f"|{'|'.join(row)}|") # Format and print the data row, joining values with ' | '.  

parser.add_argument('-i','--input')


