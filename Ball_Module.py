class Ball:
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coords = self.canvas.coords(self.image)
        if (coords[2] >= (self.canvas.winfo_width()) or coords[0] < 0):
            self.xVelocity *= -1
        if (coords[3] >= (self.canvas.winfo_height()) or coords[1] < 0):
            self.yVelocity *= -1
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)