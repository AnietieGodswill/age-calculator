from tkinter import *
from tkcalendar import *
from dateutil.relativedelta import *
from datetime import date

#cal_age_split = cal_age.split(" ")[1:]
#today = date.today()
def getentryvalue():
    cal_age = entrybox.get()
    cal_age_split = cal_age.split()
    today = date.today()
    for i in cal_age_split:
        cal_days = i.split("/")[-1]
        cal_months = i.split("/")[1]
        cal_years = i.split("/")[0]
        #print(cal_days,cal_months,cal_years)
        dob = date(int(cal_years),int(cal_months),int(cal_days))
        age = relativedelta(today, dob)
        find_yrs = age.years
        find_mon = age.months
        find_day = age.days
        store_yrs_mon_day = find_yrs*365+find_mon*30+find_day*1
        earth = store_yrs_mon_day/365
        mercury = store_yrs_mon_day/88
        venus = store_yrs_mon_day/225
        mars = store_yrs_mon_day/687
        jupiter = store_yrs_mon_day/(11.8 * 365)
        saturn = store_yrs_mon_day/(29.4 * 365)
        uranus = store_yrs_mon_day/(84 * 365)
        neptune = store_yrs_mon_day/(164*365)
        pluto = store_yrs_mon_day/(248 * 365)
        listbox.delete(0,END)
        listbox.insert(1,f"</> Mercury : {mercury:.2f} YEARS")
        listbox.insert(2,f"</> Venus     : {venus:.2f} YEARS")
        listbox.insert(3,f"</> Earth      : {earth:.2f} YEARS")
        listbox.insert(4,f"</> Mars       : {mars:.2f} YEARS")
        listbox.insert(5,f"</> Jupiter    : {jupiter:.2f} YEARS")
        listbox.insert(6,f"</> Saturn    : {saturn:.2f} YEARS")
        listbox.insert(7,f"</> Uranus   : {uranus:.2f} YEARS")
        listbox.insert(8,f"</> Neptune : {neptune:.2f} YEARS")
        listbox.insert(9,f"</> Pluto       : {pluto:.2f} YEARS")

if __name__ == "__main__":
    root = Tk()
    root.iconbitmap('icon.ico')
    root.resizable(0, 0)
    root.title("AGE FINDER - dx4iot")
    root.config(background="gray10")
    root.geometry("550x700")
    
    heading_h1 = Label(root,text="AGE CALCULATOR",font="Jokerman 38 bold", bg="gray10",fg="white")
    heading_h1.pack()
    #cal = Calendar(root,selectmode="day",year=2020,month=5,day=22)
    #cal.pack(pady=20)
    heading_h2 = Label(root,text="ENTER D.O.B",font="Forte 20", bg="gray10",fg="white")
    heading_h2.pack()
    entrybox = Entry(root,font="Forte 20 bold",width=20)
    entrybox.insert(0, 'YY/MM/DD')
    entrybox.pack()
    listbox = Listbox(root,selectmode=EXTENDED,bg='gray',fg='white',font='Cambria 20',width=25,height=10)
    listbox.pack(pady=20)
    button = Button(root, text='FIND AGE', command=getentryvalue,fg='white',font='Forte 20',bg="gray10",width=20)
    button.pack(pady=10)
    
    credit = Label(root,text="Developed By - dx4iot",font="Terminal 20", bg="gray10",fg="white")
    credit.pack(pady=25)

    root.mainloop()
