import math
import matrix
import excel_transfer


class Givensrotation:
    def __init__(self):
        self.am = matrix.Matrix([], "Initial matrix")
        self.im = matrix.Matrix([], "I-matrix")
        self.qm = matrix.Matrix([], "Q-matrix")
        self.qmt = matrix.Matrix([], "Q\u0022-matrix")
        self.rm = matrix.Matrix([], "R-matrix")
        self.gm = matrix.Matrix([], "G-matrix")
        self.um = matrix.Matrix([], "U-matrix")
        self.dv = matrix.Vector([], "Vector B")
        self.q0 = []
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

    def gershgorin(self):
        R = []
        pair = []
        sum = 0
        for i in range(0, self.am.len[0]):
            for j in range(0, self.am.len[1]):
                if (i != j):
                    sum = sum + self.am.getel(i, j)
                    pass
            R.append(sum)
            sum = 0
            pass

        for i in range(0, len(R)):
            a = self.am.getel(i, i) + R[i]
            b = self.am.getel(i, i) - R[i]
            pair.append([a, b])
            pass

        pass

    def makec(self, i, k):
        c = self.um.getel(i, i) / math.sqrt(math.pow(self.um.getel(i, i), 2) + math.pow(self.um.getel(k, i), 2))
        return c
        pass

    def makes(self, i, k):
        s = self.um.getel(k, i) / math.sqrt(math.pow(self.um.getel(i, i), 2) + math.pow(self.um.getel(k, i), 2))
        return s
        pass

    def makecnew(self, R, i, k):
        c = R.getel(i, i) / math.sqrt(math.pow(R.getel(i, i), 2) + math.pow(R.getel(k, i), 2))
        return c
        pass

    def makesnew(self, R, i, k):
        s = R.getel(k, i) / math.sqrt(math.pow(R.getel(i, i), 2) + math.pow(R.getel(k, i), 2))
        return s
        pass

    def setqmatrix(self, Q, T):
        matrixname = Q.name
        if (Q.len[0] == 0):
            Q = T.copy()
        else:
            Q = Q.matrixm(T, self.accuracy)
            pass
        Q.rename(matrixname)
        return Q
        pass

    def maket(self, H, i, j):
        T = matrix.Matrix([], "T-matrix")
        T.makedimatrix(self.am.len[0])
        T.chel(i, i, self.makecnew(H, i, j))
        T.chel(j, j, self.makecnew(H, i, j))
        T.chel(i, j, -self.makesnew(H, i, j))
        T.chel(j, i, self.makesnew(H, i, j))
        T.showmatrix()
        return T
        pass

    def hmaket(self, H, j, i):
        T = matrix.Matrix([], "T-matrix")
        T.makedimatrix(self.am.len[0])
        print("j: ", j, "i: ", i)
        s = self.hmakes(H, j, i)
        c = self.hmakec(H, j, i)
        T.chel(j, j, c)
        T.chel(i, i, c)
        T.chel(j, i, -s)
        T.chel(i, j, s)
        return T

    def hmakes(self, H, j, i):
        aij = H.getel(i, j - 1)
        ajj = H.getel(j - 1, j)
        s = round(aij / math.sqrt(math.pow(ajj, 2) + math.pow(aij, 2)), self.accuracy)
        if math.fabs(s) < 1 / (10 ** self.accuracy):
            s = 0
        print("S=",s," is", aij, "/((", ajj, ")^2 + (", aij, ")^2)^(1/2)")
        print("i: ", i, "j: ", j - 1, "l: ", j)
        return s
        pass

    def hmakec(self, H, j, i):
        aij = H.getel(i, j - 1)
        ajj = H.getel(j - 1, j)
        c = round(ajj / math.sqrt(math.pow(ajj, 2) + math.pow(aij, 2)), self.accuracy)
        if math.fabs(c) < 1 / (10 ** self.accuracy):
            c = 0
        print("C=",c," is", ajj, "/((", ajj, ")^2 + (", aij, ")^2)^(1/2)")
        print("i: ", i, "j: ", j - 1, "l: ", j)
        return c
        pass

    def lowzeroing(self, A):
        print("Low zeroing (step when matrix transformed into upper triangular form)")
        H = matrix.Matrix(A.matrix, "H-matrix")
        self.qm.makedimatrix(A.len[0])
        i = 0
        while i < H.len[0]:
            j = i + 1
            while j < H.len[0]:
                T = matrix.Matrix([], "T-matrix")
                #print("i: ", i, " j: ", j)
                c = self.makecnew(H, i, j)
                s = self.makesnew(H, i, j)
                T.makedimatrix(A.len[0])

                T.chel(i, i, c)
                T.chel(j, j, c)
                T.chel(i, j, -s)
                T.chel(j, i, s)

                print("i: ",i + 1, "j: ",j + 1)
                print("S=", s, " is", H.getel(j,i), "/((", H.getel(i,i), ")^2 + (", H.getel(j,i), ")^2)^(1/2)")
                print("C=", c, " is", H.getel(i, i), "/((", H.getel(i, i), ")^2 + (", H.getel(j, i), ")^2)^(1/2)")
                print("Ok so we hawe Givense matrix... and it is allready transposed")
                T.showmatrix()

                self.q0.append(T)

                row = H.getrow(i)
                # step 1
                v1 = H.getrow(i)
                v2 = H.getrow(j)
                v1.mnumber(c, self.accuracy)
                v2.mnumber(s, self.accuracy)
                H.setrowm(i, v1.rowsummarize(v2, self.accuracy))
                # H.showmatrix()
                # step 2
                v1 = row.copy()
                v2 = H.getrow(j)
                v1.mnumber(-s, self.accuracy)
                v2.mnumber(c, self.accuracy)
                H.setrowm(j, v1.rowsummarize(v2, self.accuracy))
                H.showmatrix()
                j += 1
            i += 1
        print("End of II-part step")
        return H
    def uhessenberg(self, A):
        print("I-part Hessenberg matrix.")
        H = matrix.Matrix(A.matrix, "H-matrix")
        H0 = H.copy()
        H0.rename("H0-matrix")
        Q = matrix.Matrix([], "Q-matrix")
        Q.makedimatrix(H.len[0])
        i = 2
        while i < H.len[0]:
            j = 0
            while j < i - 1:
                l = j + 1
                print("print i: ", i + 1, "print j: ", j + 1, "(j-1) is l = j+1 = ", l + 1)
                T = self.hmaket(H, l, i)
                print("We have T-matrix")
                T.showmatrix()
                T.transpose()
                H = T.matrixm(H, self.accuracy)
                H.chel(i, j, 0)
                T.transpose()
                H.showmatrix()
                print("New look of H-matrix after multiplication: T-transposed * H")
                #H0 = H.copy()
                H = H.matrixm(T, self.accuracy)
                #H.chel(i, j, 0)
                print("New look of H-matrix after multiplication:  H * T")
                H.showmatrix()
                j += 1
            i += 1
        print("End of I-part step")
        return H

    def ugivencerot(self, A):
        print("Givens")
        H = matrix.Matrix(A.matrix, "H-matrix")
        j = 0
        while j < H.len[0]:
            i = j + 1
            while i < H.len[0]:
                print(i, j)
                T = self.maket(H, i, j)
                H = T.matrixm(H, self.accuracy)
                H.showmatrix()
                i += 1
            j += 1
        return H
        pass

    def resolve(self):
        self.am.showmatrix()
        i = 0
        H = matrix.Matrix(self.am.matrix, "H-matrix")
        H = self.uhessenberg(H)
        print("II-part QR-factorization")
        H.showmatrix()
        while i < 100:
            print("Step----->", i + 1)
            R = self.lowzeroing(H)
            self.makeqm()
            print("New look of Q-matrix after multiplication:  Q * T")
            self.qm.showmatrix()
            H.showmatrix()
            H = R.matrixm(self.qm, self.accuracy)
            H.showmatrix()
            i += 1

    def resolve0(self):
        self.am.showmatrix()
        i = 0
        H = matrix.Matrix(self.am.matrix, "H-matrix")
        H = self.uhessenberg(H)

        H.showmatrix()
        while i < 100:
            print(i, "----->")
            H = self.ugivencerot(H)
            self.makeqm()
            self.qm.showmatrix()
            H.showmatrix()
            self.qm.transpose()
            H = self.qm.matrixm(H, self.accuracy)
            H.showmatrix()
            i += 1
    def makeqm(self):
        while len(self.q0) > 0:
            T = self.q0.pop()
            self.qm = self.qm.matrixm(T, self.accuracy)
