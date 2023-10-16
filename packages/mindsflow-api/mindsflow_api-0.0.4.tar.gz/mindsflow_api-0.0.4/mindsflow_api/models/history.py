import redis


class History:
    unique_key: str = ""

    def __init__(self, unique_key: str = "", redis_url="redis://localhost:6379/0"):
        self.redis_url = redis_url
        self.unique_key = unique_key
        self.redis = redis.from_url(self.redis_url)

    def push(self, data):
        self.redis.lpush(self.unique_key, data)
        self.redis.ltrim(self.unique_key, 0, 9)

    def get_all(self):
        all_elements = self.redis.lrange(self.unique_key, 0, -1)
        all_elements = [element.decode() for element in all_elements]
        return all_elements

    def get(self, index=0):
        element = self.redis.lindex(self.unique_key, index)
        return element.decode()

    def compare(self, index1=-2, index2=-1):
        return self.get(index1) == self.get(index2)

