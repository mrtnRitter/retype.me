# ------------------- IMPORTS -------------------#
from nicegui import ui, events
from nicegui.events import KeyEventArguments
from pathlib import Path
from epub import ebook

# ------------------- GLOBALS -------------------#
ui.dark_mode(True)

# !! temporary hard coded!!
user_root = "Users/01223355/"


# --------------------- INIT ---------------------#
# set up new user and mkdir all dirs and files
# user name = hash from username and pass




# ------------------- FUNCTIONS -------------------#

def store_file(e: events.UploadEventArguments):
    f = Path(e.name)    
    b = Path(user_root, "Bookshelf", f.with_suffix(""))
    if not b.exists():
        b.mkdir()

    newbook = ebook(b.joinpath(f))

    with open (newbook.path, "wb") as file:
        file.write(e.content.read())
    
    newbook.unzip()
    













# ----------------------- UI -----------------------#


ui.upload(auto_upload=True, max_files=1, label="Upload ePub File", on_upload=store_file).props("accept=.epub").classes("max-w-full")







ui.run()
#ui.run(reload=False, port=native.find.open_port())