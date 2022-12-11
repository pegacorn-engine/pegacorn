import json


def json_output(raw_string_dict):
    return json.dumps(raw_string_dict, indent=4)
