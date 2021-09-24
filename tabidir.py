class TaBiDir:
    def __init__(self, g, d):
        if (not type(g) == "list" or not type(d) == "list"):
            raise ValueError
        self.__g = g
        self.__d = d
    
    def __str__(self):
        return str(self.__g + self.__d)

    def getitem(self, i):
        if i >= 0:
            return self.__d[i]
        else:
            return self.__g[i]

    def setitem(self, i, v):
        if i >= 0:
            self.__d[i] = v
        else:
            self.__g[i] = v

    def imin(self):
        return -len(self.__g)
    
    def imax(self):
        return len(self.__d)

    def append(self, v):
        self.__d.append(v)
    
    def prepend(self, v):
        self.__g.insert(0, v)
