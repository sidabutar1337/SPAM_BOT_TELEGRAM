import time
import requests

class zeussec:
    def __init__(self,token,chat_id,message):
        self.token = token
        self.chat_id = chat_id
        self.message = message
class attack(zeussec):
    def spam(self):
        self.url = f'https://api.telegram.org/bot{self.token}/SendMessage' 
        self.data = {'chat_id':self.chat_id,'text':self.message}
        self.response = requests.post(self.url,json=self.data)
        if self.response.status_code == 200:
            return self.response.json()
        else:
            return f'bot mungkin sudah mati!!{self.response.json()}'
if __name__=='__main__':
    try:
        print('##########################')
        print('|  SPAMMER BOT TELEGRAM  |')
        print('##########################')
        print('|AUTHOR:ZEUSSEC1337      |')
        print('|GITHUB:SIDABUTAR1337    |')
        print('##########################')
        token1 = input('input token: ')
        cht_id = int(input('input chat id: '))
        mssg = input('pesan untuk penipu: ')
        max_spam = int(input('mau spam berapa kali? '))
        sidabutar = attack(token1,cht_id,mssg)
        count = 0
        time.sleep(2)
        while count <  max_spam:
            print(sidabutar.spam())
            count+=1
    except ValueError:
        print('value error!!') 
