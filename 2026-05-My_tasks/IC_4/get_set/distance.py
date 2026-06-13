class Distance:
    def __init__(self, kilometers):
        self.kilometers = kilometers

    @property
    def kilometers(self):
        return self._kilometers

    @kilometers.setter
    def kilometers(self, new_kilometers):
        if new_kilometers < 0:
            raise ValueError("Kilometers cannot be negative")
        self._kilometers = new_kilometers

    @property
    def miles(self):
        return self.kilometers / 1.60934

    @miles.setter
    def miles(self, new_miles):
        if new_miles < 0:
            raise ValueError("Miles cannot be negative")
        else:
            new_kilometers = new_miles * 1.60934
            self.kilometers = new_kilometers


d = Distance(10)

print(d.kilometers)
print(d.miles)

d.miles = 1

print(d.kilometers)
print(d.miles)
