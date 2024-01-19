if False:
    import time

    class Lesson:
        def __init__(self, lesson_data ):#name, start_time, finish_time=None, place=None):
            self.name = lesson_data.get( "lesson_name", None )
            self.start_time = lesson_data.get( "start_time", None )
            self.finish_time = lesson_data.get( "finish_time", None )


    def say( speach ):
        print( speach )


    queue = [
        {
                    "lesson_name": "22:30",
                    "start_time": "22:30",
                    "finish_time": "8:45"
        },
        {
                    "lesson_name": "22:31",
                    "start_time": "22:31",
                    "finish_time": "8:45"
        },
        {
                    "lesson_name": "22:32",
                    "start_time": "22:32",
                    "finish_time": "8:45"
        }
    ]

    run = True
    moment = False
    while run and len(queue)>0:        

        if queue[0].get("finish_time", None) == None:
            queue.pop[0]
        else:
            mom_h, mom_m = tuple( map( int, queue[0]["finish_time"].split(':') ) )
            print(mom_h,mom_m)
            t = time.localtime(time.time())
            if t.tm_hour *100 + t.tm_min >  mom_h*100 + mom_m :#if t.tm_hour>=mom_h and t.tm_min>=mom_m :
                moment = True    
                

        if moment:
            #print(queue[0]["lesson_name"])

            if len(queue)==1:
                say("cograts")
            else:
                say( f"next: {queue[1]['lesson_name']} at {queue[1]['start_time']}" )    

            #run = False
            queue.pop(0)
            moment = False

import telebot


def say( s, bot_token="6816430840:AAEG1RNdd4ay0GtNSxBc6dRV5_eh7vL2j4M" ):
    bot=telebot.TeleBot(bot_token)
    bot.send_message( 931481755, text= s )

say("Hello world")                