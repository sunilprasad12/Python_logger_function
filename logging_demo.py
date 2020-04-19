import logging
from loggingpackage.custom_logger import custom_logger as cl

class LoggingDemo():

    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        m2Log = cl.customLogger(logging.INFO)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warn('warn message')
        m2Log.error('error message')
        m2Log.critical('critical message')

    def method3(self):
        m3log = cl.customLogger(logging.WARNING)
        m3log.debug('debug message')
        m3log.info('info message')
        m3log.warn('warn messages')
        m3log.error('error message')
        m3log.critical('critical messages')


demo = LoggingDemo()
demo.method1()
demo.method2()
demo.method3()
