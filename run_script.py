#import telg as te
import heroku_deploy as hd

TOKEN              = '1403865219:AAHju1lmn-faKj4u3c8tN3GsYpPY33unuHI'
heroku_app_name    = "botnew123"
start_msg          = "hi welcome you can start giving the input..."

obj = hd.telegram(TOKEN,heroku_app_name,start_msg)
obj.main()
