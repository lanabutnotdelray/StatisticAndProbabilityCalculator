import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import probability


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("MATH FUNCTIONS")
        self.geometry("600x300")
        self.resizable(False, False)

        tab_control = ttk.Notebook(self)
        tab_control.pack(expand=1, fill="both")
        tab_control.add(ProbabilityFrame(tab_control), text='PROBABILITY')
        tab_control.add(StatisticFrame(tab_control), text='STATISTIC')


class ProbabilityFrame(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.new_p = probability.Probability()

        self.x_list = tk.StringVar()
        x = str(self.new_p.xlist).replace('[', '')
        x = x.replace(']', '')
        self.x_list.set(str(x))
        self.p_list = tk.StringVar()
        x = str(self.new_p.plist).replace('[', '')
        x = x.replace(']', '')
        self.p_list.set(x)

        self.m = tk.StringVar()
        self.m2 = tk.StringVar()
        self.d = tk.StringVar()
        self.s = tk.StringVar()

        self.x_value = tk.StringVar()
        self.x_value.set("X FOR SEARCH")
        self.pr = tk.StringVar()

        ttk.Label(self, text="Value list").grid(column=0, row=0, padx=5, pady=5)
        ttk.Label(self, text="Probability list").grid(column=0, row=1, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.x_list, width=15).grid(column=1, row=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.p_list, width=15).grid(column=1, row=1, padx=5, pady=5)
        ttk.Button(self, text="UPDATE", command=self.get_result).grid(column=0, row=3,
                                                                      columnspan=2,
                                                                      sticky="we",
                                                                      padx=5, pady=5)
        ttk.Label(self, textvariable=self.m).grid(column=0, row=4, columnspan=2,
                                                  sticky="we", padx=5)
        ttk.Label(self, textvariable=self.m2).grid(column=0, row=5, columnspan=2,
                                                   sticky="we", padx=5)
        ttk.Label(self, textvariable=self.d).grid(column=0, row=6, columnspan=2,
                                                  sticky="we", padx=5)
        ttk.Label(self, textvariable=self.s).grid(column=0, row=7, columnspan=2,
                                                  sticky="we", padx=5)
        ttk.Entry(self, textvariable=self.x_value, width=15).grid(column=4, row=0, padx=5, pady=5)
        ttk.Label(self, textvariable=self.pr).grid(column=4, row=1, columnspan=2,
                                                        sticky="we", padx=5)

    def get_result(self):
        try:
            l = self.x_list.get()
            l = l.replace(' ', ' ')
            l = l.replace('[', ' ')
            l = l.replace(']', ' ')
            l = newlistx = l.split(',')
            for elem in newlistx:
                newlistx[newlistx.index(elem)] = float(elem)

            l = self.p_list.get()
            l = l.replace(' ', ' ')
            l = l.replace('[', ' ')
            l = l.replace(']', ',')
            newlistp = l.split(',')
            for elem in newlistp:
                newlistp[newlistp.index(elem)] = float(elem)

            self.new_p.change_data(newlistx, newlistp)

            result = self.new_p.mathexpect()
            self.m.set(f"MATH EXPECTION: {result}")

            result = self.new_p.squaremathexpect()
            self.m2.set(f"MATH EXPECTION IN SQUARE: {result}")

            result = self.new_p.dispersion()
            self.d.set(f"DISPERSION: {result}")

            result = self.new_p.sigma()
            self.s.set(f"SIGMA: {result}")

            x = float(self.x_value.get())
            p = self.new_p.get_x_prabability(x)
            self.pr.set(f"PRABABILITY IS {p}")

        except Exception as error:
            showerror(title="Ошибка", message=str(error))


class StatisticFrame(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.new_p = probability.Statistic()

        self.x_list = tk.StringVar()
        x = str(self.new_p.xlist)
        x = x.replace('[', '')
        x = x.replace(']', '')
        self.x_list.set(str(x))
        self.p_list = tk.StringVar()
        x = str(self.new_p.nlist).replace('[', '')
        x = x.replace(']', '')
        self.p_list.set(x)

        self.m = tk.StringVar()
        self.m2 = tk.StringVar()
        self.d = tk.StringVar()
        self.s = tk.StringVar()
        self.f = tk.StringVar()

        self.x_value = tk.StringVar()
        self.x_value.set("X FOR SEARCH")
        self.n_times = tk.StringVar()

        ttk.Label(self, text="Value list").grid(column=0, row=0, padx=5, pady=5)
        ttk.Label(self, text="N list").grid(column=0, row=1, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.x_list, width=15).grid(column=1, row=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.p_list, width=15).grid(column=1, row=1, padx=5, pady=5)
        ttk.Button(self, text="UPDATE", command=self.get_result).grid(column=0, row=3,
                                                                      columnspan=2,
                                                                      sticky="we",
                                                                      padx=5, pady=5)
        ttk.Label(self, textvariable=self.m).grid(column=0, row=4, columnspan=2,
                                                  sticky="we", padx=5)
        ttk.Label(self, textvariable=self.m2).grid(column=0, row=5, columnspan=2,
                                                   sticky="we", padx=5)
        ttk.Label(self, textvariable=self.d).grid(column=0, row=6, columnspan=2,
                                                  sticky="we", padx=5)
        ttk.Label(self, textvariable=self.s).grid(column=0, row=7, columnspan=2,
                                                  sticky="we", padx=5)
        ttk.Label(self, textvariable=self.s).grid(column=0, row=8, columnspan=2,
                                                  sticky="we", padx=5)
        ttk.Entry(self, textvariable=self.x_value, width=15).grid(column=4, row=0, padx=5, pady=5)
        ttk.Label(self, textvariable=self.n_times).grid(column=4, row=1, columnspan=2,
                                                  sticky="we", padx=5)


    def get_result(self):
        try:
            l = self.x_list.get()
            l = l.replace(' ', ' ')
            l = l.replace('[', ' ')
            l = l.replace(']', ' ')
            l = newlistx = l.split(',')
            for elem in newlistx:
                newlistx[newlistx.index(elem)] = float(elem)

            l = self.p_list.get()
            l = l.replace(' ', ' ')
            l = l.replace('[', ' ')
            l = l.replace(']', ',')
            newlistp = l.split(',')
            for elem in newlistp:
                newlistp[newlistp.index(elem)] = int(elem)

            self.new_p.change_data(newlistx, newlistp)

            result = self.new_p.mathexpect()
            self.m.set(f"MATH EXPECTION: {result}")

            result = self.new_p.squaremathexpect()
            self.m2.set(f"MATH EXPECTION IN SQUARE: {result}")

            result = self.new_p.dispersion()
            self.d.set(f"DISPERSION: {result}")

            result = self.new_p.sigma()
            self.s.set(f"SIGMA: {result}")

            result = self.new_p.fashion()
            self.s.set(f"FASHION: {result}")

            n = float(self.x_value.get())
            n_p = self.new_p.get_x_prabability(n)
            self.n_times.set(f"WE SERACH N: {n_p} TIMES")

        except Exception as error:
            showerror(title="Ошибка", message=str(error))


if __name__ == "__main__":
    app = App()
    app.mainloop()
