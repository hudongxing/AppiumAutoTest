import requests


def getToken():
    url = "http://home.uni-cocloud.com:5080/smarthome/index.php/base/Login/login"
    data = {
        "userName": "18801184375",
        "userPasswd": "68cf63c62bc68d71fc41c028375e2f6e"
    }
    r = requests.post(url, data)
    token = r.json().get("obj").get("token")
    # print(r.text)
    return token

def getShortList(name):
    url = "http://home.uni-cocloud.com:5080/smarthome/index.php/base/Home/shortcutList"
    token = getToken()
    data = {"type": "1", "token": token}
    r = requests.post(url, data)
    list = r.json().get("list")
    for i in list:
        if i.get("shortcut_name") == name:
            return True
    return False

def getAplist():
    url = "http://home.uni-cocloud.com:5080/smarthome/index.php/router/Ap/all"
    token = getToken()
    data = {"token": token}
    r = requests.post(url, data)
    list = r.json().get("list")
    for i in list:
        if i.get("online_stat") == 1:
            return i.get("index")

def getACstorage():
    url = "http://home.uni-cocloud.com:5080/smarthome/index.php/router/Ac/storage"
    token = getToken()
    data = {"token": token}
    r = requests.post(url, data)
    free_space = r.json().get("obj").get("free_space")
    return free_space


if __name__ == "__main__":
    getToken()
    # getShortList()
