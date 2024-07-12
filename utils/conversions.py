import json
import yaml


def json_to_yaml(inp: str) -> str:
    out = ""
    try:
        data = json.loads(inp)
    except Exception:
        out = "ERROR: Invalid json string"
    else:
        out = yaml.safe_dump(data, allow_unicode=True,
                             default_flow_style=False, sort_keys=False)
    return out


def yaml_to_json(inp: str) -> str:
    out = ""
    try:
        data = yaml.safe_load(inp)
    except Exception:
        out = "ERROR: Invalid yaml string"
    else:
        out = json.dumps(data, indent=4)
    return out
