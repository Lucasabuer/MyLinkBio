import reflex as rx
from myweb.components.navbar import navbar
from myweb.components.footer import footer
from myweb.views.header import header
from myweb.views.links import links
from myweb.views.sponsors import sponsors
import myweb.styles.styles as styles
from myweb.styles.styles import Size as Size


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )


app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="MoureDev | Te enseño programación y desarrollo de software",
    description="Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador.",
    image="avatar.jpg"
)
