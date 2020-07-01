import json
import re

# take a template and insert random words from different categories into the tags 
# print the templates next to numbers and then let the user choose a number which wil randomly generate a post accordingly
def main():
	with open('templates.json') as f:
		data = json.load(f)

	print("Choose your template:")

	for i, x in enumerate(data["templates"]):
		print(i+1, x["title"])

	option = int(input(""))-1

	# should check input is valid 

	template = data["templates"][option]["text"]

	# should be an automated way to go through all {} and find a corresponding option from another value in data
	# can use string format to insert value in braces, but what do we do when there's more than one element of the same type?
	# we could do until re.match doesn't match any values 

	print(template)
	num_matches = len(re.findall('\{[^, ]+\}', template))
	print(num_matches)

	for i in range(num_matches):
		sub_string = re.search('\{[^, ]+\}', template).group(0)
		print(sub_string)
		first_element = data[sub_string.strip('{}')][0]
		print(first_element)
		template = re.sub(sub_string, first_element, template, 1)
		print(template)

	print(template)

if __name__ == "__main__":
	main()