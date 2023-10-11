import webbrowser as wb
from unidecode import unidecode
import wikipedia
from pyvi import ViTokenizer
from googletrans import Translator
import datetime
import requests
from bs4 import BeautifulSoup

def find_document(message):
    print("Tất nhiên rồi, bạn muốn tìm tài liệu cho môn học nào")
    search=input()
    print(f"Đây là tài liệu cho môn {search} mà bạn đang tìm ")
    search = "-".join(unidecode(search).split()).lower()
    url = f"https://cuuduongthancong.com/s/{search}"
    wb.get().open(url)
def homework(message):
    print("Đy là bài tập của bạn trên Code PTIT")
    url = f'https://code.ptit.edu.vn/student/question'
    wb.get().open(url)
def find_on_wikipedia(message):
    wikipedia.set_lang("vi")
    ignore_word=["tìm","cho","tôi","là","ai","gì","biết", "khái niệm","về","ý nghĩa"]
    infor = message.lower().split(' ')
    search=''
    for i in infor:
        if i not in ignore_word:
            search=search+' '+ i
    information = wikipedia.summary(search,sentences=3).split('.')
    for i in information:
        print(i)
def translate_text(text, target_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def dich_thuat(message):
    text = input("Để có thể hỗ trợ chuẩn xác nhất cho chức năng dịch thuật, hãy nhập đoạn văn bản bạn muốn dịch:\n")
    target=input("Bạn muốn dịch sang ngôn ngữ nào\n").lower()
    language_codes = {
        "tiếng việt": "vi",
        "tiếng anh": "en",
        "tiếng pháp": "fr",
        "tiếng hàn": "ko",
        "tiếng nhật": "ja",
        "tiếng nga": "ru",
        "tiếng trung": "zh-cn",
        "việt": "vi",
        "anh": "en",
        "pháp": "fr",
        "hàn": "ko",
        "nhật": "ja",
        "nga": "ru",
        "trung": "zh-cn"
    }
    if target in language_codes:
        tl = language_codes[target]
        translated_text = translate_text(text, tl)
        print(f"Đoạn văn bản được dịch thành:")
        print(translated_text)
    else:
        print("Xin lỗi, tôi không nhận ra được ngôn ngữ bạn nhập")

def find_on_google(message):
    ignore_word = ["tìm","kiếm","google","trên","cho","tôi","biết", "về"]
    infor = message.lower().split(' ')
    search = ''
    for i in infor:
        if i not in ignore_word:
            search = search + ' ' + i
    if len(search)<=1:
        search=input("Bạn muốn tìm gì trên Google\n")
    url = f"https://www.google.com/search?q=+{search}"
    wb.get().open(url)
    print(f'Đây là kết quả cho {search} của bạn trên Google')
def find_on_youtube(message):
    ignore_word = ["video","youtube","mở","cho","tôi","về","trên","tìm"]
    infor = message.lower().split(' ')
    search = ''
    for i in infor:
        if i not in ignore_word:
            search = search + ' ' + i
    if len(search) <=1:
        search = input("Bạn muốn tìm gì trên Youtube\n")
    url = f"https://youtube.com/search?q={search}"
    wb.get().open(url)
    print(f'Đây là kết quả cho {search} của bạn trên Youtube')
def open_code_ptit(message):
    print("Tất nhiên rồi, đây là bài tập trên Code Ptit để bạn có thể luyện thêm khả năng code.\nNgoài ra bạn có thể tham khảo tử CodeLearn, CodeAcademy, LeetCode để trao dồi thêm.")
    url="https://code.ptit.edu.vn/student/question"
    wb.get().open(url)
def show(message):
    print("Đánh giá hôm nay của bạn trên Code PTIT\n")
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



