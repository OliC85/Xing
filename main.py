from XASession.Login import Login
from XASession.Account import Account

if __name__ == "__main__":
    id = ""
    pwd = ""
    cert_pwd = ""
    login = Login.get_instance()
    login.api_login(id, pwd, cert_pwd)

    if login.login_state == 1:
        account = Account.get_instance()
        account.account_info()
    print("------END--")
