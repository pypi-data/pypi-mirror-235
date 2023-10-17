import reflex as rx

from flexdown import types
from flexdown.blocks.block import Block


demo_box_style = {
    "border_radius": "8px;",
    "border": "2px solid #F4F3F6",
    "box_shadow": "rgba(99, 99, 99, 0.1) 0px 2px 8px 0px;",
    "padding": 5,
    "width": "100%",
    "overflow_x": "auto",
}


class DemoBlock(Block):
    """A block that displays a component along with its code."""

    type = "eval"
    starting_indicator = "```python demo"
    ending_indicator = "```"

    def render(self, env: types.Env) -> rx.Component:
        code = self.get_content(env)
        comp = eval(code, env, env)
        code_block = self.component_map.get("codeblock", rx.code_block)
        return rx.vstack(
            rx.center(comp, style=demo_box_style),
            rx.box(
                code_block(code, language="python"),
                width="100%",
            ),
            padding_y="1em",
            spacing="1em",
        )
