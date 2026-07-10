class Codec:
    def __init__(self):
        self.url_map = {}
        self.counter = 0
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl):
        self.counter += 1
        short_url = self.base_url + str(self.counter)
        self.url_map[short_url] = longUrl
        return short_url

    def decode(self, shortUrl):
        return self.url_map[shortUrl]