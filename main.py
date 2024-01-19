import time
from custom_logging import log
import telebot
from project_path import ProjectPath as pp
import json


"""def say( s ):
    print(s)"""

def wait( formated_time ):

    wait_h, wait_m = tuple( map( int, formated_time.split(':') ) )
    t = time.localtime(time.time())

    while not t.tm_hour *100 + t.tm_min >=  wait_h*100 + wait_m :
        t = time.localtime(time.time())
        time.sleep( 1 )

    return    


def wait_day( wait_day ):

    t = time.localtime(time.time())

    while t.tm_wday < wait_day : #FIXME:  (  t.tm_wday < wait_day  ) --> (  t.tm_wday == wait_day  ) could be dangerous
        t = time.localtime(time.time())
        time.sleep(60)

    return


def say( s, bot_token="6816430840:AAEG1RNdd4ay0GtNSxBc6dRV5_eh7vL2j4M" ):

    chanel_id = -1002056335596
    dev_id = 931481755

    bot=telebot.TeleBot(bot_token)
    bot.send_message( dev_id, text= s, timeout=None )    



def day( schedule_dict, day_int ):#day( schedule_list, schedule_dict, day_int ):
    #queue = []
    schedule_list = schedule_dict[ "schedule" ][ day_int ]

    day_name = schedule_list[0]["day_name"]
    queue = schedule_list[1::]

    #compile schedule
    wait( "7:00" )

    """schedule_text = f"{day_name}\n"
    for l in queue:
        schedule_text += f"{l.get('start_time')} - {l.get('finish_time')}  {l.get('lesson_name')}\n"

    say( schedule_text[:-1:] )"""


    #queue
    run = True
    moment = False
    time_seconds_delay = 0

    while run and len(queue)>0:  

        time.sleep( time_seconds_delay )      

        if queue[0].get("finish_time", None) == None:
            queue.pop[0]
        else:
            #mom_h, mom_m = tuple( map( int, queue[0]["finish_time"].split(':') ) )
            prefire_minutes = 5
            if len(queue)==1:
                prefire_minutes = 0

            flt_l = tuple( map( int, queue[0]["finish_time"].split(':') ) )
            lesson_fTime = f"{ str(flt_l[0]) }:{ str(flt_l[1] - prefire_minutes) }"
            wait( formated_time = lesson_fTime )
            moment = True    
                

        if moment:
            log( f"{queue[0]['lesson_name']} finished") #ends

            if len(queue)==1:
                #time.sleep( prefire_minutes*60 )
                say("Уроки закончились, пиздуйте домой")

                #next day schedule
                schedule_text = f"next day({ schedule_dict['schedule'][ (day_int+1)%5 ][0].get('day_name') }) schedule\n"
                for l in schedule_dict["schedule"][ (day_int+1)%5 ][1::]:
                    schedule_text += f"{l.get('start_time')} - {l.get('finish_time')}  {l.get('lesson_name')}\n"

                say( schedule_text[:-1:] )

                print("day finished")
                run = False #FIXME: too much?
            else:
                say( f"next: {queue[1]['lesson_name']} at {queue[1]['start_time']}" )    

            #run = False
            queue.pop(0)
            moment = False


def week( start_week_day=1, finish_week_day=5 ):

    schedule_file = open( f"{pp.path}\\schedules\\11A_fizmat\\11a_fizmat.json", 'r', encoding='utf-8' )
    schedule_dict = json.load( schedule_file )
    schedule_file.close()

    for d in range(start_week_day-1,finish_week_day):
        #WARNING: d is real (starts from 0), but start(finish)_week_day is "human readable" starts from 1(monday)

        wait_day(d)
        print(f"day {d} started")
        log(f"day {d} started")        

        #monday_int = 0
        day_schedule_list = schedule_dict[ "schedule" ][ d ]

        log( day_schedule_list )

        day( schedule_dict, day_int=d ) #day( day_schedule_list, schedule_dict, day_int=d )



def monday():

    schedule_file = open( f"{pp.path}\\schedules\\11A_fizmat\\11a_fizmat.json", 'r', encoding='utf-8' )
    schedule_dict = json.load( schedule_file )
    schedule_file.close()

    monday_int = 0
    monday_schedule_list = schedule_dict[ "schedule" ][ monday_int ]

    log( monday_schedule_list )

    day( monday_schedule_list, day_int=monday_int )


def main():
    """time_delay = 0
    run = True
    while run:
        time.sleep(time_delay)
        monday_int = 0
        if time.localtime(time.time()).tm_wday == monday_int:
            print("monday just stared")
            run = False
    monday() """   
    while True:
        print("start week")
        week()


if __name__=="__main__":
    main()
