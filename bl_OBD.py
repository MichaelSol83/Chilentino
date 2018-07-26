import obd


class Singleton:
    """ A python singleton """

    class __impl:
        __connection=None
        def connect_to_obd(self):
            self.__connection = obd.OBD()
            return self.__connection

        def run_query_speed(self):
            return self.__connection.query(obd.commands.SPEED)

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Singleton.__instance is None:
            # Create and remember instance
            Singleton.__instance = Singleton.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)


#print(Singleton().connect_to_obd());
#print(Singleton().run_query_speed());