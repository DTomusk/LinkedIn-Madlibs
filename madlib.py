import json
import re
import random 
from twitter import LincolnIngram

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


	# this ought to be a new function 
	num_matches = len(re.findall('\{[^, ]+\}', template))

	for i in range(num_matches):
		sub_string = re.search('\{[^, ]+\}', template).group(0)
		var_range = len(data[sub_string.strip('{}')])
		first_element = data[sub_string.strip('{}')][random.randint(0, var_range-1)]
		template = re.sub(sub_string, first_element, template, 1)

	print(template)

	username = input("Username: ")
	password = input("Password: ")
	Link = LincolnIngram(username, password)

	Link.login()
	Link.tweet(template)

	# I wanted to see what was inside a 9v battery and now I've got two battery halves lying on my desk that I don't know what to do with (the insides weren't even that interesting)
	# it's clear that no LinkedIn post is just one sentence long, rather a post should be a combination of sentences each with their own specific function 
	# the structure of a post should follow a clear arc to make the author look as good as possible while maintaining an air of humility 
	# unfortunately a lot of these are neither funny nor realistic, so some might ask, what's the point? 

if __name__ == "__main__":
	main()