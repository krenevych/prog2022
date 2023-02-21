class Program:
    def run(self):
        print("Програма запускається")


class Computer:
    def __init__(self):
        self.programList = []

    def instalProgram(self, p: Program):
        self.programList.append(p)

    def runAllProgram(self):
        for p in self.programList:
            p.run()


if __name__ == '__main__':

    prog = Program()
    comp = Computer()

    comp.runAllProgram()

