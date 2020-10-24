import pdfplumber
import re
import openpyxl
import os
import xlwt
import datetime

def generate_Path(FolderPath):
    if not os.path.exists('./'+FolderPath):
        print(FolderPath, " not exist, try to create it.")
        os.makedirs('./' + FolderPath)

def SavePathToList():
    months = {
        #'Mar_2020': [3, 10, 32],
        #'Apr_2020': [4, 1, 31],
        #'Mai_2020': [5, 1, 32],
        #'Jun_2020': [6, 1, 31],
        #'Jul_2020': [7, 1, 32],
        'Aug_2020': [8, 1, 32],
        'Sept_2020': [9, 1, 31],
        'Okt_2020': [10, 1, 19]
    }
    PathList = []
    for month in months.keys():
        for diff in range(months[month][1],months[month][2]):
            date = datetime.date.today().replace(month=months[month][0], day=diff)
            pdfname = './data/'+month + '/'+ str(date) + '-de.pdf'
            PathList.append(pdfname)
    print(PathList)
    return PathList

def read_pdf(path,page):
    #qa!
    # wq:;
    # :::
    # path = './Mar_2020/2020-03-04-de.pdf'

    if os.path.exists(path):
        pdf = pdfplumber.open(path)
        page = pdf.pages[page]
        print(path[-17:] + " is already read!")
    else:
        print(path[-17:] + " is not found!")
        return None
    return page;

def extract_data(path):
    if os.path.exists(path):
        pdf = pdfplumber.open(path)
        if(int(path[-12:-10])>7):
            page = pdf.pages[2]
        else:
            page = pdf.pages[1]
        #print(page.extract_text())
        print(path[-17:] + " is already read!")
    else:
        print(path[-17:] + " is not found!")
        return None
    number = []
    bundesland = [
        "Baden-?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Bayern\s?\s(\d{1,3}.?\d{0,3})",
        "Berlin?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Brandenburg\s?\s(\d{1,3}.?\d{0,3})",
        "Bremen?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Hamburg\s\s(\d{1,3}.?\d{0,3})",
        "Hessen\s\s(\d{1,3}.?\d{0,3})",
        "Mecklenburg-?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Niedersachsen?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Nordrhein-?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Rheinland-?\D+\s?\s(\d{1,3}.?\d{,3})",
        "Saarland\s\s(\d{1,3}.?\d{0,3})",
        "Sachsen?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Sachsen-?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Schleswig-?\D+\s?\s(\d{1,3}.?\d{0,3})",
        "Thüringen\s\s(\d{1,3}.?\d{0,3})",
        "Gesamt?\D+\s?\s(\d{1,3}.?\d{0,3})"]
    if(page.extract_text()!=None):
        for land in bundesland:
            #print(page.extract_text())
            infektion = re.findall(land, page.extract_text())
            #print(infektion)
            if(infektion != []):
                number.append(infektion[0])
            else:
                for index in range(2,5):
                    otherpage =pdf.pages[index]
                    #print(otherpage.extract_text())
                    if(otherpage.extract_text()==None):
                        continue
                    infektion = re.findall(land, otherpage.extract_text())
                    #print(infektion)
                    if(infektion != []):
                        number.append(infektion[0])
                        break
                if(infektion==[]):
                    number.append('0')
    else:
        for index in range(0,16):
            number.append('0')
    print(number)
    return number

def SaveToExcel(FilePath,SheetName,PathList):
    #if not os.path.exists(FilePath):
        #print(FilePath, " not exist, try to create it.")
        #workbook = xlwt.Workbook(encoding='utf-8')
        #workbook.add_sheet(SheetName)
        #workbook.save(FilePath)

    workbook = xlwt.Workbook(encoding='utf-8')  # 新建工作簿
    sheet1 = workbook.add_sheet('numbers')
    bundesland = [
        "Baden-Württemberg",
        "Bayern",
        "Berlin",
        "Brandenburg",
        "Bremen",
        "Hessen",
        "Hamburg",
        "Mecklenburg-Vorpommern",
        "Niedersachsen",
        "Nordrhein-Westfalen",
        "Rheinland-Pfalz",
        "Saarland",
        "Schleswig-Holstein",
        "Sachsen",
        "Sachsen-Anhalt",
        "Thüringen"]
    for line in range(0,16):
        sheet1.write(line,0,bundesland[line])
    #workbook.save(FilePath)
    column = 1
    for path in PathList:
        sheet1.write(0,column,path[-17:-7])
        #page = read_pdf(path, 1)
        number = extract_data(path)
        for line in range(1, 17):
            sheet1.write(line, column, int(number[line - 1].replace('.','').replace(',','')))
        column+=1
        #if column == 20:
            #break
    workbook.save(FilePath)

def page(path):
    month = int(path[-12:-10])
    day = int(path[-9:-7])
    if(month ==3):
        destination =1
    else:
        destination =2
    return destination


def printnumber(PathList):
    for path in PathList:
        page = read_pdf(path, 1)
        number = extract_data(page)

PathList = SavePathToList()
#print(read_pdf('./Aug_2020/2020-08-31-de.pdf',3).extract_text())
#extract_data(read_pdf('./Aug_2020/2020-08-31-de.pdf',3))
#print(read_pdf('./data/Aug_2020/2020-08-07-de.pdf',3).extract_text())
extract_data('./data/Aug_2020/2020-08-31-de.pdf')
#extract_data('./data/Aug_2020/2020-08-07-de.pdf')
#(read_pdf('./Mar_2020/2020-03-04-de.pdf',1))
#printnumber(PathList)

#SaveToExcel('./Infektionsnumber.xls', 'numbers',PathList)


bundesland = [
    "Baden-?\D+\s?\s(\d{1,3}.?\d{0,3})",
    "Bayern\s?\s(\d{1,3}.?\d{0,3})",
    "Berlin\s?\s(\d{1,3}.?\d{0,3})",
    "Brandenburg\s\s(\d{1,3}.?\d{0,3})",
    "Bremen?\D+\s?\s(\d{1,3}.?\d{0,3})",
    "Hamburg\s\s(\d{1,3}.?\d{0,3})",
    "Hessen\s\s(\d{1,3}.?\d{0,3})",
    "Mecklenburg-?\D+\s?\s(\d{1,3}.?\d{0,3})",
    "Niedersachsen?\D+\s?\s(\d{1,3}.?\d{0,3})",
    "Nordrhein-?\D+\s?\s(\d{1,3}.?\d{0,3})",
    "Rheinland-Pfalz\s\s(\d{1,3}.?\d{,3})",
    "Saarland\s\s(\d{1,3}.?\d{0,3})",
    "Sachsen\s\s(\d{1,3}.?\d{0,3})",
    "Sachsen-Anhalt?\D+\s?\s(\d{1,3}.?\d{0,3})",
    "Schleswig-?\D+\s?\s(\d{1,3}.?\d{0,3})",
    "Thüringen\s\s(\d{1,3}.?\d{0,3})",
    "Gesamt?\D+\s?\s(\d{1,3}.?\d{0,3})"]
