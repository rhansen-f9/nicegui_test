from contextlib import contextmanager
from nicegui import ui, app
import pages

@contextmanager
def frame(navigation_str: str):
    """Custom page frame to share the same styling and behavior across all pages"""
    app.colors(
        primary='#0a5997', 
        secondary='#4ebbeb', 
        accent='#120377', 
        positive='#21ba45',
        negative='#c10015',
        info='#31ccec',
        warning='#f2c037',
        dark='#000000',
        on_primary='#ffffff',
        # color1='',
        # color2='',
        )

    with ui.header().classes('bg-primary'):
        with ui.row():
            ui.label('This is the header')
            ui.label('on_primary on primary').classes(f'bg-primary text-on_primary')
    
    with ui.left_drawer().classes('bg-secondary'):
        ui.label('This is a left drawer')
        for lbl in range(5):
            ui.label(f'Lable {lbl +1}')

    yield

    with ui.footer().classes('bg-primary'):
        ui.label('This is the footer')