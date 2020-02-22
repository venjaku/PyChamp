#Downloading Images from a Link
#Note:Make sure that you have downloaded required modules.

import requests
import wget
from bs4 import BeautifulSoup

#The URL from where we are going to download images
url = "https://www.slideshare.net/secret/Ja6M4oWhJeik7O"

#Response Type
response = requests.get(url)

#Parsing Response Using Beautiful Soup
bs = BeautifulSoup(response.text, "html.parser")

#Declaring what to download through classes and file type
slides = bs.find_all("img",{"class":"slide_image"})

#Downloading Slides and Storing with a Specific name
for index,slide in enumerate(slides):
    imagename = "Venky" + "-" + str(index) + ".jpg"
    image = wget.download(slide["data-full"],imagename)
    print("Downloading - " + slide["data-full"])

#Ignore this Line - Credits: Venkatesh Vanjaku
