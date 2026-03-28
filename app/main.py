from nicegui import ui
import pages

pages.home()

ui.run(
    title="Novus Roofing and Exteriors"
    # port=443,
    # ssl_certfile="<path_to_certfile>",
    # ssl_keyfile="<path_to_keyfile>",
)