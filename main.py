import yaml

def readYaml(path) -> {}:
    config = {}
    with open(path) as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
    return config
