import yaml


def read_yaml(path) -> {}:
    config = {}
    with open(path) as file:
        try:
            config = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc)
    return config


class Yaml:

    def __init__(self, path):
        super(Yaml, self).__init__()
        self.config = read_yaml(path)

    def value(self, value: str):
        def fun(f):
            values = value.split(".")
            r_value = None
            for v in values:
                r_value = self.config[v] if r_value is None else r_value[v]
            return r_value

        return fun
