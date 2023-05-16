import gspread
from oauth2client.service_account import ServiceAccountCredentials


def auth():
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('misc/chat-384709-f24e97dc0a0b.json', scope)
    client = gspread.authorize(creds)
    return client


def read_message_preview():
    sheet = client.open('ЧАТ').sheet1
    print(sheet)
    rules = sheet.cell(17, 2).value
    print(rules)
    return rules


client = auth()