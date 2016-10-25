import math
import matrix
import excel_transfer
import Lab2.Lagrange.lagrange as lgr

class Aitkenscheme:
    def __init__(self):
        # For task v15:
        self.x = 0.0
        self.sta = 3
        self.a_matrix = matrix.Matrix([], "Initial matrix")
        self.sheet = matrix.Matrix([], "Result matrix")
        self.sheet_work = matrix.Matrix([], "Matrix in work")
        self.x_values = matrix.Vector([], "A bunch of x-values")
        self.y_values = matrix.Vector([], "A bunch of y-values")
        self.L = lgr.Lagrange()
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

    def makedafault_old(self):
        self.exeldata = excel_transfer.Excel()
        self.am = self.exeldata.transferlist('square')

    def makedafault(self):
        xk = [1.0, 1.08, 1.13, 1.20, 1.27, 1.31, 1.38]
        self.x_values.setvector(vector=xk)
        yk = [1.1752, 1.3025, 1.3863, 1.5095, 1.2173, 1.2236, 1.2347]
        self.y_values.setvector(vector=yk)
        self.x = 1.188

    def importparam(self, accuracy):
        self.accuracy = accuracy
        pass

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
            print("QR (Lab2) Aitken`s scheme method for function v0.0001 betta")
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
        self.x_values.showvector()
        self.y_values.showvector()

    def count_sheet_column(self, table_pos):
        values = [[0, 0], [0, 0]]
        result = [0] * table_pos
        self.L.set_x(self.x)
        N = self.x_values.len
        i = table_pos
        # With matrix
        while i < (N - 1):
            values[0][0] = self.sheet.getel(i, table_pos)
            values[0][1] = self.sheet.getel(i, table_pos)
            values[1][0] = self.sheet.getel(i + 1, table_pos)
            values[1][1] = self.sheet.getel(i + 1, table_pos)

            self.L.set_l(values=values)
            result.append()
            self.sheet_work.append_column()
            i += 1




        #self.l = (float(1) / float(1)) * self.m.getminor2(0, 0, vh_r=None)
        #self.L.set_l(values=[[A, B], [C, D]])
        return self.L.get_l()

    def prepare_sheet(self):
        N = self.x_values.len
        difference = [(self.x_values.vector[item] - self.x) for item in range(N)]
        self.sheet.appendnrow([i for i in range(N)])
        self.sheet.appendnrow(self.x_values.vector)
        self.sheet.appendnrow(self.y_values.vector)
        self.sheet.appendnrow(difference)

    def count_and_check(self):
        i = 0
        difference = self.accuracy * 2
        while difference >= self.accuracy:
            self.count_sheet_column(i)

    def count_row(self, i):
        pass