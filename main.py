import sys
import json 
import os

os.system("curl -X POST -u \"apikey:52Z4tDujEEKo3-Vw45gifumAEHzI7CCFBfYBAA9e-C6E\" --form \"images_file=@"+sys.argv[1]+"\" \"https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19\" > output.json")

ingredients = []

with open('output.json') as json_data:
    json_data = json.load(json_data)
    for dictionary in json_data["images"]:
        for classes in dictionary["classifiers"]:
            for eachClass in classes["classes"]:
                if "type_hierarchy" in eachClass:
                    ingredients.append(eachClass["class"])

print(ingredients)


