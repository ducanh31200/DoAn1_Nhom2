
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insertBefore(self, given_ptr, new_data):
        if (self.head == given_ptr):

            n = Node(new_data)

            n.next = self.head

            self.head = n
        else:
            p = None
            n = self.head

            while (n != given_ptr):
                p = n
                n = n.next

            m = Node(new_data)

            m.next = p.next

            p.next = m

    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node


    def append(self, new_data):

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def remove(self, data):
        temp = self.head


        if (temp is not None):
            if (temp.data == data):
                self.head = temp.next
                temp = None
                return


        while (temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next

        temp = None
    def printList(self):
        temp = self.head
        while (temp):
            temp.data.show()
            temp = temp.next

    def printCompare(self):
        f = open("DS_Cau__6.txt", "w", encoding='utf-8')
        temp = self.head
        while (temp):
            if (temp.data.DT.data.Toan > temp.data.DT.data.Van):
                f.write( temp.data.details() + "\n")
            temp = temp.next
        f.close()

    def sort5(self):
        temp1 = self.head
        while (temp1):
            temp2 = temp1.next
            while (temp2):
                if (temp1.data.DS.data.MaTruong > temp2.data.DS.data.MaTruong):
                    temp = temp1.data
                    temp1.data = temp2.data
                    temp2.data = temp
                elif (temp1.data.DS.data.MaTruong == temp2.data.DS.data.MaTruong):
                    if (temp1.data.DS.data.Ten > temp2.data.DS.data.Ten):
                        temp = temp1.data
                        temp1.data = temp2.data
                        temp2.data = temp
                    elif (temp1.data.DS.data.Ten == temp2.data.DS.data.Ten):
                        if (temp1.data.DS.data.Ho > temp2.data.DS.data.Ho):
                            temp = temp1.data
                            temp1.data = temp2.data
                            temp2.data = temp
                temp2 = temp2.next

            temp1 = temp1.next
        f = open("DS_Cau_5.txt", "w", encoding='utf-8')
        t = self.head

        while (t):
            f.write( t.data.details1() + "\n")
            t = t.next
        f.close()

    def sort7(self):
        temp1 = self.head
        while (temp1):
            temp2 = temp1.next
            while (temp2):
                if (temp1.data.DS.data.MaTruong == temp2.data.DS.data.MaTruong):
                    if (temp1.data.TONGDIEM() < temp2.data.TONGDIEM()):
                        temp = temp1.data
                        temp1.data = temp2.data
                        temp2.data = temp
                temp2 = temp2.next
            temp1 = temp1.next
        f = open("DS_Cau__7.txt", "w", encoding='utf-8')
        t = self.head
        while (t):
            if (t.data.XEPLOAI() == 'Kem'):
                f.write( t.data.details() + "\n")
            t = t.next
        f.close()
    def thukhoa(self):
        temp1 = self.head
        while (temp1):
            temp2 = temp1.next
            while (temp2):
                if (temp1.data.DS.data.MaTruong == temp2.data.DS.data.MaTruong):
                    if (temp1.data.TONGDIEM() < temp2.data.TONGDIEM()):
                        temp = temp1.data
                        temp1.data = temp2.data
                        temp2.data = temp
                temp2 = temp2.next
            temp1 = temp1.next

        t = self.head
        while (t):
            if (t.data.XEPLOAI() == 'Kem'):
                t.data.show()
            t = t.next

    def Check(self, MaTruong, truong, i):

        if not truong:
            return True
        else:
            for x in range(i):
                if (MaTruong == truong[x]):
                    return False
        return True

    def cau8(self):
        truong = []
        i = 0
        f = open("DS_Cau__8.txt", "w", encoding='utf-8')
        temp = self.head
        while (temp):
            if (self.Check(temp.data.DS.data.MaTruong, truong, i)):
                f.write(temp.data.details() + "\n")
                truong.append(temp.data.DS.data.MaTruong)
                i = i + 1
            temp = temp.next
        f.close()
    def List_MaTr(self, MT):
        MT = MT + "   "
        f = open("DS_Cau__9.txt", "w", encoding = 'utf-8')
        temp = self.head
        dau = 0
        truot = 0
        tongso = 0
        while(temp):
            if( temp.data.DS.data.MaTruong.strip() == MT.strip()):
                tongso = tongso + 1
                f.write( temp.data.details() + "\n")
                if temp.data.XEPLOAI() == "Kem" :
                    truot = truot + 1
                else :
                    dau = dau + 1
            temp = temp.next
        if tongso == 0:
            f.write("Khong co Ma Truong nay trong danh sach")
        else :
            ptDau = dau*100/tongso
            ptTruot = truot*100/tongso
            f.write("Ti le dau va truot la : " + str(ptDau) + "% va " + str(ptTruot) + "%")
        f.close()


    def List_SBD(self, id_sbd):
      f = open("DS_Cau__10.txt", "w", encoding = 'utf-8')
      temp = self.head
      dem = 0
      while(temp):
        if( temp.data.DS.data.SBD.strip() == id_sbd.strip()):
            dem = 1
            if(int(temp.data.DS.data.Phai) == 0):
                f.write( 'GIAY BAO DIEM' + '\n' +
                         'So Bao Danh: ' + str(temp.data.DS.data.SBD) + '\n' +
                         'Anh: ' + temp.data.DS.data.Ho + " " + temp.data.DS.data.Ten + '\n' +
                         'Toan: ' + str(temp.data.DT.data.Toan) + '\n' +
                         'Van: ' + str(temp.data.DT.data.Van) + '\n' +
                         'Tong Diem: ' + str(temp.data.TONGDIEM()) + '\n' +
                         'Xep Loai: ' + temp.data.XEPLOAI()
                         )
            else:
                f.write( 'GIAY BAO DIEM' + '\n' +
                         'So Bao Danh: ' + str(temp.data.DS.data.SBD) + '\n' +
                         'Chi: ' + temp.data.DS.data.Ho + " " + temp.data.DS.data.Ten + '\n' +
                         'Toan: ' + str(temp.data.DT.data.Toan) + '\n' +
                         'Van: ' + str(temp.data.DT.data.Van) + '\n' +
                         'Tong Diem: ' + str(temp.data.TONGDIEM()) + '\n' +
                         'Xep Loai: ' + temp.data.XEPLOAI()
                         )
        temp = temp.next
      if(dem == 0):
          f.write("Khong co thi sinh nay !")
      f.close()


class DiemThi:
    def __init__(self, SBD, Mon, Diem):
        self.SBD = SBD
        self.Mon = Mon
        self.Diem = Diem

    def details(self):
        return str(self.SBD) + "|" + str(self.Mon) + "|" + str(self.Diem) + "|"

    def show(self):
        print(self.details())


class DanhSach:
    def __init__(self, SBD, Ho, Ten, Phai, NgaySinh, MaTruong):
        self.SBD = SBD
        self.Ho = Ho
        self.Ten = Ten
        self.Phai = Phai
        self.NgaySinh = NgaySinh
        self.MaTruong = MaTruong

    def details(self):
        return self.Ho + " " + self.Ten + "|" + self.Phai + "|" + self.NgaySinh + "|" + self.MaTruong + "|"

    def show(self):
        print(self.details())


class Combine:
    def __init__(self, DS, DT):
        self.SBD = DS.data.SBD
        self.Toan = DS.data.Diem
        self.Van = DT.data.Diem

    def details(self):
        return str(self.Toan) + "|" + str(self.Van) + "|"

    def show(self):
        print(self.details())


class Data():
    def __init__(self, DS, DT):
        self.DS = DS
        self.DT = DT

    def details(self):
        return str(self.DS.data.SBD) + "|" + self.DS.data.details() + self.DT.data.details()

    def details1(self):
        return str(self.DS.data.SBD) + "|" + self.DS.data.details() + self.DT.data.details() + str(
            self.DTN()) + "|" + str(self.TONGDIEM()) + "|" + self.XEPLOAI()

    def show(self):
        print(self.details())

    # DTN
    def DTN(self):
        dtn = self.DT.data.Toan
        if (self.DT.data.Toan > self.DT.data.Van):
            dtn = self.DT.data.Van
        return dtn

    def TONGDIEM(self):
        sum = self.DT.data.Toan + self.DT.data.Van
        return sum

    def XEPLOAI(self):
        strr = ''
        if (self.TONGDIEM() >= 16 and self.DTN() >= 7):
            strr = "Gioi"
        elif (self.TONGDIEM() >= 14 and self.DTN() >= 6):
            strr = "Kha"
        elif (self.TONGDIEM() >= 10 and self.DTN() >= 4):
            strr = "Trung Binh"
        else:
            strr = "Kem"
        return strr

def xemDSTXT():
    newWin = Toplevel()
    newWin.title("Danh sách")

    my_text = Text(newWin)
    my_text.pack()


    text_file = open("DanhSach.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def xemTruongTXT():
    newWin = Toplevel()
    newWin.title("Chi tiết đối tượng")

    my_text = Text(newWin)
    my_text.pack()


    text_file = open("Truong.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def xemDiemTXT():
    newWin = Toplevel()
    newWin.title("Danh sách điểm thi")

    my_text = Text(newWin)
    my_text.pack()


    text_file = open("Diem.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def btn_SearchSBD_delete_Click():
    if(SBD_delete_field.get() == ""):
        messagebox.showerror("Lỗi !", "Hãy nhập SBD !")
    else:
        sbd = SBD_delete_field.get()
        dem = 0
        temp = llistData.head
        while(temp):
            if(temp.data.DS.data.SBD.strip() == sbd.strip()):
                print(sbd)
                print(temp.data.DS.data.SBD.strip())
                llistData.remove(temp.data)
                dem = 1
                messagebox.showinfo("Success !", "Đã Xóa Mẫu Tin: " + str(sbd))
                break
            temp = temp.next
        llistData.sort5()
        if(dem == 0) :
            messagebox.showinfo("Fail !", "Không có thí sinh : " + str(sbd))
    clearAll()

def clearAll():
        SBD_delete_field.delete(0, END)
        sobaodanh_field.delete(0, END)
        lastName_field.delete(0, END)
        firstName_field.delete(0, END)
        gender_field.delete(0, END)
        birthday_field.delete(0, END)
        matruong_field.delete(0, END)
        math_field.delete(0, END)
        van_field.delete(0, END)
        model_field.delete(0, END)
        sobaodanh_field.delete(0, END)
        MaTr_field.delete(0, END)
        SBD_field.delete(0, END)

def checkError():
    if( sobaodanh_field.get() == '' or
    lastName_field.get() == '' or
    firstName_field.get() == '' or
    gender_field.get() == '' or
    birthday_field.get() == '' or
    matruong_field.get() == '' or
    math_field.get() == '' or
    van_field.get() == '' or
    model_field.get() == ''):
        messagebox.showerror("Lỗi !")

        return -1
    else:
        temp = llistData.head
        while(temp):
            if(temp.data.DS.data.SBD.strip() == sobaodanh_field.get().strip()):
                messagebox.showerror("Lỗi !", "SBD tồn tại rồi, Vui lòng nhập SBD khác !")

                return -1
            temp = temp.next
def insertBefore_3():
    value = checkError()
    if (value == -1):
        return
    else:
        SBD = sobaodanh_field.get()
        Ho = lastName_field.get()
        Ten = firstName_field.get()
        Phai = gender_field.get()
        NgaySinh = birthday_field.get()
        Matruong = matruong_field.get()
        Toan = float(math_field.get())
        Van = float(van_field.get())
        a = DanhSach(SBD, Ho, Ten, Phai, NgaySinh, Matruong)
        llist.append(a)
        b = DiemThi(SBD,"Toan",Toan)
        c = DiemThi(SBD,"Van", Van)
        llist2.append(b)
        llist2.append(c)
        ds3 = llist2.head
        while (ds3):
            dt = ds3.next
            while (dt):
                if (ds3.data.SBD.strip() == SBD.strip()):

                    e = Combine(ds3, dt)
                    llist3.append(e)
                    break
                dt = dt.next
            ds3 = ds3.next

        ds = llist.head
        while ds:
            dt1 = llist3.head
            while (dt1):
                if (ds.data.SBD.strip() == SBD.strip() and dt1.data.SBD.strip() == SBD.strip()):
                    c = Data(ds, dt1)
                    break
                dt1 = dt1.next
            ds = ds.next

        f = open("DanhSach1.txt", "w", encoding='utf-8')

        temp = llistData.head
        while (temp):
            if ('0001' == model_field.get().strip()):
                llistData.push(c)
                break
            elif temp.data.DS.data.SBD.strip() == model_field.get().strip():
                llistData.insertBefore(x.next, c)
                break
            x = temp
            temp = temp.next
        acb = llistData.head
        while (acb):
            f.write(acb.data.details() + "\n")
            acb = acb.next
        f.close()
        newWin = Toplevel()
        newWin.title("Danh sách sinh viên ")

        my_text = Text(newWin)
        my_text.pack()

        text_file = open("DanhSach1.txt", 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
    clearAll()



def insertAfter_4():
    value = checkError()
    if (value == -1):
        return
    else:
        SBD = sobaodanh_field.get()
        Ho = lastName_field.get()
        Ten = firstName_field.get()
        Phai = gender_field.get()
        NgaySinh = birthday_field.get()
        Matruong = matruong_field.get()
        Toan = float(math_field.get())
        Van = float(van_field.get())
        a = DanhSach(SBD, Ho, Ten, Phai, NgaySinh, Matruong)
        llist.append(a)
        b = DiemThi(SBD, "Toan", Toan)
        c = DiemThi(SBD, "Van", Van)
        llist2.append(b)
        llist2.append(c)
        ds3 = llist2.head
        while (ds3):
            dt = ds3.next
            while (dt):
                if (ds3.data.SBD.strip() == SBD.strip()):
                    e = Combine(ds3, dt)
                    llist3.append(e)
                    break
                dt = dt.next
            ds3 = ds3.next

        ds = llist.head
        while ds:
            dt1 = llist3.head
            while (dt1):
                if (ds.data.SBD.strip() == SBD.strip() and dt1.data.SBD.strip() == SBD.strip()):
                    c = Data(ds, dt1)
                    break
                dt1 = dt1.next
            ds = ds.next

        f = open("DanhSach2.txt", "w", encoding='utf-8')

        temp = llistData.head
        while (temp):
            if ('123' == model_field.get().strip()):
                llistData.push(c)
                break
            elif temp.data.DS.data.SBD.strip() == model_field.get().strip():

                llistData.insertBefore(temp.next, c)
                break

            temp = temp.next
        acb = llistData.head
        while (acb):
            f.write(acb.data.details() + "\n")
            acb = acb.next
        f.close()
        newWin = Toplevel()
        newWin.title("Danh sách sinh viên ")

        my_text = Text(newWin)
        my_text.pack()

        text_file = open("DanhSach2.txt", 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
    clearAll()

def btn_Cau5():

    llistData.sort5()
    newWin = Toplevel()
    newWin.title("Danh sách sinh viên ")

    my_text = Text(newWin)
    my_text.pack()

    text_file = open("DS_Cau_5.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def btn_Cau6():
    llistData.printCompare()
    newWin = Toplevel()
    newWin.title("Danh Sách Sinh Viên có điểm Toán lớn hơn Văn ")

    my_text = Text(newWin)
    my_text.pack()

    text_file = open("DS_Cau__6.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def btn_Cau7():
    llistData.sort7()
    newWin = Toplevel()
    newWin.title("Danh Sách Sinh Viên Kém ")

    my_text = Text(newWin)
    my_text.pack()

    text_file = open("DS_Cau__7.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def btn_Cau8():
    llistData.sort7()
    llistData.cau8()
    newWin = Toplevel()
    newWin.title("Danh Sách Sinh Viên Thủ Khoa ")

    my_text = Text(newWin)
    my_text.pack()

    text_file = open("DS_Cau__8.txt", 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()





def btn_SearchMT_Click():
    if (MaTr_field.get() == ""):
        messagebox.showerror("Lỗi !", "Hãy nhập mã trường !")
    else:
        matruong = MaTr_field.get()

        llistData.List_MaTr(matruong)
        newWin = Toplevel()
        newWin.title("Danh Sách Sinh Viên có mã trường " + MaTr_field.get())

        my_text = Text(newWin)
        my_text.pack()


        text_file = open("DS_Cau__9.txt", 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
    clearAll()

    # Câu 10


def btn_SearchSBD_Click():
    if (SBD_field.get() == ""):
        messagebox.showerror("Lỗi !", "Hãy nhập SBD!")
    else:
        sbd = SBD_field.get()

        llistData.List_SBD(sbd.strip())
        newWin = Toplevel()
        newWin.title("Chi Tiết Sinh Viên SBD: " + SBD_field.get())

        my_text = Text(newWin)
        my_text.pack()


        text_file = open("DS_Cau__10.txt", 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
    clearAll()

if __name__ == '__main__':

    llist = LinkedList()
    llist2 = LinkedList()
    llist3 = LinkedList()
    llistData = LinkedList()

    f = open("DanhSach.txt", "r")
    for x in f:
        SBD = str(x[0:5])
        Ho = str(x[5:20])
        Ten = str(x[20:27])
        Phai = str(x[27:29])
        NgaySinh = str(x[29:40])
        MaTruong = str(x[40:44])
        a = DanhSach(SBD, Ho, Ten, Phai, NgaySinh, MaTruong)
        llist.append(a)

    f = open("Diem.txt", "r")
    for x in f:
        a = DiemThi(str(x[0:5]), str(x[5:14]), float(x[14:20]))
        llist2.append(a)

    ds3 = llist2.head
    while (ds3):
        dt = ds3.next
        while (dt):
            if (ds3.data.SBD == dt.data.SBD):
                a = Combine(ds3, dt)
                llist3.append(a)
            dt = dt.next
        ds3 = ds3.next

    ds = llist.head
    while (ds):
        dt = llist3.head
        while (dt):
            if (ds.data.SBD == dt.data.SBD):
                llistData.append(Data(ds, dt))
            dt = dt.next
        ds = ds.next



    # create form
    root = Tk()
    root.title("Quản lý điểm thi")
    root.geometry("550x400")
    heading = Label(root, text="")


    btn_DSTXT = Button(root, text="Xem File Danh Sách", command=xemDSTXT)
    btn_TruongTXT = Button(root, text="Xem File Trường", command=xemTruongTXT)
    btn_DiemTXT = Button(root, text="Xem File Điểm", command=xemDiemTXT)

    btn_Cau5 = Button(root, text="Danh Sách Sinh Viên",command=btn_Cau5)
    btn_Cau6 = Button(root, text="DS Sinh Viên Toán lớn hơn Văn",command=btn_Cau6)
    btn_Cau7 = Button(root, text="DS Sinh Viên Kém",command=btn_Cau7)
    btn_Cau8 = Button(root, text="DS Sinh Thủ Khoa", command=btn_Cau8)

    MaTr = Label(root, text="Mã Trường", bg="light green")
    MaTr_field = Entry(root)
    btn_SearchMT = Button(root, text="Search", fg="Black", command=btn_SearchMT_Click)

    SBD = Label(root, text="Số Báo Danh", bg="light green")
    SBD_field = Entry(root)
    btn_SearchSBD = Button(root, text="Search_SBD", fg="Black", command=btn_SearchSBD_Click)

    SBD_delete = Label(root, text="Xóa Một Mẫu Tin", bg="light green")
    SBD_delete_field = Entry(root)
    btn_SearchSBD_delete = Button(root, text="Xoa", fg="Black", command=btn_SearchSBD_delete_Click)

    insertNode = Label(root, text="Mục Chèn Node", bg="light green")
    sobaodanh = Label(root, text="SBD", bg="light green")
    lastName = Label(root, text="Họ", bg="light green")
    firstName = Label(root, text="Tên", bg="light green")
    gender = Label(root, text="Phái", bg="light green")
    birthday = Label(root, text="Ngày Sinh", bg="light green")
    matruong = Label(root, text="Mã Trường", bg="light green")
    math = Label(root, text="Toán", bg="light green")
    van = Label(root, text="Văn", bg="light green")

    model = Label(root, text="Mẫu chọn để chèn", bg="light green")

    sobaodanh_field = Entry(root)
    lastName_field = Entry(root)
    firstName_field = Entry(root)
    gender_field = Entry(root)
    birthday_field = Entry(root)
    matruong_field = Entry(root)
    math_field = Entry(root)
    van_field = Entry(root)

    model_field = Entry(root)

    btn_insertAfter = Button(root, text="Chèn sau", fg="Black", command=insertAfter_4)

    btn_insertBefore = Button(root, text="Chèn trước", fg="Black", command=insertBefore_3)

    # position
    heading.grid(row=0, column=1)
    btn_DSTXT.grid(row=1, column=0)
    btn_TruongTXT.grid(row=1, column=1)
    btn_DiemTXT.grid(row=1, column=2)

    btn_Cau5.grid(row=2, column=0)
    btn_Cau6.grid(row=2, column=1)
    btn_Cau7.grid(row=2, column=2)
    btn_Cau8.grid(row=2, column=4)


    MaTr.grid(row=6, column=0)
    MaTr_field.grid(row=6, column=1)
    btn_SearchMT.grid(row=6, column=2)

    SBD.grid(row=7, column=0)
    SBD_field.grid(row=7, column=1)
    btn_SearchSBD.grid(row=7, column=2)

    SBD_delete.grid(row=8, column=0)
    SBD_delete_field.grid(row=8, column=1)
    btn_SearchSBD_delete.grid(row=8, column=2)

    insertNode.grid(row=9, column=1)

    sobaodanh.grid(row=10, column=0)
    lastName.grid(row=11, column=0)
    firstName.grid(row=12, column=0)
    gender.grid(row=13, column=0)
    birthday.grid(row=14, column=0)
    matruong.grid(row=15, column=0)
    math.grid(row=16, column=0)
    van.grid(row=17, column=0)

    sobaodanh_field.grid(row=10, column=1)
    lastName_field.grid(row=11, column=1)
    firstName_field.grid(row=12, column=1)
    gender_field.grid(row=13, column=1)
    birthday_field.grid(row=14, column=1)
    matruong_field.grid(row=15, column=1)
    math_field.grid(row=16, column=1)
    van_field.grid(row=17, column=1)

    model.grid(row=16, column=2)
    model_field.grid(row=17, column=2)
    btn_insertBefore.grid(row=19, column=2)
    btn_insertAfter.grid(row=20, column=2)

    root.mainloop()

