# your code goes here!
import re

class EmailAddressParser:

    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    
    def __init__(self, emails):
        self.email_list = emails


    def parse(self):
        email_strings = re.split(r',|\s', self.email_list)
        parsed_emails = set()
        for string in email_strings:
            if self.email_regex.fullmatch(string):
                parsed_emails.add(string)
        
        return sorted(list(parsed_emails))