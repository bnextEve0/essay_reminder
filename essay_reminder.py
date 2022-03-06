import requests

def reminder():
    return '\n帶著碩一的初心,好好學習~\n在還有時間可以扎實學習的時間\n帶著實驗與探索知識的精神勇於嘗試吧:)'



def lineNotifyMessage():
    token = '54W204G9el9SbxO4o25Si0t70WU3jyGhRXZkYqxvcxD'
    msg = reminder()
    r = requests.post(url='https://notify-api.line.me/api/notify', headers={'Authorization': f'Bearer {token}'},data={'message':  msg  })
    return r.status_code

if __name__ == '__main__':
    lineNotifyMessage()
