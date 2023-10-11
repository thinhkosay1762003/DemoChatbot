import requests
from bs4 import BeautifulSoup

def search_wikihow(message):
    base_url = "https://www.wikihow.vn"
    search_url = f"{base_url}/wikiHowTo?search={message}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all("a", class_="result_link")
    result = search_results[0]
    link = requests.get(result["href"])
    soup=BeautifulSoup(link.text,'html.parser')
    phuong_phap=soup.find_all("div",class_="method_label")
    for i, method in enumerate(phuong_phap, 1):
        # Lấy văn bản trong thẻ <div> và thẻ <h3>
        div_text = method.text.strip()
        h3_text = method.find_next("h3").text.strip()

        print(f"{div_text} {h3_text}")
        tutor_texts = method.find_next("b", class_="whb")
        a=1
        print(f" 1.{tutor_texts.text}")
        while tutor_texts and tutor_texts.find_next("div", class_="step_num") and tutor_texts.find_next("div", class_="step_num").text != '1':
            tutor_texts = tutor_texts.find_next("b", class_="whb")
            a=a+1
            print(f" {a}.{tutor_texts.text}")
n=input()
search_wikihow(n)
