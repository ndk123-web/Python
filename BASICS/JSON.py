import json

x = '{"name":"Navnath","age":19,"city":"mumbai"}'

y = json.loads(x)   # converts json to python dictionary
print(y['age'])

# dict
l = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

z = json.dumps(l)   # converts python dictionary to json
print(z)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))