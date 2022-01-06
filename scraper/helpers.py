import json


def save_as_json(data,name_of_file):
	filename = f'{name_of_file.replace(" ", "-")}.json'
	with open(filename,"w") as file:
		json.dump(data,file,indent=4)