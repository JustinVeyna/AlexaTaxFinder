'''
Created on Jun 26, 2017

@author: Justin Veyna
'''
"""
XLSX files taken from:
https://taxfoundation.org/?s=State%20Individual%20Income%20Tax%20Rates%20and%20Brackets
"""

from openpyxl import load_workbook
import SaveLoader as sl

BASE_FILE_NAME = 'data\State Individual Income Tax {}.xlsx'
YEARS = [2015, 2016, 2017]
FILE_NAMES = map(lambda x: BASE_FILE_NAME.format(x), YEARS)
STATE_DICT_FILE = "data\states.p"
MASTER_DICT_FILE = "data\master.p"
"r, s)"
ODD_STATES = ["Alaska", "Colorado", "Florida", "Illinois", "Indiana", "Michigan", "Nevada", "South Dakota", "Texas", "Washington", "Wyoming"]
STATE_DICT={'Ala.': 'Alabama', 'Mass.': 'Massachusetts', 'S.D.': 'South Dakota', 'Pa.': 'Pennsylvania', 'Miss.': 'Mississippi', 'Vt.': 'Vermont', 'S.C.': 'South Carolina', 'Tenn.': 'Tennessee', 'N.Y.': 'New York', 'Mont.': 'Montana', 'W.Va.': 'West Virginia', 'Iowa': 'Iowa', 'Ariz.': 'Arizona', 'D.C.': 'Washington DC', 'Ga.': 'Georgia', 'M.': 'Maryland', 'La.': 'Louisiana', 'N.J.': 'New Jersey', 'Nev.': 'Nevada', 'Minn.': 'Minnesota', 'N.D.': 'North Dakota', 'N.H.': 'New Hampshire', 'Ark.': 'Arkansas', 'Utah': 'Utah', 'N.C.': 'North Carolina', 'N.M.': 'New Mexico', 'Mo.': 'Missouri', 'Conn.': 'Connecticut', 'Maine': 'Maine', 'Va.': 'Virginia', 'Md.': 'Maruland', 'Wis.': 'Wisconsin', 'Ind.': 'Indiana', 'Mich.': 'Michigan', 'Wash.': 'Washington', 'Wyo.': 'Wyoming', 'R.I.': 'Rhode Island', 'Del.': 'Delaware', 'Colo.': 'Colorado', 'Alaska': 'Alaska', 'Hawaii': 'Hawaii', 'Tex.': 'Texas', 'Fla.': 'Florida', 'Calif.': 'California', 'Ore.': 'Oregon', 'Okla.': 'Oklahoma', 'Ill.': 'Illinois', 'Nebr.': 'Nebraska', 'Idaho': 'Idaho', 'Ky.': 'Kentucky', 'Ohio': 'Ohio', 'Kans.': 'Kansas'}

def get_val(sheet, col, row):
    alphabet = " ABCDEFGHIJKL"
    code = alphabet[col]+str(row)
    val = sheet[code].value
    return val

def parse_sheet(sheet, d):
    ret = dict()
    for i in range(3,300):
        val = get_val(sheet, 1, i)
        if val != None:
            state = d[get_val(sheet,1, i)]
            if state in ODD_STATES:
                ret[state] = {"individual": get_val(sheet, 2, i), "joint": get_val(sheet, 6, i)}
            else:
                ret[state] = parse_state(sheet, i, d)
    return ret
        
def parse_state(sheet, i, d):
    state = d[get_val(sheet,1, i)]
    individual = parse_brackets(sheet, i, 2)
    joint = parse_brackets(sheet, i, 6)
    return {"individual": individual, "joint": joint}
        
def parse_brackets(sheet, row, col):
    j = 0
    ret = []
    while j == 0 or get_val(sheet, 1, row+j) == None:
        percent = get_val(sheet, col, (row+j))
        bracket = get_val(sheet, col+2, (row+j))
        if percent == None:
            break
        ret.append((bracket, percent))
        j+=1
        if j>13:
            print(j)
    return ret

if __name__ == '__main__':
    master_dict = dict()
    d = STATE_DICT #relic
    for year in YEARS:
        filename = BASE_FILE_NAME.format(year)
        wb = load_workbook(filename = filename)
        sheet = wb['Sheet1']
        master_dict[year] = parse_sheet(sheet, d)
    print(repr(master_dict))
    sl.pickle_save(master_dict, MASTER_DICT_FILE)