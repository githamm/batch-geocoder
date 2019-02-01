import geocoder
import csv
#import time

rows = []
fieldnames = ['dwellingType', 'recordID', 'dateIssued', 'permitType', 'permitValuation', 'units', 'address', 'contractor', 'statCode', 'neighborhood', 'postal', 'confidence', 'lat', 'lng']

# File name to be geocoded
with open('input.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for line in reader:
        g = geocoder.here(line['address'], app_id='app id would go here' , app_code='app code would go here')

        # Add the CSV line data into the Geocoder JSON result
        result = g.json
        result.update(line)

        # Store Geocoder results in a list to save it later
        rows.append(result)

with open('results.csv', 'a') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
    #time.sleep(2)