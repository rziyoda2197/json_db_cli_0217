import json

FILE = "db.json"

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=2)

while True:
    print("1.Add 2.Show")
    c = input("> ")

    data = load()

    if c=="1":
        name = input("name: ")
        data.append({"name":name})
        save(data)

    if c=="2":
        print(data)
