#!/bin/python

import sys

def isValid(email):
    # Complete this function
    mail_parts = email.split("@")
    if len(mail_parts) != 2:
    	return "No"
    if len(mail_parts[0]) != 5:
    	return "No"
    if not is_ascii(mail_parts[0]):
    	return "No"
    if mail_parts[1] != "hogwarts.com":
    	return "No"
    return "Yes"

def is_ascii(s):
    return all(c.isalpha() and c.islower() for c in s)

if __name__ == "__main__":
    s = raw_input().strip()
    result = isValid(s)
    print result
