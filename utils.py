import json
import yaml


def json_to_yaml(inp: str) -> str:
    out = ""
    try:
        data = json.loads(inp)
    except Exception:
        out = "[bold red]ERROR[/bold red]: Invalid json string"
    else:
        out = yaml.dump(data)
    return out


def yaml_to_json(inp: str) -> str:
    out = ""
    try:
        data = yaml.load(inp, Loader=yaml.SafeLoader)
    except Exception:
        out = "[bold red]ERROR[/bold red]: Invalid yaml string"
    else:
        out = json.dumps(data, indent=4)
    return out
