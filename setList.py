from openpyxl import load_workbook

def get_engWords():
    engWords = []                                 # List of only english words

    wb = load_workbook(filename='words_db.xlsx')
    sheet = wb.active

    for row in sheet.rows:
        engWords.append(str(row[0].value))
        
    return engWords