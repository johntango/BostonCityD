# read json from url and print the data
import json
import urllib.request
import urllib.parse
import urllib.error

url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
print(type(data))
print(data[:2])
# print the structure of the data

# load the data into a dictionary
info = json.loads(data)
myData = info["data"]  # get the data part of the dictionary

print(myData[0:5])
print("Total salary:"+  myData[0][18])
print("Total salary:"+  myData[1][18])

