email_test = """joey@example.com jadoe@sample.co qsus@example.br joes@sample.com"""

print email_test

import pandas as pd

email_dict = {
    'name': ['john', 'jane', 'susan', 'joe'],
    'email': ["joey@example.com", "jadoe@sample.co", "qsus@example.br", "joes@sample.com"]
}

df = pd.DataFrame(email_dict , columns=['name','email'])

print df


import re

pattern = r'([A-Za-z]+)'

regex = re.compile(pattern, flags=re.IGNORECASE)

match = regex.match("abc@example.com")

print match.groups()

search_string = regex.findall(email_test)

print search_string