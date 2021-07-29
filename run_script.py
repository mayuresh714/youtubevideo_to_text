import telg as te

TOKEN              = '1403865219:AAHju1lmn-faKj4u3c8tN3GsYpPY33unuHI'
heroku_app_name    = "newtelebot"
start_msg          = "hi welcome you can start giving the input..."

obj = te.telegram(TOKEN,heroku_app_name)
obj.main()