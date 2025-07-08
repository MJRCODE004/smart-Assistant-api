class Point:

    def draw(self):
        print("draw")

    def write(self):
        print("write")

point1 = Point()

point1.draw()


class Full:
    def insert(self):
        print("insert")

    def update(self):
        print("update")
f = Full()
f.insert()