#first director of pokemon
import cranidos,geodude,onix
class Kangsuk:
    def __init__(self):
        self.name = '강석'
        self.director = []
        self.director.append(geodude.Geodude())
        self.director.append(onix.Onix())
        self.director.append(cranidos.Cranidos())
        [self.director[i].ability() for i in range(len(self.director))]