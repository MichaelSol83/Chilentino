import bl_OBD
import proxy


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


def testObd():
    print(bl_OBD.Singleton().connect_to_obd());
    print(bl_OBD.Singleton().run_query_speed());
    print(proxy.startTread_init_auth())

def poc_scenario():
    temp_id_connector="xxx-yyy-zzz";
   # vin=get_vin_from_obd()
   # is_client_auth=call_auth_https(temp_id_connector,vin)
   # speed_rate=get_speed_from_obd()
   # is_send_ok=update_server_with_speedrate(temp_id_connector,vin)




testObd()




