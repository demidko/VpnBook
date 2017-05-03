from urllib.request import urlopen
from html.parser import HTMLParser


class WebWriter(HTMLParser):
    def error(self, message):
        input("Error: " + message)

    def handle_data(self, data):
        for i in self.words:
            if not self.words[i] and i in data:
                print(data)
                self.words[i] = True

    def set_words(self, words):
        self.words = {i: False for i in words}
        return self

		
print("Connecting to https://vpnbook.com ...")
try:
    WebWriter().set_words(["Username", "Password"]).feed(str(urlopen("http://www.vpnbook.com/").read()))
except Exception as error:
    print(error)
input()
