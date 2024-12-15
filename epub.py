# ------------------- IMPORTS -------------------#
from zipfile import ZipFile
from pathlib import Path
import os
from bs4 import BeautifulSoup

# ------------------- GLOBALS -------------------#






# ------------------- FUNCTIONS -------------------#

class ebook:
    def __init__(self, path):
        self.path = path
        self.ncx = None
        self.autor = None
        self.title = None
        self.totalpages = None
        self.playorder = []


    def __str__(self):
        pass

    def parse(self):
        p = Path(self.path).parent
        z = p.joinpath("epub")

        if not z.exists():
            z.mkdir()

        with ZipFile(self.path, "r") as zip:
            zip.extractall(z)

        for r, d, f in os.walk(z):
            for file in f:
                if file.endswith(".ncx"):
                    self.ncx = Path(r).joinpath(file)
                    break

        with open (self.ncx, "r", encoding="utf-8") as f:
            toc = BeautifulSoup(f.read(), "xml")

        self.autor = toc.find("docAuthor").find("text").text
        self.title = toc.find("docTitle").find("text").text
        self.totalpages = toc.find("meta", {"name" : "dtb:totalPageCount"}).get("content")
        
        for c in toc.findAll("navPoint"):
            url = c.find("content").get("src").split("#")[0]
            if not url in self.playorder:
                self.playorder.append(url)
        
    








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