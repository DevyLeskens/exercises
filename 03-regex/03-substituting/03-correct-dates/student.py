# Write your code here
import re


def correct_dates(string):
    # return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2/\1/\3', string)
    return re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\1/\3', string)
