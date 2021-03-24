
def group_by_owners(data):
    try:
        return_value = {}
        for key,value in data.items():
            if return_value.get(value):
                return_value[value].append(key)
            else:
                return_value[value] = [key]
        return return_value
    except Exception as e:
        print(str(e))


value = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

output = group_by_owners(value)