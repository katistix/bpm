import json

def read(box):
    data = open("boxes/" + box + "/box_config.json", 'r')
    return json.load(data)