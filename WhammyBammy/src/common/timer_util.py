from PyQt4.QtCore import QTimer, QObject, SIGNAL

class TimerUtil(object):

    @classmethod
    def create_timer(cls, call_me):
        timer = QTimer()
        QObject.connect(timer, SIGNAL("timeout()"), call_me)
        return timer

    @classmethod
    def start_timer(cls, call_me, time):
        timer = QTimer()
        QObject.connect(timer, SIGNAL("timeout()"), call_me)
        timer.start(time)
        return timer
    
    @classmethod
    def start_single_shot(cls, time, call_me):
        QTimer.singleShot(time, call_me)