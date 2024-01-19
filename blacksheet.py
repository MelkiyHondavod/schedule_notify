"""import time

def wait( formated_time ):

    wait_h, wait_m = tuple( map( int, formated_time.split(':') ) )
    t = time.localtime(time.time())

    while not t.tm_hour *100 + t.tm_min >=  wait_h*100 + wait_m :
        t = time.localtime(time.time())
        time.sleep( 1 )

    return    

formatted_time = "19:41"              
print(f"waiting for {formatted_time} ...")
wait(f"{formatted_time}")
print(f"hey it's {formatted_time}")              """



import telebot
def say( s, bot_token="6816430840:AAEG1RNdd4ay0GtNSxBc6dRV5_eh7vL2j4M" ):
    chanel_id = -1002056335596
    bot=telebot.TeleBot(bot_token)
    bot.send_message( chanel_id, text= s, timeout=None )   

say("hello")    