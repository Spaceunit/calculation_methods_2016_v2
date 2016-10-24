import math
import matrix
import excel_transfer


class Aitkenscheme:
    def __init__(self):
        self.sta = 3
        self.a_matrix = matrix.Matrix([], "Initial matrix")
        self.commands = {
            "none": 0,
            "exit": 1,
            "test": 2,
            "clear": 3,
            "help": 4,
            "new": 5,
            "show slist": 6,
            "show scount": 7,
            "acc": 8,
            "mk": 9,
            "start": 10,
            "old": 11
        }

    def inputdata(self, accuracy):
        self.accuracy = accuracy

    def showCommands(self):
        print('')
        print("Commands...")
        for item in self.commands:
            print(str(item) + ": " + str(self.commands[item]))

    def enterCommand(self):
        command = "0"
        print('')
        print("Enter command (help for Q&A)")
        while (command not in self.commands):
            command = input("->")
            if (command not in self.commands):
                print("There is no such command")
            else:
                return self.commands[command]

    def showHelp(self):
        print('')
        print("Help v0.001")
        self.showCommands()

    def inputnewdata(self):
        task = 0
        self.am = matrix.Matrix([], "Initial matrix")
        while (task != 1):
            print('')
            print("Enter matrix dimension:")
            while (task != 1):
                num = int(input("-> "))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n"):
                    self.am = self.inputmatrix(num)
                    # self.dv = self.inputvector()
                    task = 1
            task = 0
            self.am.rename("Initial matrix")
            self.um = self.am.copy()
            self.um.rename("U-matrix")
            self.am.showmatrix()
            print("Our matrix with accuracy: 3")
            self.am.showmatrixaccuracy3()
            # self.dv.showvector()
            print("Matrix is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1

    def inputmatrix(self, num):
        print('')
        i = 0
        task = 0
        nm = matrix.Matrix([], "new matrix")
        while (i < num):
            print("Enter matrix row (use spaces)")
            print("Row ", i + 1)
            while (task != 1):
                row = list(map(float, input("-> ").split()))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n" and len(row) == num):
                    task = 1
                    nm.appendnrow(row)
                elif (len(row) != num):
                    print('')
                    print("Incorrect input: count of items.")
            task = 0
            i += 1
        return nm

    def inputvector(self):
        print('')
        i = 0
        task = 0
        num = self.am.len[0]
        print("Enter vector row (use spaces)")
        print("Row")
        while (task != 1):
            row = list(map(float, input("-> ").split()))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n" and len(row) == num):
                task = 1
                nm = matrix.Vector(row, "new vector")
            elif (len(row) != num):
                print('')
                print("Incorrect input: count of items.")
        return nm

    def setbettavector(self):
        self.btv = matrix.Vector([], "Betta-vector")
        for i in range(0, self.dv.len):
            self.btv.appendel(self.dv.getel(i) / self.am.getel(i, i))

    def somedata(self):
        self.am = matrix.Matrix([[10, 2, -1],
                                 [-2, -6, -1],
                                 [1, -3, 12]],
                                "Initial matrix")

        self.dv = matrix.Vector([5, 24.42, 36], "Vector B")

    def makedafault(self):
        self.exeldata = excel_transfer.Excel()
        self.am = self.exeldata.transferlist('square')

    def importparam(self, exmatrix, accuracy):
        self.accuracy = accuracy
        self.am = exmatrix.copy()
        self.am.rename('Initial matrix')
        self.um = self.am.copy()
        self.um.rename('U-matrix')
        self.im.makedimatrix(self.am.len[0])
        # self.qmt.makedimatrix(self.am.len[0])

    def setaccuracy(self):
        task = 0
        print('')
        print("Enter accuracy:")
        while (task != 1):
            self.accuracy = int(input("-> "))
            print("Input is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1
        pass

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("QR (Lab1) method for matrix v0.0002 betta")
            print('')
            task = self.enterCommand()
            if (task == 2):
                self.somedata()
                pass
            elif (task == 3):
                pass
            elif (task == 4):
                self.showHelp()
            elif (task == 5):
                self.inputnewdata()
                pass
            elif (task == 6):
                self.am.showmatrix()
                print("Our matrix with accuracy: 3")
                self.am.showmatrixaccuracy3()
                # self.dv.showvector()
                pass
            elif (task == 8):
                self.setaccuracy()
                pass
            elif (task == 9):
                self.makedafault()
                pass
            elif (task == 10):
                self.resolve()
                pass
            elif (task == 11):
                self.inputnewdata()
        pass

    def resolve(self):
        self.a_matrix.showmatrix()