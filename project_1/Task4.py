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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
# Create lists for telephone numbers
tel_num_outgoing_calls = []
tel_num_sent_text = []
tel_num_received_text = []
tel_num_received_calls = []

# Iterate over lists and append necessary info
for i in range(len(calls)):
    tel_num_outgoing_calls.append(calls[i][0])
    tel_num_received_calls.append(calls[i][1])
for i in range(len(texts)):
    tel_num_sent_text.append(texts[i][0])
    tel_num_received_text.append(texts[i][1])

# Remove duplicates
tel_num_outgoing_calls = list(set(tel_num_outgoing_calls))
tel_num_sent_text = list(set(tel_num_sent_text))
tel_num_received_text = list(set(tel_num_received_text))
tel_num_received_calls = list(set(tel_num_received_calls))

# Create a list with potential not telemarketers
not_telemarketers = list(set(tel_num_sent_text + tel_num_received_text + tel_num_received_calls))

potential_telemarketers = []

# Define potential telemarketers
for i in range(len(tel_num_outgoing_calls)):
    if tel_num_outgoing_calls[i] not in not_telemarketers:
        potential_telemarketers.append(tel_num_outgoing_calls[i])

# Remove duplicates
potential_telemarketers = list(set(potential_telemarketers))
# Sort list
potential_telemarketers.sort()

# Print out the result
print("These numbers could be telemarketers: ")
for number in potential_telemarketers:
    print(number)
