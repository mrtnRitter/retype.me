# ------------------- IMPORTS -------------------#
from zipfile import ZipFile
from pathlib import Path



# ------------------- GLOBALS -------------------#






# ------------------- FUNCTIONS -------------------#

class ebook:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        pass

    def unzip(self):
        p = Path(self.path).parent
        z = p.joinpath("epub")

        if not z.exists():
            z.mkdir()

        with ZipFile(self.path, "r") as zip:
            zip.extractall(z)

    def parse():
        pass



















# open content file from tmp path




# index files and read text htmls in chapter order




# display text htmls on editor page


# parse html elements in own box with remove option and search for same ids or html entities in all docs when removing



# store updated html, parse each letter as span with dimmed color



# listen to keyboard inputs, compare input with current span, red wrong, undimmed right





# book = epub.read_epub(path)

# #print (book.get_metadata("DC", "title"))
# #print (book.get_metadata("DC", "creator"))


# texts = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
# images = book.get_items_of_type(ebooklib.ITEM_IMAGE)

# #for image in images:
#     #print(image.get_content())


# for i, text in enumerate(texts):  
#     if i == 5:
#         html_page = text.get_content().decode("utf8")


# raw_text = BeautifulSoup(html_page, features="html.parser").get_text()

# print (html_page)