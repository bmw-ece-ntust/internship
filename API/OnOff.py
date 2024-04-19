import requests
import urllib3
import keyring
import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IP_ADDR = "192.168.50.29"


class aosswitch:
    def __init__(self, ip=IP_ADDR, username="admin", port=10):
        self.session = requests.Session()
        self.ip = ip
        self.username = username
        self.url = "http://{}/rest/v4/".format(self.ip)
        self.cookie = self.login()
        self.headers = {"cookie": self.cookie}
        self.port = port
        
    def login(self):
        creds = {
            "userName": self.username,
            "password": keyring.get_password("3810", self.username),
        }
        response = requests.post(
            self.url + "login-sessions", json=creds, verify=False, timeout=10
        )
        cookie = {"cookie": response.json()["cookie"]}
        if response.status_code == 201:
            print("Login OK to ArubaOS-Swtich IP: {}".format(self.ip))
        else:
            print(
                "Login error to ArubaOS-Swtich IP: {}".format(
                    response.status_code
                )
            )
        return cookie
    
    def logout(self):
        response = requests.delete(
            self.url + "login-sessions",
            headers=self.cookie,
            verify=False,
            timeout=10,
        )
        print("Logout Status Code: {}".format(response.status_code))
    
    def getvlans(self):
        vlans = requests.get(
            self.url + "vlans", headers=self.cookie, verify=False, timeout=10
        )
        return vlans.json()
    
    def poe_off(self):
        call = requests.put(
            self.url + "ports/{}/poe".format(self.port),
            json={"is_poe_enabled": False},
            headers=self.cookie,
            verify=False, 
            timeout=10,
        )
        if call.status_code == 200:
            print("poe for port: {} off".format(self.port))
        else:
            print(
                "Something went wrong. Status code is {}".format(
                    call.status_code
                )
            )
            
    def poe_on(self):
        call = requests.put(
            self.url + "ports/{}/poe".format(self.port),
            json={"is_poe_enabled": True},
            headers=self.cookie,
            verify=False,
            timeout=10,
        )
        if call.status_code == 200:
            print("poe for port {} on".format(self.port))
        else:
            print(
                "Something went wrong. Status code: {}".format(
                    call.status_code
                )
            )