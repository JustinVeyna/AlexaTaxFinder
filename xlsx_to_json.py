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
STATE_DICT={'N.M.': 'new mexico', 'Ala.': 'alabama', 'Idaho': 'idaho', 'Nebr.': 'nebraska', 'Ohio': 'ohio', 'Mich.': 'michigan', 'Colo.': 'colorado', 'Utah': 'utah', 'Tenn.': 'tennessee', 'Conn.': 'connecticut', 'Pa.': 'pennsylvania', 'Ky.': 'kentucky', 'Ill.': 'illinois', 'Okla.': 'oklahoma', 'Alaska': 'alaska', 'Vt.': 'vermont', 'Fla.': 'florida', 'Wash.': 'washington', 'Minn.': 'minnesota', 'Va.': 'virginia', 'Tex.': 'texas', 'R.I.': 'rhode island', 'S.D.': 'south dakota', 'N.D.': 'north dakota', 'Miss.': 'mississippi', 'N.J.': 'new jersey', 'S.C.': 'south carolina', 'Del.': 'delaware', 'Kans.': 'kansas', 'Mass.': 'massachusetts', 'Calif.': 'california', 'Hawaii': 'hawaii', 'D.C.': 'washington dc', 'Maine': 'maine', 'Ore.': 'oregon', 'W.Va.': 'west virginia', 'La.': 'louisiana', 'N.H.': 'new hampshire', 'N.C.': 'north carolina', 'N.Y.': 'new york', 'M.': 'maryland', 'Ind.': 'indiana', 'Wyo.': 'wyoming', 'Mont.': 'montana', 'Mo.': 'missouri', 'Wis.': 'wisconsin', 'Ark.': 'arkansas', 'Ga.': 'georgia', 'Iowa': 'iowa', 'Ariz.': 'arizona', 'Nev.': 'nevada', 'Md.': 'maruland'}


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