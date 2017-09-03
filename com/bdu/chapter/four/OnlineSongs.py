class OnlineSongs:
    x=0
    def __init__(self):
        print "I am constructor"

    def songs(self):
        self.x = self.x + 1

    def __del__(self):
        print "I am self destructed",self.x


a1 = OnlineSongs()
a1.songs()