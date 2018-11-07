class Codec:
    
    def __init__(self):
        self.url_dict = {}
        self.short_url_set = set()
        self.char_set = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while True:
            short_url = ''
            for i in range(6):
                short_url += self.char_set[random.randint(0, len(self.char_set) - 1)]
            if short_url not in self.short_url_set:
                self.url_dict[short_url] = longUrl
                self.short_url_set.add(short_url)
                return short_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url_dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))