class Road:
    def __init__(self, l=1000, w=7):
        self._length = l
        self._width = w

    def tons(self):
        rez = self._width * self._length * 25 * 5 / 1000
        return rez, self._length, self._width


road1 = Road(5000, 20)
t, length, width = road1.tons()
print(f"На дорогу протяжённостью {length}м и шириной {width}м потребуется "
      f"{t:.0f}т асфальта(при условии толщины полотна в 5см).")
