import csv, operator, openpyxl
from xlrd import open_workbook

cont = 0

def open_text_file(strNameFile):
    global res
    try:
        f = open(strNameFile, "r")
        tf = f.readlines()
        f.close()
        return tf
    except:
        pass


def write_excel(info):
    global cont
    try:
        doc = openpyxl.load_workbook("Doc.xlsx")
        sheet = doc.get_sheet_by_name('Hoja1')
        cont = 1
        for line in info:
            sheet['A'+str(cont)] = line
            cont += 1
        doc.save("Doc.xlsx")
    except:
        print("Error!")


def read_excel():
    try:
        doc = openpyxl.load_workbook("Doc.xlsx")
        sheet = doc.get_sheet_by_name('Hoja1')
        i = 1
        while i < cont:
            print(sheet['A'+str(i)].value)
            i += 1
        doc.save("Doc.xlsx")
    except:
        print("Error!")

write_excel(open_text_file("12_write_excel.py"))
read_excel()
