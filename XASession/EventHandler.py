# XASession/EventHandler.py
import win32com.client

class EventHandler:
    def __init__(self):
        self.login_state = 0

    @classmethod
    def get_instance(cls):
        xsession = win32com.client.DispatchWithEvents("XA_Session.XASession", cls)
        return xsession
