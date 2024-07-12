import gradio as gr
from .conversions import json_to_yaml, yaml_to_json


def convert(inp: str, kind: str) -> str:
    out = ""
    if inp.strip()[0] in ("[", "{") and kind == "yaml":
        return "ERROR: Please check correct options are specified"
    match kind:
        case "json":
            out = json_to_yaml(inp)
        case "yaml":
            out = yaml_to_json(inp)
        case _:
            out = "ERROR: Please check correct options are specified"
    return out


def interface() -> gr.Interface:
    return gr.Interface(
        fn=convert,
        inputs=[
            gr.Textbox(label="Input", lines=8),
            gr.Dropdown(
                ["json", "yaml"],
                label="JSON or YAML?",
                info="Type of input string"
            )
        ],
        outputs=[
            gr.Textbox(label="Output", lines=10)
        ],
        title="JYC: JSON to YAML Converter",
        flagging_dir="store"
    )
