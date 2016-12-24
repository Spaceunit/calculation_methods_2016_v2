import math
import matrix
import excel_transfer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab


class LVE:
    def __init__(self):
        self.raw_data = {}
        self.result_data = {}
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
            "image 1": 11,
            "image 2": 12
        }


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

    #remake
    def inputnewdata0(self):
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

    def makedafault(self):
        print("Setting up data for task#15")
        self.raw_data = {'a': 1.77, 'b': 2.17, 'c': 1.38, 'd': 0.89, 'x0': 3.39, 'y0': 2.13, 't0': 15, 't1': 45}
        #self.raw_data = {'a': 1.89, 'b': 2.25, 'c': 1.49, 'd': 1.05, 'x0': 3.55, 'y0': 2.35, 't0': 18, 't1': 48}
        self.accuracy = 3
        self.print_raw_data()
        print("Accuracy of calculations:",(10**(-self.accuracy)))
        pass

    def importparam(self, accuracy):
        self.accuracy = accuracy

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
            else:
                if self.accuracy < 0:
                    print("Please enter positive number!")
                    task = 0
        pass

    def inputdata(self, data_name, data_type):
        task = 0
        input_type = int
        if data_type == "float":
            input_type = float
        elif data_type == "int":
            input_type = int
        else:
            print("Undefind type", data_type)
            task = 1
        if task == 0:
            print('')
            print("Enter ", data_name, ":")
            while (task != 1):
                value = input_type(input("-> "))
                print("Value", data_name, "is", value)
                print("Input is correct? (enter - yes/n - no)")
                command = input("-> ")
                if (command != "n"):
                    task = 1
            return value
        else:
            pass

    def inputnewdata(self):
        for value in ['a', 'b', 'c', 'd', 'x0', 'y0', 't0', 't1']:
            self.raw_data[value] = self.inputdata(value, 'float')

    def dostaff(self):
        task = 0
        while (task != 1):
            print('')
            print("Lotka–Volterra equations lab#4 v0.0002 betta")
            print('')
            task = self.enterCommand()
            if (task == 2):
                pass
            elif (task == 3):
                pass
            elif (task == 4):
                self.showHelp()
            elif (task == 5):
                self.inputnewdata()
                pass
            elif (task == 6):
                self.print_raw_data()
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
                self.printresult()

            elif (task == 12):
                self.printresult1()
        pass

    def print_raw_data(self):
        for value in ['a', 'b', 'c', 'd', 'x0', 'y0', 't0', 't1']:
            print("Value", value, "is", self.raw_data[value])

    @staticmethod
    def dx_dt_equation(a, b, x, y):
        return a * x - b * x * y

    @staticmethod
    def dy_dt_equation(c, d, x, y):
        return -c * y + d * x * y

    @staticmethod
    def pps(a, b, c, d, x, y):
        return (LVE.dx_dt_equation(a, b, x, y), LVE.dy_dt_equation(c, d, x, y))

    @staticmethod
    def t_step(t_array, h, i):
        t_array.append(t_array[i] + h)

    @staticmethod
    def y_step(y_array, k_array, i):
        y_array.append(y_array[i] + (k_array[0] + 2 * k_array[1] + 2 * k_array[2] + k_array[3]) / 6)

    @staticmethod
    def x_step(x_array, q_array, i):
        x_array.append(x_array[i] + (q_array[0] + 2 * q_array[1] + 2 * q_array[2] + q_array[3]) / 6)

    @staticmethod
    def make_kq_array(x_array, y_array, a, b, c, d, h, i):
        k_array = []
        q_array = []
        ppsp = LVE.pps(a, b, c, d, x_array[i], y_array[i])

        k_array.append(h * ppsp[1])
        q_array.append(h * ppsp[0])

        p_array = (1.0, 0.5, 0.5, 1)

        for j in [1, 2, 3]:
            x = x_array[i]
            y = y_array[i]

            x += q_array[j - 1] * p_array[j]
            y += k_array[j - 1] * p_array[j]

            ppsp = LVE.pps(a, b, c, d, x, y)

            k_array.append(h * ppsp[1])
            q_array.append(h * ppsp[0])

        return [k_array, q_array]

    @staticmethod
    def iteration(t_array, x_array, y_array, a, b, c, d, h, i):
        LVE.t_step(t_array, h, i)

        kq_array = LVE.make_kq_array(x_array, y_array, a, b, c, d, h, i)

        LVE.x_step(x_array, kq_array[1], i)
        LVE.y_step(y_array, kq_array[0], i)
        pass

    @staticmethod
    def iteration_demo(t_array, x_array, y_array, a, b, c, d, h, i):
        LVE.t_step(t_array, h, i)

        kq_array = LVE.make_kq_array(x_array, y_array, a, b, c, d, h, i)

        print("Factors k and q:")
        j = 0
        while j < len(kq_array[0]):
            print(j + 1, ") k:", kq_array[0][j], "; q:", kq_array[1][j])
            j += 1

        LVE.x_step(x_array, kq_array[1], i)
        LVE.y_step(y_array, kq_array[0], i)
        pass

    @staticmethod
    def check_h(epsilon, x0, y0, t0, a, b, c, d, h):
        an = True
        x1_array = []
        y1_array = []

        x2_array = []
        y2_array = []

        t1_array = []
        t2_array = []



        t1_array.append(t0)
        t2_array.append(t0)

        x1_array.append(x0)
        y1_array.append(y0)

        x2_array.append(x0)
        y2_array.append(y0)

        LVE.iteration_demo(t1_array, x1_array, y1_array, a, b, c, d, h, 0)

        LVE.iteration_demo(t2_array, x2_array, y2_array, a, b, c, d, h / 2, 0)
        LVE.iteration_demo(t2_array, x2_array, y2_array, a, b, c, d, h / 2, 1)

        num = 2**4 - 1
        r1 = abs((x1_array[1] - x2_array[2]) / num)
        r2 = abs((y1_array[1] - y2_array[2]) / num)
        print("x1 from h/2:", x2_array[1], "; y2 from h/2:", y2_array[1])
        print("R1 = |", x1_array[1], "-", x2_array[2], "| /", num, "=", r1)
        print("R2 = |", y1_array[1], "-", y2_array[2], "| /", num, "=", r2)
        r = max([r1, r2])
        print("R = max(", r1, ",", r2, ") =", r)

        if r >= epsilon:
            an = False
        else:
            an = True

        return an

    @staticmethod
    def auto_set_h(epsilon, x0, y0, t0, a, b, c, d, h):
        #h = epsilon ** 0.25
        an = False
        while an != True:
            an = LVE.check_h(epsilon, x0, y0, t0, a, b, c, d, h)
            h /= 2
            print("In autoset h is", h)


        return h

    def resolve(self):
        a = self.raw_data['a']
        b = self.raw_data['b']
        c = self.raw_data['c']
        d = self.raw_data['d']
        x0 = self.raw_data['x0']
        y0 = self.raw_data['y0']
        t0 = self.raw_data['t0']
        t1 = self.raw_data['t1']

        x_array = []
        y_array = []
        t_array = []

        x_array.append(x0)
        y_array.append(y0)
        t_array.append(t0)
        epsilon = 10 ** (-self.accuracy)
        h = epsilon ** 0.25

        print("R1 = |x(h) - x(h/2)|/(2 ** 4 - 1)")
        print("R1 = |y(h) - y(h/2)|/(2 ** 4 - 1)")
        print("R = max(R1, R2)")
        #h = 0.0005
        #an = LVE.check_h(epsilon, x0, y0, t0, a, b, c, d, h)
        h = LVE.auto_set_h(epsilon, x0, y0, t0, a, b, c, d, h)
        print("h is", h)
        i = 0

        while t_array[-1] <= t1:
            LVE.iteration(t_array, x_array, y_array, a, b, c, d, h, i)
            i += 1
        print("Final iteration number is:",i,"; (", x_array[-1], ";", y_array[-1], ")")
        print(max(x_array))
        print(max(y_array))
        print(min(x_array))
        print(min(y_array))
        j = 0
        #while j < len(x_array):
        #    print("Iteration number is:", j, "; (", x_array[j], ";", y_array[j], ")")
        #    j += 1

        self.result_data['x'] = x_array
        self.result_data['y'] = y_array
        self.result_data['t'] = t_array


    def printresult(self):
        plt.figure()
        #victim pray
        t = np.asarray(self.result_data['t'])
        y = np.asarray(self.result_data['y'])
        x = np.asarray(self.result_data['x'])
        #t = [0, 1, 2, 3, 4, 5]
        #y = [2, 4, 8, 9, 7, 3]
        #x = [1, 2, 6, 3, 4, 5]
        plt.plot(t, y, 'r-', label='Foxes', linewidth=2)
        #Predator
        plt.plot(t, x, 'b-', label='Rabbits', linewidth=2)
        plt.grid()
        plt.legend(loc='best')
        plt.xlabel('time')
        plt.ylabel('population')
        plt.title('Evolution of fox and rabbit populations')
        #plt.savefig('./rabbits_and_foxes_2.png')

        plt.show()
        plt.close()
        pass

    def printresult1(self):
        plt.figure()
        #victim pray
        t = np.asarray(self.result_data['t'])
        y = np.asarray(self.result_data['y'])
        x = np.asarray(self.result_data['x'])
        #t = [0, 1, 2, 3, 4, 5]
        #y = [2, 4, 8, 9, 7, 3]
        #x = [1, 2, 6, 3, 4, 5]
        #plt.plot(t, y, 'r-', label='Rabbits', linewidth=2)
        #Predator
        plt.plot(x, y, 'b-', label='Dependency', linewidth=2)
        plt.grid()
        plt.legend(loc='best')
        plt.xlabel('Foxes')
        plt.ylabel('Rabbits')
        plt.title('Evolution of fox and rabbit populations')
        #plt.savefig('./rabbits_and_foxes_2.png')

        plt.show()
        plt.close()
        pass
