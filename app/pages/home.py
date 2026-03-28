from nicegui import ui
import layout as layout

def home() -> None:
    """Home page"""
    @ui.page('/')
    def content():
        with layout.frame('- Home Page -'):
            ui.label('This is the home page')

            ui.button('Click me!')
            colors = [
                ('primary', 'white'),
                ('secondary', 'white'),
                ('info', 'dark'),
                ('warning', 'dark'),
                ('dark', 'white'),
                ('positive', 'white'),
                ('negative', 'white'),
                ('accent','white'),
                ]
            for (bg, fg) in colors:
                with ui.card().classes(f'w-50 bg-{bg} text-{fg} text-bold items-center'):
                    ui.label(f'{fg} on {bg}')