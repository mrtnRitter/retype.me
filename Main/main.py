from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed or not'))
ui.dark_mode(True)

ui.run()