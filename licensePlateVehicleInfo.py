'''
  Written by Chris Baird, Shane Barnett, Nick Brell, and Riley Gilliam
  RowdyHacks 2019 | April 13-14

  RowdyPlates

  RowdyPlates was created in less than 24 hours during the hackathon RowdyHacks

  The system interpreted license plate images and utilized a HTML scraping tool
  to return all publicly available data. The system was built with
  Python, Node.js, and a machine learning model on a Raspberry Pi
'''

import sys
import os
import requests

# HTML scraping package
from bs4 import BeautifulSoup

# Saves the plate number read from the API call in the alprNode.js file
plateNumURL = sys.argv[1]

# Creates a URL to query searchquarry.com
urlWithNum = "https://www.searchquarry.com/vehicle_records/lregister-new?sqwp=yes&sqtb=license_plate&trackstat=id-20734-&license_plates=" + plateNumURL + "&state=TX"

# Stores the publicly available data related to the license plate number
data = requests.get(urlWithNum)

# Creates a new directory and stores the information
if not os.path.isdir("./" + plateNumURL):
    os.mkdir("./" + plateNumURL)

    # Creates a text file for the vehicle information
    vHistory = open("./" + plateNumURL + "/" + "vehicleHistory" + ".txt", "w")
    vHistory.close()

    # Scrapes the data from HTML searchquarry using the urlWithNum variable
    soup = BeautifulSoup(data.text, 'html.parser')

    # New List for storing data
    data = []

    # Stores the scraped data in the list
    for tr in soup.find_all('tr'):
        vehicleInfo = [td.text for td in tr.find_all('td')]
        data.append(vehicleInfo)
        
    # Creates an output file to save info from license plate to current directory
    outFile = open("./" + plateNumURL + "/" + "vehicleInfo" + ".txt", "w")

    # Cleans up the data that was retrieved
    year = ''.join(data[2])
    make = ''.join(data[3])
    model = ''.join(data[4])
    body = ''.join(data[5])
    engine = ''.join(data[6])

    # Writes vehicle info to txt file
    fullString = str(year + "\n" + make + "\n" + model + "\n" + body + "\n" + engine)
    outFile.write(fullString)
    outFile.close()

    # Prints out the results
    print(fullString)

else:

    # Opens an existing file
    vHistory = open("./" + plateNumURL + "/" + "vehicleHistory" + ".txt", "a")
    vHistory.close()
