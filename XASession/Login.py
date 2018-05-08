# XASession/Login.py
import pythoncom

from XASession.EventHandler import EventHandler

class Login(EventHandler):
    def __init__(self):
        super().__init__()

    def OnLogin(self, code, msg):  # event handler
        if code == "0000":
            print("로그인 ok\n")
            self.login_state = 1
        else:
            self.login_state = 2
            print("로그인 fail.. \n code={0}, message={1}\n".format(code, msg))

    def api_login(self, id, pwd, cert_pwd): # id, 암호, 공인인증서 암호
        self.ConnectServer("hts.ebestsec.co.kr", 20001)
        is_connected = self.Login(id, pwd, cert_pwd, 0, False)  # 로그인 하기

        if not is_connected:  # 서버에 연결 안되거나, 전송 에러시
            print("로그인 서버 접속 실패... ")
            return

        while self.login_state == 0:
            pythoncom.PumpWaitingMessages()
