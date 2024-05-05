import reflex as rx
import myweb.constants as const
from myweb.styles.styles import Size as Size
from myweb.components.title import title
from myweb.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor(
                "elgato.png",
                const.ELGATO_URL
            ),
            link_sponsor(
                "mvp.png",
                const.MVP_URL
            ),
            spacing=Size.BIG.value
        ),
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )
