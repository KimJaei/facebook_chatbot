# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.decorators import channel
from bothub_client.messages import Message
import requests
from bs4 import BeautifulSoup
import random


class Bot(BaseBot):
    """Represent a Bot logic which interacts with a user.

    BaseBot superclass have methods belows:

    * Send message
      * self.send_message(message, chat_id=None, channel=None)
    * Data Storage
      * self.set_project_data(data)
      * self.get_project_data()
      * self.set_user_data(data, user_id=None, channel=None)
      * self.get_user_data(user_id=None, channel=None)
    * Channel Handler
      from bothub_client.decorators import channel
      @channel('<channel_name>')
      def channel_handler(self, event, context):
        # Handle a specific channel message
    * Command Handler
      from bothub_client.decorators import command
      @command('<command_name>')
      def command_handler(self, event, context, args):
          # Handle a command('/<command_name>')
    * Intent Handler
      from bothub_client.decorators import intent
      @intent('<intent_id>')
      def intent_result_handler(self, event, context, answers):
          # Handle a intent result
          # answers is a dict and contains intent's input data
            {
              "<intent slot id>" : <entered slot value>
              ...
            }
    """
    @channel()
    def default_handler(self, event, context):
        """Handle a message received

        event is a dict and contains trigger info.

        {
           "trigger": "webhook",
           "channel": "<name>",
           "sender": {
              "id": "<chat_id>",
              "name": "<nickname>"
           },
           "content": "<message content>",
           "raw_data": <unmodified data itself webhook received>
        }
        """
        # self.send_message('Echo: {}'.format(event['content']))

        content = event['content']


        if content=='일상':
          self.chatbot_daily(event)
        elif content=='개그':
          self.chatbot_comic(event)
        elif content=='판타지':
          self.chatbot_fantasy(event)
        elif content=='액션':
          self.chatbot_action(event)
        elif content=='드라마': 
          self.chatbot_drama(event)
        elif content=='순정':
          self.chatbot_pure(event)
        elif content=='감성':
          self.chatbot_sensibility(event)
        elif content=='스릴러':
          self.chatbot_thrill(event)
        elif content=='시대극':
          self.chatbot_historical(event)
        elif content=='스포츠':
          self.chatbot_sports(event)
        elif content=='장르를 직접 선택할래!':
          self.chatbot_abc(event)
        elif content=='장르':
          self.chatbot_pick(event)
        elif content=='장르를 추천해줘!':
          self.chatbot_pick(event)
        elif content=='인기웹툰에서 추천해줘!':
          self.chatbot_time(event)
        elif content=='추천':
          self.chatbot_text(event)
        else:
          self.chatbot_text(event)

    def chatbot_pick(self, event):
      pick=['일상','개그','판타지','액션','드라마','순정','감성','스릴러','시대극','스포츠']
      pickpick=random.choice(pick)
      msg="오늘의 추천 장르는 ["+pickpick+"] 입니다."
      self.send_message(msg)
      message= pickpick+ "장르의 웹툰을 추천 받으시려면 "+pickpick+ " 버튼을 눌러주세요!"
      self.send_message(message)
      message2= "추천받은 장르가 마음에 드지않는다면 슬프지만 장르 버튼을 눌러 장르를 다시 추천받는 방법도 있습니당.. "
      self.send_message(message2)
      message3=Message(event).set_text("혹시 처음 선택페이지로 가시려면 추천을 눌러주세요!").add_quick_reply(pickpick).add_quick_reply('장르').add_quick_reply('추천')
      self.send_message(message3)

    def chatbot_text(self, event):
      message = "안녕하세요! 저는 그림그리기를 좋아하는 지구에요!\n무슨 웹툰을 볼까 고민될땐 저를 찾아주세요!"
      self.send_message(message)
      msg = Message(event).set_text('사용자님은 어떤 방법으로 웹툰을 추천받고싶으세요?').add_quick_reply('장르를 직접 선택할래!').add_quick_reply('장르를 추천해줘!').add_quick_reply('인기웹툰에서 추천해줘!')
      self.send_message(msg)

    def chatbot_abc(self, event):
      msg = Message(event).set_text('앗 그럼 원하시는 웹툰의 장르를 선택해주세요! 제가 추천해드릴게용').add_quick_reply('일상').add_quick_reply('개그').add_quick_reply('판타지').add_quick_reply('액션').add_quick_reply('드라마').add_quick_reply('순정').add_quick_reply('감성').add_quick_reply('스릴러').add_quick_reply('시대극').add_quick_reply('스포츠')
      self.send_message(msg)
    
    def chatbot_daily(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=daily'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      dailylist=[]
 
      for title in all_a:
        dailylist.append(title.text)
      
      message = "캐릭터들의 일상이 담겨있는 ["+random.choice(dailylist)+"]을 추천합니다!"
      self.send_message(message)
    
    def chatbot_comic(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=comic'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      comiclist=[]
 
      for title in all_a:
        comiclist.append(title.text)
      
      message = "썸네일만 봐도 재미있는 ["+random.choice(comiclist)+"]을 추천합니당!"
      self.send_message(message)

    def chatbot_fantasy(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=fantasy'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      fantasylist=[]
 
      for title in all_a:
        fantasylist.append(title.text)
      
      message = "개성넘치는 캐릭터들이 등장하는 ["+random.choice(fantasylist)+"]은 어떤가요??"
      self.send_message(message)

    def chatbot_action(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=action'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      actionlist=[]
 
      for title in all_a:
        actionlist.append(title.text)
      
      message = "얍얍! 보기만해도 액션감이 넘치는 ["+random.choice(actionlist)+"]을 추천합니다!"
      self.send_message(message)

    def chatbot_drama(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=drama'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      dramalist=[]
 
      for title in all_a:
        dramalist.append(title.text)
      
      message = "커쥬유마걸~ 드라마틱한 연출이 담겨있는 ["+random.choice(dramalist)+"]은 어떠세요?"
      self.send_message(message)

    def chatbot_pure(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=pure'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      purelist=[]
 
      for title in all_a:
        purelist.append(title.text)
      
      message = "보기만해도 설렘이 가득한 ["+random.choice(purelist)+"]을 추천합니당!"
      self.send_message(message)

    def chatbot_sensibility(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=sensibility'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      sensibilitylist=[]
 
      for title in all_a:
        sensibilitylist.append(title.text)
      
      message = "흑흑 ["+random.choice(sensibilitylist)+"]은 제가봐도 감성적이에요ㅠ 추천합니다!"
      self.send_message(message)

    def chatbot_thrill(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=thrill'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      thrilllist=[]
 
      for title in all_a:
        thrilllist.append(title.text)
      
      message = "커즈 쓰릴러~ 쓰릴러 나잇! ["+random.choice(thrilllist)+"]은 너무 스릴넘치는 웹툰이에요!."
      self.send_message(message)

    def chatbot_historical(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=historical'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      historicallist=[]
 
      for title in all_a:
        historicallist.append(title.text)
      
      message = "전하 소인이 감히 추천드리는 시대극 웹툰은 ["+random.choice(historicallist)+"]입니다!"
      self.send_message(message)

    def chatbot_sports(self, event):
      Tag = '#content > div.list_area > ul > li > dl > dt > a'
      URL= 'https://comic.naver.com/webtoon/genre.nhn?genre=sports'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      sportslist=[]
 
      for title in all_a:
        sportslist.append(title.text)
      
      message = "제가 추천하는 스포츠 웹툰은 보기만해도 운동한 것 같은 ["+random.choice(sportslist)+"]입니다!"
      self.send_message(message)

    def chatbot_time(self, event):
      Tag = '#realTimeRankFavorite > li > a'
      URL= 'https://comic.naver.com/webtoon/weekday.nhn'

      req = requests.get(URL)
      html = req.text
      soup = BeautifulSoup(html, 'html.parser') 

      all_a = soup.select(Tag)
      timelist=[]

      for title in all_a:
        timelist.append(title.text)

      po=random.choice(timelist)

      i=0
      j=[]

      while po[i]!='-':
        j.append(po[i])
        i=i+1
      
      self.send_message("앗! 실시간 인기 웹툰은 다 재미있는데...")
      ab="저는 그 중 ["+"".join(j)+"] 이 가장 재밌는거같아요!"
      self.send_message(ab)
