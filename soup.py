import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.bilgisayarhocam.com")

if url.status_code == 200:
    print("Siteden veri çekilebilir.")
else:
    print("Siteden veri çekilemez")
    
    
soup = BeautifulSoup(url.content, "html.parser") # sitenin htmlsini parçalıyor

# yazdir = soup.find("p").text # find önüne gelen ilk istenileni geri döndürür

yazdir = soup.find("footer", {"class":"bg-black"}).text

print(yazdir)