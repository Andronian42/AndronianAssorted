import wget
urlprefix = "https://disney-studios-awards.s3.amazonaws.com/luca/books/flipH45pEt23wR/files/mobile/"
urlsuffix = ".jpg"
bookpage=range(1,181)
for page in bookpage:
    wget.download(urlprefix + str(page) + urlsuffix)