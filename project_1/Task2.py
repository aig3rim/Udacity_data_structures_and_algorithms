"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
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

# Change datatype from string to integer for the duaration column in calls file
for item in calls:
    item[3] = int(item[3])

# Create a dictionary with unique phone numbers
unique_tel_num_dict = dict.fromkeys(unique_tel_num_lst, 0)

# Calculate total time spent on the phone
for item in calls:
    unique_tel_num_dict[item[0]] += item[3]
    unique_tel_num_dict[item[1]] += item[3]

# Find a telephone number with the longest time spent
max_key = max(unique_tel_num_dict, key=unique_tel_num_dict.get)

# Print results
print("{} spent the longest time, {} seconds, on the phone during September 2016".format(max_key,
                                                                                         unique_tel_num_dict[max_key]))
