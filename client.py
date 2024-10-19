import os
import json
import requests
import logging
import asyncio
import bs4
import sqlite3

import rubpy

class Client:
    def __init__(self,session: str,token: str):
        """
## Client
**session** : name of session

**token** : Token
        """
        self.session = session
        self.token = token
    def GetMe(self):
        getme_api = requests.post(f'https://eitaayar.ir/api/{self.token}/getMe')
        return getme_api.json()
    async def send_message(self,chat_id: int,message: str):
        pass
    def run(self):
        if self.session and self.token:
            if os.path.exists(f'{self.session}.session') == False:
                s = sqlite3.connect(f'{self.session}.session')
                c = s.cursor()
                c.execute(f'CREATE TABLE Bot (Token TEXT NOT NULL)')
                c.execute(f"INSERT INTO Bot VALUES ('{self.token}')")
                s.commit()
            asyncio.run(self.__start())
        else:
            return f"where is {self.session} or {self.token}?"
    async def __start(self):
        api = requests.post(f'https://eitaayar.ir/api/{self.token}')
        json_api = api.json()
        if json_api['description'] == 'Not Found: method not found!':
            pass
        else:
            print('NotFounded Token !') 
