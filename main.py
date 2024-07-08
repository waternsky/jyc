#!/usr/bin/env python

import yaml
import json
import gradio as gr


def main():
    gr.Interface(fn=json_yaml_ui,
                 inputs=["text", "textbox"],
                 outputs=["textbox"]).launch()


def json_yaml_ui(kind: str, input_string: str) -> str:
    match kind:
        case "json":
            return json_yaml(input_string)
        case "yaml":
            return yaml_json(input_string)
        case _:
            return "ERROR: Please provide valid input"


def json_yaml(inp: str) -> str:
    try:
        data = json.loads(inp)
    except Exception:
        return "ERROR: Invalid json"
    else:
        return yaml.dump(data, default_flow_style=False)


def yaml_json(inp: str) -> str:
    try:
        data = yaml.load(inp, Loader=yaml.SafeLoader)
    except Exception:
        return "ERROR: Invalid yaml"
    else:
        return json.dumps(data, indent=4)


if __name__ == "__main__":
    main()
