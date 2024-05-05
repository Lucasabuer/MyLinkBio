import reflex as rx
from myweb.components.link_icon import link_icon
from myweb.components.info_text import info_text
from myweb.styles.styles import Size as Size
from myweb.styles.colors import Color as Color
from myweb.styles.colors import TextColor as TextColor
import myweb.constants as const
import datetime


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Lucas haciendo lio",
                size="xl",
                src="favicon.ico",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Brais Moure",
                    size="lg"
                ),
                rx.text(
                    "@mouredev",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL
                    ),
                    link_icon(
                        "icons/spotify.svg",
                        const.SPOTIFY_URL
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL
                    ),
                    spacing=Size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+",
                "años de experiencia"
            ),
            rx.spacer(),
            info_text(
                "100+", "aplicaciones creadas"
            ),
            rx.spacer(),
            info_text(
                "1M+", "seguidores"
            ),
            width="100%"
        ),
        rx.text(
            f"""
            Soy ingeniero de software y actualmente trabajo como freelance
            full-stack developer iOS y Android.
            Además, creo contenido formativo sobre programación en redes.
            Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!
            """,
            font_size=Size.DEFAULT.value,
            color=TextColor.BODY.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2010