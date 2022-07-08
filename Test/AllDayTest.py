from __future__ import print_function
from tabnanny import check
from tracemalloc import start
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import pickle
import datetime

# Import user func
from verify_format import timeFormatCheck
from verify_format import dateFormatCheck


def makeDateTime(date, time):
    datetime = date + "T" + time
    return datetime


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    calendarEvent = {
        'summary': "",
        'location': "",
        'description': "",
        'start': {
            'dateTime': "2022-05-28T20:00:00",
            'timeZone': 'Japan',
        },
        'end': {
            'dateTime': "2022-05-28T21:00:00",
            'timeZone': 'Japan',
        },
    }
    calendarEvent = {
        'summary': "",
        'location': "",
        'description': "",
        'start': {
            'date': "2022-05-28",
            'timeZone': 'Japan',
        },
        'end': {
            'date': "2022-05-28",
            'timeZone': 'Japan',
        },
    }
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    calendarEvent = service.events().insert(calendarId='ke37d1obkoa9ihbjghnc52ui54@group.calendar.google.com',
                                            body=calendarEvent).execute()
    print("""
---------------------------------------
Script succesfully!
event id = """+calendarEvent['id'] + """
---------------------------------------
""")


if __name__ == '__main__':
    main()
