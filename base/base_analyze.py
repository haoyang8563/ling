import yaml


def analyze_data(file_name, func_name):
    with open("data/" + file_name + ".yaml", "r") as f:
        content = yaml.load(f, yaml.FullLoader)[func_name]
        data = list()
        data.extend(content.values())
        return data
