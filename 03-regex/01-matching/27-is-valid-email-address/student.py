# Write your code here
import re


def is_valid_email_address(string):
    return re.fullmatch('[0-9a-z.]+@(student\.ucll\.be|ucll\.be)', string)