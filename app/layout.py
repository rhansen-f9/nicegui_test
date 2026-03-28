from contextlib import contextmanager
from nicegui import ui
import pages
from typing import Literal

@contextmanager
def frame(navigation_str: str):
    """Custom page frame to share the same styling and behavior across all pages"""
    ui.colors(
        primary='#5898d4', 
        secondary='#26a69a', 
        accent='#9c27b0', 
        positive='#21ba45',
        negative='#c10015',
        info='#31ccec',
        warning='#f2c037',
        dark='#000000',
        # color1='',
        # color2='',
        )

    with ui.header().classes('bg-primary'):
        with ui.row():
            ui.label('This is the header')
    
    with ui.left_drawer().classes('bg-secondary'):
        ui.label('This is a left drawer')
        for lbl in range(5):
            ui.label(f'Lable {lbl +1}')

    yield

    with ui.footer().classes('bg-primary'):
        ui.label('This is the footer')