import time
#import os

def log( string, end='\n', log_file_path="my_data", file_name ="log.txt",     lines_lim = 100 ):


    with open( fR"{log_file_path}\{file_name}", 'r+', encoding='utf-8' ) as f:
        

        lines = f.readlines()
        if len(lines) > lines_lim :
            dump_f = open( fR"""{log_file_path}\old_logs\dump{ int(lines[0]) }.txt""", 'w', encoding='utf-8' )
            dump_f.writelines( lines )
            dump_f.close()
            f.seek(0)
            #print(str( int(lines[0][:-1:])+1 ))
            f.write(str( int(lines[0][:-1:])+1 )+'\n')
        del lines


        t = time.localtime(time.time())

        f.write( f"{time.strftime('[%d.%m.%y %H:%M:%S]', t)}: {string}{end}" )
        f.truncate()
    f.close()
    #del f    #FIXME: should it be here?
