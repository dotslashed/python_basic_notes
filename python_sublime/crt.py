import requests
import os

resp = requests.get('https://crt.sh/?q=grasple.com&output=json')

json_data = resp.json()

for items in json_data:
	values_1 = items.values()
	for x in values_1:
		list1 = []
		list_val = list(values_1)
		domains_unsorted = list_val[2]
		new = domains_unsorted.replace('*.', '')
