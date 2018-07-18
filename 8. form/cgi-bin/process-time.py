import cgi
import json
import os

form = cgi.FieldStorage()
timing_value = form['timevalue'].value

print('Content-type: text/html \n\n')
print(json.dumps({"timing": timing_value}))