import json

path = "C:\\Users\\nikita\\Desktop\\save\\PyLol\\TimeTable11A\\data"

"""
string_f = open( f"{path}\\string_data\\day_names.json" )
strings_dict = json.load( string_f )
string_f.close()
del string_f

fizmat_schedule = []
himbio_schedule = []

with open( f"{path}\\shedules\\pnsr", 'r', encoding='utf-8' ) as sf :
    

    for c, s_l in enumerate( sf ):

        if (c+1)%2 == 1 :
            line_data = s_l[:-1:].split('/')

            if len(line_data)==1:
                line_data.append(line_data[0])
            
            fizmat_schedule.append({
                "lesson_name": line_data[0]
            })
            himbio_schedule.append({
                "lesson_name": line_data[1]
            })
sf.close()
del sf
pass   


#fizmat
lessons_by_days = [
    7,
    6,
    7,
    6,
    6
]

fs = []
for day_n, ld in enumerate( lessons_by_days ):
    fs.append( fizmat_schedule[:ld:] ) 
    fs[-1].insert( 0, strings_dict["en"][day_n])
    fizmat_schedule = fizmat_schedule[ld::]


fm_sh_dict = {
    "schedule":fs
}

with open( f"{path}\\shedules\\11A_fizmat\\11a_fizmat.json", 'w', encoding='utf-8' ) as fizmat_sh_file:
    json.dump( fm_sh_dict, fizmat_sh_file, ensure_ascii=False, indent=4 )
"""


"""#himbio
    
fizmat_schedule = himbio_schedule    

lessons_by_days = [
    7,
    6,
    7,
    6,
    6
]

fs = []
for day_n, ld in enumerate( lessons_by_days ):
    fs.append( fizmat_schedule[:ld:] ) 
    fs[-1].insert( 0, strings_dict["en"][day_n])
    fizmat_schedule = fizmat_schedule[ld::]


fm_sh_dict = {
    "schedule":fs
}

with open( f"{path}\\shedules\\11A_himbio\\11a_himbio.json", 'w', encoding='utf-8' ) as fizmat_sh_file:
    json.dump( fm_sh_dict, fizmat_sh_file, ensure_ascii=False, indent=4 )"""

if True:
    with open( f"{path}\\schedules\\11A_fizmat\\11a_fizmat.json", 'r', encoding='utf-8' ) as fizmat_sh_file:
        sh_json = json.load( fizmat_sh_file )

    print(type(sh_json))    

    for day in range(0, len(sh_json["schedule"])):
        """start_time = "8:00"
        for les in range( 1, len( sh_json["schedule"][day][1::] )+1 ):
            
            if sh_json["schedule"][day][les].get("start_time", None) == None:
                sh_json["schedule"][day][les]["start_time"]   =   f"{int(start_time.split(':')[0]) + les-1}:{start_time.split(':')[1]}"
                sh_json["schedule"][day][les]["finish_time"]  =   f"{int(start_time.split(':')[0]) + les-1  }:{ str((int(start_time.split(':')[1])+45) % 60).rjust(2,'0') }" """

        """sh_json["schedule"][day][0] = {
            "day_name": sh_json["schedule"][day][0]
        }"""

        sh_json["schedule"][day][0] = sh_json["schedule"][day][0]
        

    #print( sh_json )
    with open( f"{path}\\schedules\\11A_fizmat\\11a_fizmat.json", 'w', encoding='utf-8' ) as fizmat_sh_file:
        json.dump( sh_json, fizmat_sh_file, ensure_ascii=False, indent=4 )