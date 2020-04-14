import os
import json
import sys

name = sys.argv[0]
path = "/home/pi/mycroft-core/skills/"
for skill in os.listdir(path):
    print(skill)
    new_path = ''
    new_path = path + skill + "/settings.json"
    if ".msm" not in skill : 
        with open(new_path, 'r') as f: 
            data = json.load(f) 
            data['name'] = name
        os.remove(new_path) 
        with open(new_path, 'w') as f:
            json.dump(data, f, indent = 4)


