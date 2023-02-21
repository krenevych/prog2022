class Program:


    def run(self):
        print("Програма запускається")


class Computer:

    def runProgram(self, p: Program):
        print("Комп'ютер запускає програму...")
        p.run()


if __name__ == '__main__':

    prog = Program()
    comp = Computer()

    comp.runProgram(prog)

