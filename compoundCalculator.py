import tkinter as tk

class interestCalculator:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self,key,float(value))
        self.endBalance()

    def newContrib(self):
        self.contrib = self.contrib * (1 + (self.contRate/1200))
        return float(self.contrib)

    def endBalance(self):
        for _ in range(int(self.months)):
            self.capital = (self.capital + self.newContrib()) * (1+(self.retRate/1200))



def main():
    resulting = "$0.00"
    def on_submit():
        months = m_e.get()
        contrib = contrib_entry.get()
        capital = cap_entry.get()
        retRate = ret_entry.get()
        contRate = cont_entry.get()
        instance = interestCalculator(months=months,contrib=contrib,capital=capital,retRate=retRate,contRate=contRate)
        results["text"] = "Ending balance of : $" + "{:.2f}".format(instance.capital)

    window=tk.Tk()
    window.title('Compounding interest calculator')
    m_f = tk.Frame(master=window).pack()
    m_lab = tk.Label(master=m_f, text="How many months?").pack()
    m_e = tk.Entry(master=m_f, width=20)
    m_e.pack()
    m_e.insert(0,12)
    tk.Label(master=m_f,text='What is your monthly contribution?').pack()
    contrib_entry = tk.Entry(mmaster=m_f)
    contrib_entry.pack()
    contrib_entry.insert(0,100)
    tk.Label(master=m_f,text='What is your starting capital?').pack()
    cap_entry = tk.Entry(master=m_f)
    cap_entry.pack()
    cap_entry.insert(0,10000)
    tk.Label(master=m_f,text='What is the expected annual percentage return rate?').pack()
    ret_entry = tk.Entry(master=m_f)
    ret_entry.pack()
    ret_entry.insert(0,7)
    tk.Label(master=m_f,text='What is the expected growth percentage of your monthly contribution?').pack()
    cont_entry = tk.Entry(master=m_f)
    cont_entry.pack()
    cont_entry.insert(0,2)

    button = tk.Button(
        text="Run calculator",
        width=25,
        height=5,
        command=on_submit,
    ).pack()

    results = tk.Label(master=m_f, text="Ending balance of : " + resulting)
    results.pack()


if __name__=='__main__':
    main()
input('press enter to exit...')
