"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create empty lists for each column with telephone numbers in texts and calls
sending_tel_num_txt_lst = []
receiving_tel_num_txt_lst = []
sending_tel_num_calls_lst = []
receiving_tel_num_calls_lst = []

# Loop over the lists of lists and create lists with unique telephone numbers
# for each type of records
for item in texts:
    if item[0] not in sending_tel_num_txt_lst:
      sending_tel_num_txt_lst.append(item[0])
    if item[1] not in receiving_tel_num_txt_lst:
        receiving_tel_num_txt_lst.append(item[1])

for item in calls:
    if item[0] not in sending_tel_num_calls_lst:
      sending_tel_num_calls_lst.append(item[0])
    if item[1] not in receiving_tel_num_calls_lst:
        receiving_tel_num_calls_lst.append(item[1])

# Find unique telephone numbers for all records

unique_tel_num_lst = list(set(
                            sending_tel_num_txt_lst +\
                             receiving_tel_num_txt_lst +\
                              sending_tel_num_calls_lst +\
                               receiving_tel_num_calls_lst
                               ))
# Print results
print("There are {} different telephone numbers in the records.".format(
                                                                        len(unique_tel_num_lst)
                                                                        ))
