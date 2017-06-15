from urllib.request import urlopen
from html.parser import HTMLParser


class VPNParser(HTMLParser):
    auth = {"Username": None, "Password": None}

    def error(self, message):
        input("Error: " + message)

    def handle_data(self, data):
        for i in self.auth:
            if self.auth[i] is None and i in data:
                print(data)
                self.auth[i] = data.split(": ")[1] + '\n'

print("Connecting to vpnbook.com...")
try:
    parser = VPNParser()
    parser.feed(str(urlopen("http://www.vpnbook.com/").read()))
    open("vpnbook.txt", "w").writelines(parser.auth.values())
except Exception as error:
    print(error)
input()
