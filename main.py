import random
import json
import pickle
import numpy as np
import task
import datetime
from keras.models import load_model
from pyvi import ViTokenizer




data = json.loads(open('data.json', encoding='utf-8').read())
tu=pickle.load(open('tu.pkl', 'rb'))
nhan=pickle.load(open('nhan.pkl', 'rb'))
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words=ViTokenizer.tokenize(sentence).split(' ')
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag= [0] * len(tu)
    for w in sentence_words:
        for i,word in enumerate(tu):
            if word==w:
                bag[i]=1
    return np.array(bag)

def predict_class(sentence):
    bow=bag_of_words(sentence)
    res=model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD =0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse = True)
    return_list = []
    for r in results:
        return_list.append({'data':nhan[r[0]], 'probability': str(r[1])})
    return return_list
def get_response(intents_list, data_json,message):
    tag=intents_list[0]['data']
    danh_sach_chu_de = data_json['du_lieu']
    list_of_task = data_json['nhiem_vu']
    for i in list_of_task:
        if i['tag'] == tag:
            eval(f"task.{i['mission']}('{message}')")
            break
    for i in danh_sach_chu_de:
         if i['tag'] == tag:
            print(i['tag'])
            if len(i['tra_loi']) != 0:
                print(random.choice(i['tra_loi']))
            break
def welcome(name):
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        print(f"Buổi sáng tốt lành, {name} ")
    elif hour >= 12 and hour < 18:
        print(f"Chào buổi chiều,{name} ")
    elif hour >= 18 or hour<6:
        print(f"Chào buổi tối,{name} ")
    print("Tôi là trợ lý ảo P-BOT.\nTôi có thể giải đáp các thắc mắc của bạn liên quan tới Học viện Công nghệ Bưu chính Viễn thông PTIT\nBạn có câu hỏi gì cần giải đáp không!")

if __name__ == "__main__":
    with open("DSSV.csv", mode="r", encoding="utf-8-sig") as file:
        header = file.readline()
        data_sv = file.readlines()


    def nhap_msv():
        msv = input("Để có thể bắt đầu xin hãy nhập Mã sinh viên của bạn: ").upper()
        msv = f'"{msv}"'
        for row in data_sv:
            row_list = row.split(",")
            check_msv = row_list[1]
            if msv == check_msv:
                return f'{row_list[2][1:-1]} {row_list[3][1:-1]}'
        return None


    name = nhap_msv()
    while name is None:
        print('Không tìm thấy sinh viên với MSV đã nhập. Xin hãy nhập lại.')
        name = nhap_msv()
    welcome(name)
    while True:
        message=input("")
        ints=predict_class(message)
        get_response(ints,data,message)


