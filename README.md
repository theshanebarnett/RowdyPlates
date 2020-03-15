# RowdyPlates

Scalable real time asset tracking using license plate recognition on a self contained device.

The system interpreted license plate images and utilized a HTML scraping tool
to return all publicly available data. The system was built with
Python, Node.js, and a machine learning model on a Raspberry Pi

RowdyPlates was created by @bairdChris, @theshanebarnett, @nickb210, and Riley Gilliam in less than 24 hours during the hackathon RowdyHacks

## Requirements

- Node.js
- Python 3
- A Raspberry Pi with Raspbian and a PiCamera

## Usage
1. Run the Node.js file within the Raspbian environment 
2. Use your PiCamera to capture a legible license plate image
3. Receive all publicly available data associated with that license plate number, including the vehicle Python file is in the same directory and your PiCamera is properly 

## Issues

- Currently doesn't operate unless it's run within the Raspbian environment
- Can only input license plate images through a Raspberry Pi camera

## Acknowledgements
- Matt Hill and the team at OpenALPR for their open source license plate recognition API
- The Beautiful Soup Community for their Python HTML scraping library
- The RowdyHacks organization for putting together this amazing event 
