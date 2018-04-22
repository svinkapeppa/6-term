class Logger(object):
    __instance = None

    def __new__(cls):
        if Logger.__instance is None:
            Logger.__instance = object.__new__(cls)
        return Logger.__instance

    @staticmethod
    def error(msg):
        print('Error: {}'.format(msg))
        exit(42)

    @staticmethod
    def warning(msg):
        print('Warning: {}'.format(msg))
