import requests
from bs4 import BeautifulSoup


def search_wikihow(query):
    base_url = "https://www.wikihow.vn"
    search_url = f"{base_url}/wikiHowTo?search={query}"
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all("a", class_="result_link")

        if not search_results:
            print("Không tìm thấy kết quả cho tìm kiếm này.")
        else:
            result = search_results[0]
            link = result["href"]
            tutorial_response = requests.get(link)

            if tutorial_response.status_code == 200:
                tutorial_soup = BeautifulSoup(tutorial_response.text, 'html.parser')
                steps = tutorial_soup.find_all("div", class_="step")

                print(f"Hướng dẫn cho '{query}':\n")
                for i, step in enumerate(steps, 1):
                    step_text = step.find("b",class_="whb")
                    if step_text:
                        print(f"{i}. {step_text.text}")

n = input("Nhập tên hướng dẫn bạn muốn tìm: ")
search_wikihow(n)

