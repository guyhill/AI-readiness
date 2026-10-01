import yaml
from pprint import pprint

with open("output.yaml", "r") as file:
    x = yaml.safe_load(file)
pprint(x)
