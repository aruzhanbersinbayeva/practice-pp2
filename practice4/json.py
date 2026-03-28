import json
data = {
    "name": "Arman",
    "age": 16,
    "skills": ["Python", "Math", "English"]
}

json_string = json.dumps(data, indent=4)
print("JSON string:")
print(json_string)

parsed_data = json.loads(json_string)
print("\nParsed data:")
print(parsed_data)
print("\nName from parsed data:", parsed_data["name"])