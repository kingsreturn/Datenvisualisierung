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

def generate_File(FilePath,SheetName):
    if not os.path.exists(FilePath):
        print(FilePath, " not exist, try to create it.")
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet(SheetName)
        workbook.save(FilePath)

def SavePathToList():
    months = {
        'Okt_2020': [10, 1, 19]
        #'Sept_2020': [9, 1, 31],
        #'Aug_2020': [8, 1, 32],
        #'Jul_2020': [7, 1, 32],
        #'Jun_2020': [6, 1, 31],
        #'Mai_2020': [5, 1, 32],
        #'Apr_2020': [4, 1, 31],
        #'Mar_2020': [3, 4, 32]
    }
    PathList = []
    for month in months.keys():
        for diff in range(months[month][1],months[month][2]):
            date = datetime.date.today().replace(month=months[month][0], day=diff)
            pdfname = './'+month + '/'+ str(date) + '-de.pdf'
            PathList.append(pdfname)
    print(PathList)
    return PathList

def read_pdf(path,page):
    #path = './Mar_2020/2020-03-04-de.pdf'
    bundesland = [
        "Berlin\s\s(\d+)",
        "Baden-Württemberg\s\s(\d+)",
        "Bayern\s\s(\d+)",
        "Bremen\s\s(\d+)",
        "Hessen\s\s(\d+)",
        "Hamburg\s\s(\d+)",
        "Mecklenburg-Vorpommern\s\s(\d+)",
        "Niedersachsen\s\s(\d+)",
        "Nordrhein-Westfalen\s\s(\d+)",
        "Rheinland-Pfalz\s\s(\d+)",
        "Saarland\s\s(\d+)",
        "Schleswig-Holstein\s\s(\d+)",
        "Sachsen\s\s(\d+)",
        "Thüringen\s\s(\d+)"]

    pdf = pdfplumber.open(path)

    page = pdf.pages[page]
    print(path[-17:] + " is already read!")
    return page;
    #print(page.extract_text())

def extract_data(page):
    number = []
    # number.append(re.findall(r"Baden-Württemberg\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Baden-Württemberg\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Bayern\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Berlin\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Brandenburg\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Bremen\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Hessen\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Hamburg\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Mecklenburg-Vorpommern\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Niedersachsen\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Nordrhein-Westfalen\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Rheinland-Pfalz\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Saarland\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Schleswig-Holstein\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Sachsen\s\s(\d+)", page.extract_text())[0])
    number.append(re.findall(r"Thüringen\s\s(\d+)", page.extract_text())[0])

    print(number)
    return number

SavePathToList()
generate_File('./Infektionsnumber.xls','numbers')
