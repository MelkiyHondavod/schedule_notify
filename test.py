from custom_logging import log

def test_log( log_file_path="C:\\Users\\nikita\\Desktop\\save\\PyLol\\TimeTable11A\\data\\log.txt" ):
    test_string = "test log"
    log(f"\n{test_string}\n")

    with open( log_file_path, 'r', encoding='utf-8' ) as test_log_file:
        if test_log_file.readlines()[-1][:-1:] == test_string :
            return "ok"
        
    return "error"    


def test_all():
    print("testing...")
    print( "logging: ", test_log() )

if __name__=="__main__":
    test_all()