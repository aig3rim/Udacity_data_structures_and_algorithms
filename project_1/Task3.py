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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
# Define function for identifying area codes
def return_area_code(tel_number):
    """
    This function returns are code for a telephone number.
    """

    # Fixed-line
    if tel_number.startswith('(0'):
        return tel_number.split(')')[0]+')'

    # Telemarketers
    if tel_number.startswith('140'):
        return '140'

    # Mobile phone numbers
    if (' ' in tel_number) and (tel_number.startswith('7') or tel_number.startswith('8') or tel_number.startswith('9')):
        return tel_number[:4]

    else:
        return None

bang_called_area_codes = []

# Find area codes called by Bangalore telephone numbers
for i in range(len(calls)):
    if calls[i][0].startswith('(080)'):
        bang_called_area_codes.append(return_area_code(calls[i][1]))

# Remove duplicates
bang_called_area_codes = list(set(bang_called_area_codes))
# Sort list in in lexicographic order
bang_called_area_codes.sort()

# Print results
print("The numbers called by people in Bangalore have codes:")
for code in bang_called_area_codes:
    print(code)

# Part B
bang_to_all_tel_num_cnt = 0
bang_to_bang_tel_num_cnt = 0

for i in range(len(calls)):
    if calls[i][0].startswith('(080)'):
        bang_to_all_tel_num_cnt += 1
        if calls[i][1].startswith('(080)'):
            bang_to_bang_tel_num_cnt += 1

# Calculate the percentage of calls made to Bamgalore from Bangalore
pcnt_to_bang = round((bang_to_bang_tel_num_cnt * 100) / bang_to_all_tel_num_cnt, 1)

# Print results
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(pcnt_to_bang))
