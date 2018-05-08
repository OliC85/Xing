# XASession/Account.py
from XASession.EventHandler import EventHandler

class Account(EventHandler):
    def __init__(self):
        super().__init__()

    def account_info(self):
        account_no = self.GetAccountListCount()

        print("계좌 갯수 = {0}".format(account_no))

        for i in range(account_no):
            account = self.GetAccountList(i)
            print("계좌번호 = {0}".format(account))
