from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_map = defaultdict(OrderedDict)
        self.key_to_value = {}
        self.key_to_freq = defaultdict(int)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self.key_to_value:
            freq = self.key_to_freq[key]
            del self.freq_map[freq][key]
            if not self.freq_map[freq]:
                del self.freq_map[freq]
                if self.min_freq == freq:
                    self.min_freq += 1
            self.key_to_freq[key] += 1
            self.freq_map[self.key_to_freq[key]][key] = self.key_to_value[key]
            # print(self.key_to_value[key])
            return self.key_to_value[key]
        else:
            # print(-1)
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_value:
            self.key_to_value[key] = value
            freq = self.key_to_freq[key]
            del self.freq_map[freq][key]
            if not self.freq_map[freq]:
                del self.freq_map[freq]
                if self.min_freq == freq:
                    self.min_freq += 1
            self.key_to_freq[key] += 1
            self.freq_map[self.key_to_freq[key]][key] = value
            # print(self.key_to_value, len(self.key_to_value))
            return
        if len(self.key_to_value) == self.capacity:
            k, v = self.freq_map[self.min_freq].popitem(last=False)
            if not self.freq_map[self.min_freq]:
                del self.freq_map[self.min_freq]
            del self.key_to_freq[k]
            del self.key_to_value[k]
        self.key_to_value[key] = value
        self.key_to_freq[key] += 1
        self.freq_map[self.key_to_freq[key]][key] = value
        self.min_freq = 1
        # print(self.key_to_value, len(self.key_to_value))
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
