import ystockquote as ys
import csv
import sys
import urllib2


""" First we import a CSV file with 2 columns: stock symbols, stock names """

data = {}

# The program checks for a command line argument
# It should be the name of the csv file
filename = str(sys.argv[1])

# Open CSV file and save as a dictionary
try:
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            symbol = row[0]
            name = row[1]
            data[symbol] = [name]  # Later, we add the price to the list
except IOError:
    print("Error opening file. Check your filename and try again.")
    exit()


""" Next we search yahoo using the date the user enters """

date = raw_input("Enter a date [yyyy-mm-dd]: ")
print("")

# Validate date input


# Search yahoo
for symbol in data.keys():
    # Try to search for symbol and notify user of errors
    try:
        price = ys.get_historical_prices(symbol, date, date)[1][4]
    except urllib2.HTTPError:
        price = "Error retreiving a price. Symbol not found."

    # Append price to list in data dict
    data[symbol].append(price)

# Print data for kicks
for k in data.keys():
    print("%s   [%s]  :    %s" % (data[k][0], k, data[k][1]))
