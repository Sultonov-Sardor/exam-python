# import requests
# from bs4 import BeautifulSoup

# data = requests.get("https://kun.uz/")
# soup = BeautifulSoup(data.text, "html.parser")

# items = soup.select("body > div.page-wrapper > div > div.page-body.pt60 > div.mob-container.bg-white > div > div:nth-child(2) > a > div.post-small__info > div > span")
# print(items)
# for item in items:
#     print(item)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# import requests
# from bs4 import BeautifulSoup

# def fetch_kurs():
#     url = "https://kun.uz/"
#     response = requests.get(url)

#     #  if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     elements = soup.find_all("body > div.page-wrapper > div > div.page-body.pt60 > div:nth-child(6) > div > div > div:nth-child(1) > a > div.post-small__info > h5")
#     print(elements)

#     # for ele in kurs:
#     #     valyuta = item["data-currency"]
#     #     aP = input("valyuta kriting")

#     #     if aP != valyuta:
#     #         aP *= valyuta
#     #         print(aP)

# fetch_kurs()


























import requests
from bs4 import BeautifulSoup

url = 'https://kun.uz/news/list'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('a', class_='daily-block l-item')

    for article in articles[:10]:
        title = article.find('p', class_="news-title").text
        time = article.find('p', class_="news-date").text

        print("Title:", title)
        print("Time:", time)
        print("*" * 80)