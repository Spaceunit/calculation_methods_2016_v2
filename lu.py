import math
import matrix
class LU:
    def __init__(self):
        self.accuracy = 2
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

    def setlu(self):
        #self.numberconversion(0)
        #self.rawsubtract(0)
        self.lm.makedimatrix(self.um.len[0])
        for row in range(0,self.um.len[0]):
            #self.numberconversion(row)
            self.rawsubtract(row)
            pass
        pass

    def numberconversion(self, row):
        print('')
        print("Number conversion...")
        num = self.um.getel(row, row)
        print("R", row + 1, "/", num, ";")
        for i in range (row, self.um.len[0]):
            print("Step #",i + 1)
            self.um.chel(row, i, round(self.um.getel(row, i) / num, self.accuracy))
            self.um.showmatrix()
        print('End of number conversion')
        pass

    def rawsubtract(self, row):
        print('')
        print("Row subtract...")
        print("Step#", row + 1, ";")
        for k in range(row + 1, self.um.len[0]):
            print("R", k + 1, "- R", k, "*", "R(", k + 1, ",", row + 1, ")")
            if math.copysign(1, self.um.getel(row, row)) == math.copysign(1, self.um.getel(k, row)):
                self.lm.chel(k, row, round(self.um.getel(k, row) / self.um.getel(row, row), self.accuracy))
                pass
            else:
                self.lm.chel(k, row, round(-1 * self.um.getel(k, row) / self.um.getel(row, row), self.accuracy))
                pass
            #self.lm.chel(k,row,self.um.getel(k,row) / self.um.getel(row,row))
            #self.lm.chel(k,row,self.um.getel(k,row))
            self.um.chel(k, row, 0)
            for j in range(row + 1, self.um.len[0]):
                print("Step #", j + 1)
                self.um.chel(k, j, round(self.um.getel(k,j) - self.um.getel(row, j) * self.lm.getel(k, row), self.accuracy))
                self.um.showmatrix()
                self.lm.showmatrix()
                pass
        print('End of row subtract')
        pass

    def getdet(self):
        result = 1
        for i in range(0,self.um.len[0]):
            result *= self.um.getel(i,i) * self.lm.getel(i,i)
            #print(self.um.getel(i,i),self.lm.getel(i,i),result)
        result = round(result, self.accuracy)
        return result

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

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("LU factorization v0.0002 betta")
            print('')
            task = self.enterCommand()
            if (task == 2):
                self.dostaff()
            elif (task == 3):
                pass
            elif (task == 4):
                self.showHelp()
            elif (task == 5):
                self.inputnewdata()
                pass
            elif (task == 6):
                self.am.showmatrix()
                pass
            elif (task == 8):
                self.setaccuracy()
                pass
            elif (task == 9):
                self.makedafault()
                pass
            elif (task == 10):
                self.setlu()
                print("Determinant:")
                print(self.getdet())
                pass
            elif (task == 11):
                self.inputnewdata()
        pass

    def inputdata(self, arg,accuracy):
        self.accuracy = accuracy
        self.am = arg.copy()
        self.am.rename("Initial matrix")
        self.um = self.am.copy()
        self.um.rename("U-matrix")
        self.lm = matrix.Matrix([], "Lmatrix")
        self.am.showmatrix()
        pass

    def inputnewdata(self):
        task = 0
        self.am = matrix.Matrix([], "Initial matrix")
        self.lm = matrix.Matrix([], "Lmatrix")
        while (task != 1):
            print('')
            print("Enter matrix dimension:")
            while (task != 1):
                num = int(input("-> "))
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n"):
                    self.am = self.inputmatrix(num)
                    task = 1
            task = 0
            self.am.rename("Initial matrix")
            self.am.showmatrix()
            print("Matrix is correct? (enter - yes/n - no)")
            command = input("-> ")
            if (command != "n"):
                task = 1
        self.um = self.am.copy()
        self.um.rename("U-matrix")

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

    def showCommands(self):
        print('')
        print("Commands...")
        for item in self.commands:
            print(str(item) + ": " + str(self.commands[item]))

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

    def makedafault(self):
        self.am = matrix.Matrix([[3.81, 0.25, 1.28, 1.75],
                                [2.25, 1.32, 5.58, 0.49],
                                [5.31, 7.28, 0.98, 1.04],
                                [10.39, 2.45, 3.35, 2.28]],
                               "Initial matrix")
        self.um = self.am.copy()
        self.um.rename("U-matrix")
        self.lm = matrix.Matrix([], "Lmatrix")