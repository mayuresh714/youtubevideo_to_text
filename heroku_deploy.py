 
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT',5000))
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

 
class telegram():
    def __init__(self,TOKEN,heroku_app_name):
        self.TOKEN = TOKEN
        self.heroku_app_name = heroku_app_name

    def start(self,update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text(start_msg)

    def help(self,update, context):
        """Send a message when the command /help is issued."""
        update.message.reply_text('Help!')

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
            update.message.reply_text(pm[strt:])

    def error(update, context):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)

    def main(self):
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        updater = Updater(self.TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(CommandHandler("help", self.help))

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, self.response))

        # log all errors
        dp.add_error_handler(self.error)

        # Start the Bot
        updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=self.TOKEN)
        updater.bot.setWebhook('https://{}.herokuapp.com/'.format(self.heroku_app_name) + self.TOKEN)

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()

 