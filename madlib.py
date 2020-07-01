import json

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

	template = data["templates"][option]

	# should be an automated way to go through all {} and find a corresponding option from another value in data

if __name__ == "__main__":
	main()