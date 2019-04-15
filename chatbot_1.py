# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.decorators import channel
from bothub_client.messages import Message

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
        #self.send_message('Echo: {}'.format(event['content']))

        ontent = event['content']

        if content =='사용법':
          self.chatbot_text(event)
        else:
          self.search_word(event)

    def chatbot_text(self, event):
      message = "안녕하세요, 영어 사전 챗봇입니다.\n 알고싶은 영어 단어를 입력하면 네이버 사전으로 이동합니다."
      self.send_message(message)

    def search_word(self, event):
      content = event['content']
      url='https://endic.naver.com/search.nhn?sLn=kr&isOnlyViewEE=N&query={}'.format(content)
      message = Message(event).set_text(content + '네이버 사전')\
                              .add_url_button('{}'.format(content),url)
      self.send_message(message)