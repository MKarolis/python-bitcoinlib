import json

def format_json(input):
    dumped = json.dumps(input.__dict__)
    parsed = json.loads(dumped)
    return json.dumps(parsed, indent=4, sort_keys=True)