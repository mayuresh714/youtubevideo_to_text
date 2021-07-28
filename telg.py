import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from google_trans_new import google_translator
import process as pc

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
 
class telegram():
    def __init__(self,TOKEN):
        self.TOKEN = TOKEN
        
    def response(self,update, context):
        #print(update)
        try: 
          cust= update.message.chat.first_name + update.message.chat.last_name
        except:
          cust = update.message.chat.first_name  
 
        #pm = update.message.text 
        try:
            pm = pc.transcribe().sms_reply(update.message.text,cust)
        except:
            pm = "invalid link,plz provide the valid link for transcription."
        if type(pm) == list:
            #context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(r"{}".format(pm[0]),'rb'), caption=pm[1])
            context.bot.sendPhoto(chat_id=update.message.chat.id, photo = pm[0] , caption=pm[1])
        else:
            strt = 0
            for i in range(20,len(pm),1000):
                update.message.reply_text(pm[strt:i])
                strt = i

    def error(self,update, context):
        logger.warning('Update "%s" caused error "%s"', update, context.error)

    def main(self):
        updater = Updater(self.TOKEN, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(MessageHandler(Filters.text, self.response))
        updater.start_polling()
        updater.idle()
