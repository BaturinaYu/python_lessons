import tkinter
import time


class TrafficLight:
    color = ['grey', 'red', 'yellow', 'green']

    def __running(self, long=2):
        root = tkinter.Tk()
        root.geometry('200x400+500+100')
        canvas = tkinter.Canvas(root, width=200, height=400, bg=self.color[0])
        canvas.pack()

        def paint_circle(root, canvas, x0, y0, color1, color2):
            canvas.create_oval(x0, y0, x0 + 100, y0 + 100, outline=color1, fill=color2)
            root.update()


        def miganie(root, canvas, x0, y0, color1, color2):
            for i in list(range(3)):
                paint_circle(root, canvas, x0, y0, color2, color2)
                time.sleep(0.5)
                paint_circle(root, canvas, x0, y0, color2, color1)
                time.sleep(0.5)
        for i in list(range(long)):
            """Красный горит 7 секунд"""
            paint_circle(root, canvas, 50, 50, self.color[1], self.color[1])
            paint_circle(root, canvas, 50, 150, self.color[2], self.color[0])
            paint_circle(root, canvas, 50, 250, self.color[3], self.color[0])
            time.sleep(7)
            """Мигает красный"""
            miganie(root, canvas, 50, 50, self.color[0], self.color[1])
            """Жёлтый горит 2 секунды"""
            paint_circle(root, canvas, 50, 50, self.color[1], self.color[0])
            paint_circle(root, canvas, 50, 150, self.color[2], self.color[2])
            paint_circle(root, canvas, 50, 250, self.color[3], self.color[0])
            time.sleep(2)
            """Мигает жёлтый"""
            miganie(root, canvas, 50, 150, self.color[0], self.color[2])
            """Зелёный горит 7 секунд"""
            paint_circle(root, canvas, 50, 50, self.color[1], self.color[0])
            paint_circle(root, canvas, 50, 150, self.color[2], self.color[0])
            paint_circle(root, canvas, 50, 250, self.color[3], self.color[3])
            time.sleep(7)
            """Мигает зелёный"""
            miganie(root, canvas, 50, 250, self.color[0], self.color[3])

tlight = TrafficLight()
tlight._TrafficLight__running()
