# calls the needed libraries
# csv helps work with .csv files, used to open, read and write to them
import csv

#tkinter is used to choose which file we want to change
import tkinter
from tkinter import filedialog,messagebox

# Path is used for working with strings as directory names
from pathlib import Path

# time and datetime, help with the time pieces of the code, turning dates into epoch time (time in seconds)
import time
import datetime


# these are the lists that will hold the clent objects
client_list = []
needed_reviews = []

# client is a custom object that i use to manipulate the clients and store their information
class client:
    def __init__(self,name,since,review):
        self.name = name
        self.since = since
        self.review = review
        self.review_deadline = 0
        self.since_et = 0
        self.review_et = 0
        self.review_deadline_et = 0
        
# this opens a .csv file in the format that the lpl export function currently (1/4/2022) exports it into
# column 1 is client name
# column 2 is the date the client has been workign with me, "Client since date"
# column 3 is the date of the clients last recorded review
file_name = filedialog.askopenfilename()
print(file_name)
read_csv = Path(file_name)
with open(read_csv) as csvfile:
    data = csv.reader(csvfile)
    i=0
    # this for/if loop skips the first row, which is the header and then checks to see if there are values for since/review date,
    # if there are values it appends them to the client_list
    for row in data:
        name = row[1]
        since = row[10]
        review = row[0]
        if i >= 1 and since != '' and review != '':
            each_client = client(name,since,review)
            each_client.since_et = int(time.mktime(datetime.datetime.strptime(since, "%m/%d/%Y").timetuple()))
            each_client.review_et = int(time.mktime(datetime.datetime.strptime(review, "%m/%d/%Y").timetuple()))
            client_list.append(each_client)
        i += 1

# the length of a year in seconds or "epoch time"
year_in_seconds = 31556926

# this for and while loop converts the client since date into a review deadline, by adding a year onto it and checking if its in the future
# then it checks to see if the client has had a review within 1 year of the deadline, if not it appends that client to the needed_review list
for client in client_list:
    review_deadline = client.since_et + year_in_seconds
    while review_deadline < time.time():
        review_deadline += year_in_seconds
    client.review_deadline_et = review_deadline
    client.review_deadline = datetime.date.fromtimestamp(client.review_deadline_et)
    client.review_deadline = datetime.date.strftime(client.review_deadline, "%m/%d/%Y")  
    if (client.review_et + year_in_seconds) < review_deadline:
        needed_reviews.append(client)

write_csv = Path('clients_needing_reviews.csv')
with open(write_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Client Name", "Review Deadline", "Last Review"])
    for client in needed_reviews:
        row = [client.name, client.review_deadline, client.review]
        csvwriter.writerow(row)

#for client in needed_reviews:
#     print(client.name)
#     print(client.review)
#     print(client.review_deadline)

#print(len(client_list))
#print(len(needed_reviews))