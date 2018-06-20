import sys

class Game():
    def __init__(self):
        self.min = self.mid = self.max = 0

    def update_mid(self):
        sum = self.min + self.max
        if sum % 2 != 0:
            sum += 1
        self.mid = sum//2

    def check_range(self):
        if self.max == self.min:
            self.end(self.min)
        if self.max - self.min < 2:
            question = "Is your number {0}?".format(self.min)
            if self.yes(question):
                self.end(self.min)
            else:
                self.end(self.mid)

    def guess(self):
        question = ("Is your number in the inclusive range of {0} to {1}?"
                    .format(self.min, self.mid, self.max))
        if self.yes(question):
            self.max = self.mid
        else:
            self.min = self.mid + 1

    def setup(self):
        while self.min < 1:
            self.min = int(input("Enter min range (1 - INF): "))
        while self.max < self.min:
            self.max = int(input("Enter max range ({0} - INF): ".format(self.min)))

    def play(self):
        self.setup()
        while True:
            self.update_mid()
            self.check_range()
            self.guess()

    def yes(self, question):
        r = input(question)
        return (r.lower() == "yes" or r.lower() == "y")

    def end(self, number):
        print("Your number is {0}".format(number))
        sys.exit(0)

if __name__ == "__main__":
    g = Game()
    g.play()
