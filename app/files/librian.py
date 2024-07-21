import json


def txt_to_str(file, direction=False):
    if direction:
        with open(f"app/files/directions/{file}", 'r', encoding='utf-8') as f:
            string = f.read()
            f.close()
        return string
    else:
        with open(f"app/files/{file}", 'r', encoding='utf-8') as f:
            string = f.read()
            f.close()
        return string


def get_directions(group):
    with open('app/files/all_directions.json', 'r') as f:
        directions = json.load(f)
        f.close()
    result = list()
    for item in directions[group]:
        result.append(((txt_to_str(item, True)), item))
    return result


def get_cods():
    with open('app/files/all_directions.json', 'r') as f:
        directions = json.load(f)
        f.close()
    result = list()
    for key in directions.keys():
        for item in directions[key]:
            result.append(item)
    return result


def get_b():
    with open('app/files/calc/b.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    return directions


def get_m():
    with open('app/files/calc/m.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    return directions


def get_a():
    with open('app/files/calc/a.json', 'r', encoding='utf-8') as f:
        directions = json.load(f)
        f.close()
    return directions


def new_member(name):
    with open('app/stat.json', 'r') as f:
        stat = json.load(f)
        f.close()
    stat["cnt"] += 1
    if name not in stat["members"]:
        stat["members"].append(name)
    with open('app/stat.json', 'w') as f:
        json.dump(stat, f)
        f.close()


def get_stat():
    with open('app/stat.json', 'r') as f:
        stat = json.load(f)
        f.close()
    return stat