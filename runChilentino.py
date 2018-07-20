
def init_auth():
    print("todo procedure: 1.get vin key")
    print("todo procedure: 2.check connector id")
    print("todo authorization/authontication throught server")
    return True

def init_configuration():
    print("todo load system configuration")
    print("todo load last session configuration, load last profile to check whether all tasks had been completed.")
    return True

def run_diagnostics(authSettings,os_Configuration):   
    print("todo connect to elm327")
    print("todo handle_osConfiguration")
    print("todo run_commands_in_elm327")
    print("todo hadle_commands_send_toserver_logging")

state_1=init_auth()
state_2=init_configuration()
run_diagnostics("{vin:1231223123,user:qqq-www-eee}","{conf:}")
