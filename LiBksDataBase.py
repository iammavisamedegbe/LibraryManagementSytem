import sqlite3
#database
def connectData():
    con=sqlite3.connect('library.db')
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS libooks(id INTEGER PRIMARY KEY,Mty text, Ref text,Tit text,Fname text, SName text,Addr1 text,
                Addr2 text,PCD text,MNo text,Bkid text,BkTs text,Atr text,Dbo text,Ddu text,DonL text,LrF text,DoD text,Spr text)
                """)
    con.commit()
    con.close()

def addRecord(Mty,Ref,Tit,Fname, SName,Addr1, Addr2,PCD,MNo,Bkid,BkTs,Atr,Dbo,Ddu,DonL,LrF,DoD,Spr):
    con=sqlite3.connect('library.db')
    cur=con.cursor()
    cur.execute("INSERT INTO libooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (Mty,Ref,Tit,Fname, SName,Addr1,Addr2,PCD,MNo,Bkid,BkTs,Atr,Dbo,Ddu,DonL,LrF,DoD,Spr)
                )
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM libooks")
    rows= cur.fetchall()
    con.close()
    return rows

def deleteRecord(id):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    cur.execute("DELETE FROM libooks WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(Mty="",Ref="",Tit="",Fname="", SName="",Addr1="",Addr2="",PCD="",MNo="",Bkid="",BkTs="",Atr="",Dbo="",Ddu="",DonL="",LrF="",DoD="",Spr=""):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM libooks WHERE Mty=? OR Ref=? OR Tit=? OR Fname=? OR SName=? OR Addr1=? OR Addr2=? OR PCD=? OR MNo=? OR Bkid=? OR BkTs=? OR Atr=? OR Dbo=? OR Ddu=? OR DonL=? OR LrF=? OR DoD=? OR Spr=?",
    (Mty, Ref, Tit, Fname, SName, Addr1, Addr2, PCD, MNo, Bkid, BkTs, Atr, Dbo, Ddu, DonL, LrF, DoD, Spr))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id,Mty="",Ref="",Tit="",Fname="", SName="",Addr1="",Addr2="",PCD="",MNo="",Bkid="",BkTs="",Atr="",Dbo="",Ddu="",DonL="",LrF="",DoD="",Spr=""):
    con = sqlite3.connect('library.db')
    cur = con.cursor()
    cur.execute("UPDATE libooks SET Mty=?,Ref=?,Tit=?,Fname=?, SName=?,Addr1=?,Addr2=?,PCD=?,MNo=?,Bkid=?,BkTs=?,Atr=?,Dbo=?,Ddu=?,DonL=?,LrF=?,DoD=?,Spr=? WHERE id=?",
                (Mty, Ref, Tit, Fname, SName, Addr1, Addr2, PCD, MNo, Bkid, BkTs, Atr, Dbo, Ddu, DonL, LrF, DoD, Spr,id))
    con.commit()
    con.close()



connectData()
