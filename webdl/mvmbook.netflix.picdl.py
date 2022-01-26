import wget
urlprefix = "https://mvmbook.netflixawards.com/pages/mitchells"
urlsuffix = ".jpg"
bookpage=range(0,114)
for page in bookpage:
    wget.download(urlprefix + str(page).zfill(3) + urlsuffix)