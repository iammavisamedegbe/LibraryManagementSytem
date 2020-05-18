from tkinter import *
import tkinter.messagebox
import LiBksDataBase

class Library:
    def __init__(self, root):
        self.root=root
        self.root.geometry('1200x600+0+0')
        self.root.title('Library Management System')

        #========Variables used throughout the project===========
        Mty= StringVar()
        Ref =StringVar()
        Tit =StringVar()
        Fname=StringVar()
        SName=StringVar()
        Addr1=StringVar()
        Addr2=StringVar()
        PCD=StringVar()
        MNo=StringVar()
        Bkid=StringVar()
        BkTs=StringVar()
        Atr=StringVar()
        Dbo=StringVar()
        Ddu=StringVar()
        Spr=StringVar()
        LrF=StringVar()
        DoD=StringVar()
        DonL=StringVar()

        #============Functions==============================================================================
        def iExit():
            iExit=tkinter.messagebox.askyesno('LIBRARY MANAGEMENT SYTSEM', 'Confirm Exit')
            if iExit>0:
             root.destroy()
            return
        def clearData():
            self.textMty.delete(0,END)
            self.textRef .delete(0, END)
            self.textTit.delete(0, END)
            self.textfname.delete(0, END)
            self.textlname.delete(0, END)
            self.textAddr1.delete(0, END)
            self.textAddr2.delete(0, END)
            self.textPostcode.delete(0,END)
            self.textMobileNo.delete(0, END)
            self.textBookId.delete(0, END)
            self.textBookTitle.delete(0, END)
            self.textAuthor.delete(0, END)
            self.textDateBorrowed .delete(0, END)
            self.textDateDue.delete(0, END)
            self.textDateLoan.delete(0, END)
            self.textLateReutn.delete(0, END)
            self.textDateoverDue.delete(0, END)
            self.textSellingprice.delete(0, END)

        def addData():
            if (len(Mty.get())!=0):
                LiBksDataBase.addRecord(Mty.get(), Ref.get(),Tit.get(),Fname.get(), SName.get(),Addr1.get(),Addr2.get(),PCD.get(),
                MNo.get(),Bkid.get(),BkTs.get(),Atr.get(),Dbo.get(),Ddu.get(),DonL.get(),LrF.get(),DoD.get(),Spr.get())
                
                booklist.delete(0,END)
                booklist.insert(END,(Mty.get(), Ref.get(),Tit.get(),Fname.get(), SName.get(),Addr1.get(),Addr2.get(),PCD.get(),
                MNo.get(),Bkid.get(),BkTs.get(),Atr.get(),Dbo.get(),Ddu.get(),DonL.get(),LrF.get(),DoD.get(),Spr.get()))
        
        def DisplayData():
            booklist.delete(0,END)
            for row in LiBksDataBase.viewData():
                booklist.insert(END,row)

        def selectedBook(event):
            global sb
            searchBook=booklist.curselection()[0]
            sb=booklist.get(searchBook)

            self.textMty.delete(0, END)
            self.textMty.insert(END,sb[1])
            self.textRef.delete(0, END)
            self.textRef.insert(END,sb[2])
            self.textTit.delete(0, END)
            self.textTit.insert(END,sb[3])
            self.textfname.delete(0, END)
            self.textfname.insert(END,sb[4])
            self.textlname.delete(0, END)
            self.textlname.insert(END,sb[5])
            self.textAddr1.delete(0, END)
            self.textAddr1.insert(END,sb[6])
            self.textAddr2.delete(0, END)
            self.textAddr2.insert(END,sb[7])
            self.textPostcode.delete(0, END)
            self.textPostcode.insert(END,sb[8])
            self.textMobileNo.delete(0, END)
            self.textMobileNo.insert(END,sb[9])
            self.textBookId.delete(0, END)
            self.textBookId.insert(END,sb[10])
            self.textBookTitle.delete(0, END)
            self.textBookTitle.insert(END,sb[11])
            self.textAuthor.delete(0, END)
            self.textAuthor.insert(END,sb[12])
            self.textDateBorrowed.delete(0, END)
            self.textDateBorrowed.insert(END,sb[13])
            self.textDateDue.delete(0, END)
            self.textDateDue.insert(END, sb[14])
            self.textDateLoan.delete(0, END)
            self.textDateLoan.insert(END,sb[15])
            self.textLateReutn.delete(0, END)
            self.textLateReutn.insert(END,sb[16])
            self.textDateoverDue.delete(0, END)
            self.textDateoverDue.insert(END,sb[17])
            self.textSellingprice.delete(0, END)
            self.textSellingprice.insert(END,sb[18])

        def deleteData():
            if (len(Mty.get()) != 0):
                LiBksDataBase.deleteRecord(sb[0])
                clearData()
                DisplayData()

        def seachDatabase():
            booklist.delete(0,END)
            for row in LiBksDataBase.searchData(Mty.get(), Ref.get(),Tit.get(),Fname.get(), SName.get(),Addr1.get(),Addr2.get(),PCD.get(),
                MNo.get(),Bkid.get(),BkTs.get(),Atr.get(),Dbo.get(),Ddu.get(),DonL.get(),LrF.get(),DoD.get(),Spr.get()):
                booklist.insert(END,row)

        def update():
            if (len(Mty.get()) != 0):
                LiBksDataBase.dataUpdate(sb[0],Mty.get(), Ref.get(),Tit.get(),Fname.get(), SName.get(),Addr1.get(),Addr2.get(),PCD.get(),
                MNo.get(),Bkid.get(),BkTs.get(),Atr.get(),Dbo.get(),Ddu.get(),DonL.get(),LrF.get(),DoD.get(),Spr.get())

        # ============Frames================================================================================
        MainFrame= Frame(self.root)
        MainFrame.grid()

        TitFrame=Frame(MainFrame,pady=8, padx=10,relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit=Label(TitFrame,font=('ariel',30, 'bold'),text='LIBRARY MANAGEMENT SYSTEM')
        self.lblTit.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, width='1000',height=120, bd=2, pady=20, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DetailFrame = Frame(MainFrame, width='1200', height=20, bd=0, pady=20, padx=20, relief=RIDGE)
        DetailFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, width='1000', height=500, bd=2, pady=10, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, width='600', height=400,font=('ariel', 15, 'bold'), text='LIBRARY MEMBERSHIP INFOR:')
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight= LabelFrame(DataFrame, width='400', height=300, pady=3, padx=15,font=('ariel', 15, 'bold'), text='BOOK DETAILS:')
        DataFrameRight.pack(side=RIGHT)

        # ============Labels and Entrys============================
        self.lblMty=Label( DataFrameLeft,font=('ariel',13, 'bold'),text='Member Type:',padx=2, pady=1 )
        self.lblMty.grid(row=0,column=0,sticky=W)
        self.textMty = Entry( DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Mty, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textMty.grid(row=0, column=1)

        self.lblRef = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Reference No.:', padx=2, pady=1)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.textRef = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Ref, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textRef.grid(row=1, column=1)

        self.lblTit = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Title:', padx=2, pady=1)
        self.lblTit .grid(row=2, column=0, sticky=W)
        self.textTit = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Tit, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textTit .grid(row=2, column=1)

        self.lblfName = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='First Name:', padx=2, pady=1)
        self.lblfName.grid(row=3, column=0, sticky=W)
        self.textfname = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Fname, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textfname.grid(row=3, column=1)

        self.lbllName = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Last Name:', padx=2, pady=1)
        self.lbllName.grid(row=4, column=0, sticky=W)
        self.textlname = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=SName, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textlname.grid(row=4, column=1)

        self.lblAddr1 = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Address 1:', padx=2, pady=1)
        self.lblAddr1.grid(row=5, column=0, sticky=W)
        self.textAddr1 = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Addr1, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textAddr1 .grid(row=5, column=1)

        self.lblAddr2 = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Address 2:', padx=2, pady=1)
        self.lblAddr2.grid(row=6, column=0, sticky=W)
        self.textAddr2 = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Addr2, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textAddr2.grid(row=6, column=1)

        self.lblPostcode = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Post Code:', padx=2, pady=1)
        self.lblPostcode .grid(row=7, column=0, sticky=W)
        self.textPostcode = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=PCD, width=20,relief=SUNKEN,insertwidth=4,bd=4)
        self.textPostcode.grid(row=7, column=1)

        self.lblMobileNo = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Mobile No.:', padx=2, pady=1)
        self.lblMobileNo.grid(row=8, column=0, sticky=W)
        self.textMobileNo = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=MNo, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textMobileNo.grid(row=8, column=1)

        self.lblBookId = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Book Id.:', padx=2, pady=1)
        self.lblBookId .grid(row=0, column=2, sticky=W)
        self.textBookId = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Bkid, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textBookId.grid(row=0, column=3)

        self.lblBookTitle= Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Book Title:', padx=2, pady=1)
        self.lblBookTitle.grid(row=1, column=2, sticky=W)
        self.textBookTitle = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=BkTs, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textBookTitle.grid(row=1, column=3)

        self.lblAuthor = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Author:', padx=2, pady=1)
        self.lblAuthor.grid(row=2, column=2, sticky=W)
        self.textAuthor = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Atr, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textAuthor.grid(row=2, column=3)

        self.lblDateBorrowed = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Date Borrowed:', padx=2, pady=1)
        self.lblDateBorrowed.grid(row=3, column=2, sticky=W)
        self.textDateBorrowed = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Dbo, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textDateBorrowed .grid(row=3, column=3)

        self.lblDateDue = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Date Due', padx=2, pady=1)
        self.lblDateDue .grid(row=4, column=2, sticky=W)
        self.textDateDue = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Ddu, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textDateDue.grid(row=4, column=3)

        self.lblDateLoan = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Days on Loan', padx=2, pady=1)
        self.lblDateLoan.grid(row=5, column=2, sticky=W)
        self.textDateLoan = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=DonL, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textDateLoan.grid(row=5, column=3)

        self.lblLateReutn = Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Late Return Fine', padx=2, pady=1)
        self.lblLateReutn.grid(row=6, column=2, sticky=W)
        self.textLateReutn = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=LrF, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textLateReutn.grid(row=6, column=3)

        self.lblDateoverDue= Label(DataFrameLeft, font=('ariel',13, 'bold'), text='Date Over Due', padx=2, pady=1)
        self.lblDateoverDue.grid(row=7, column=2, sticky=W)
        self.textDateoverDue = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=DoD, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textDateoverDue.grid(row=7, column=3)

        self.lblSellingprice= Label(DataFrameLeft,font=('ariel',13, 'bold'), text='Selling Price', padx=2, pady=1)
        self.lblSellingprice.grid(row=8, column=2, sticky=W)
        self.textSellingprice = Entry(DataFrameLeft, font=('ariel', 15, 'bold'), textvariable=Spr, width=20, relief=SUNKEN,insertwidth=4,bd=4)
        self.textSellingprice.grid(row=8, column=3)

    # ============List and Scrollbar============================
        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky="ns")
        booklist=Listbox(DataFrameRight, width=30,height=11,font=('ariel', 15, 'bold'),bd=4,yscrollcommand=scrollbar.set)
        booklist.bind("<<ListboxSelect>>",selectedBook)
        booklist.grid(row=0,column=0, padx=8)
        scrollbar.config(command=booklist.yview)
    # ============Buttons======================================
        self.btnAddData=Button(ButtonFrame,font=('ariel', 15, 'bold'),height=1,width=10,bd=4, text='Add Data', command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, font=('ariel', 15, 'bold'), height=1, width=10, bd=4, text='Display Data',command=DisplayData)
        self.btnDisplayData .grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, font=('ariel', 15, 'bold'), height=1, width=10, bd=4, text='Clear Data', command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, font=('ariel', 15, 'bold'), height=1, width=10, bd=4, text='Delete Data', command=deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnUpdateData = Button(ButtonFrame, font=('ariel', 15, 'bold'), height=1, width=10, bd=4, text='Update Data',command=update)
        self.btnUpdateData.grid(row=0, column=4)

        self.btnSearchData = Button(ButtonFrame, font=('ariel', 15, 'bold'), height=1, width=10, bd=4, text='Search Data ', command=seachDatabase)
        self.btnSearchData .grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, font=('ariel', 15, 'bold'), height=1, width=10, bd=4,  text='Exit', command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__ == '__main__':
    root=Tk()
    application=Library(root)
    root.mainloop()



