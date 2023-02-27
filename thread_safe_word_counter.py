import threading


class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.object_level_counter = {}

    def process_text(self, text):
        self.split_list = text.split(" ")

    def get_word_count(self, word):
        self.lock.acquire()
        self.counter = 0
        for each_word in self.split_list:
            if each_word == word:
                self.counter += 1
        self.lock.release()
        self._update_counter(word) 
        return self.counter
    
    def _update_counter(self, word):
        self.lock.acquire()
        self.object_level_counter[word] = self.object_level_counter.get(word, 0) + 1
        self.lock.release()


wc = WordCounter()
wc.process_text("the cat is in the bag")
print(wc.get_word_count("the"))
print(wc.get_word_count("bag"))
print(wc.get_word_count("dog"))
