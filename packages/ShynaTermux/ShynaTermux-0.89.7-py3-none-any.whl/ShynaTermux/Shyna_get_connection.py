import os
import requests


class ShynaConnection:
    result = ""
    wifi_home_name = 'shivam'
    url = "https://shyna623.com/connection_check/set_new_connection/"

    def check_wifi(self):
        self.result = 'phone'
        new_dict = {}
        try:
            wifi_info = os.popen('termux-wifi-connectioninfo').read()
            if str(wifi_info).lower().__contains__(self.wifi_home_name):
                self.result = 'home'
            else:
                self.result = 'phone'
            new_dict.update(username='Shyna@623')
            new_dict.update(password=os.environ.get('password'))
            new_dict.update(result=self.result)
            self.result = requests.request("POST", self.url, data=new_dict)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    ShynaConnection().check_wifi()
