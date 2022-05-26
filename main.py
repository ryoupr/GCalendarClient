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
from timeFormatCheck import timeFormatCheck
from dateFormatCheck import dateFormatCheck


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
            'dateTime': "",
            'timeZone': 'Japan',
        },
        'end': {
            'dateTime': "",
            'timeZone': 'Japan',
        },
    }

    summary = input("Summary:")
    location = input("Location:")
    description = input("Description:")

# Start date
    dateFlag = 0
    while dateFlag == 0:
        startDate = input("Start date(yyyy-mm-dd):")
        dateFlag = dateFormatCheck(startDate)
        if dateFlag == 1:
            break
        else:
            print("Invalid format. Please enter again.")

# Start date time
    timeFlag = 0
    while timeFlag == 0:
        startTime = input("Start time(hh:mm)")
        timeFlag = timeFormatCheck(startTime)
        if timeFlag == 1:
            startTime += ":00"
            break
        else:
            print("Invalid format. Please enter again.")
    startDateTime = makeDateTime(startDate, startTime)

# End date
    dateFlag = 0
    while dateFlag == 0:
        endDate = input("End date(yyyy-mm-dd):")
        dateFlag = dateFormatCheck(endDate)
        if dateFlag == 1:
            break
        else:
            print("Invalid format. Please enter again.")

# End date time
    timeFlag = 0
    while timeFlag == 0:
        endTime = input("End time(hh:mm):")
        timeFlag = timeFormatCheck(endTime)
        if timeFlag == 1:
            endTime += ":00"
            break
        else:
            print("Invalid format. Please enter again.")
            startDateTime = makeDateTime(startDate, startTime)
    endDatetime = makeDateTime(endDate, endTime)

# Add calendarEvent dict
    calendarEvent["summary"] = str(summary)
    calendarEvent["location"] = str(location)
    calendarEvent["description"] = str(description)
    calendarEvent["start"]["dateTime"] = str(startDateTime)
    calendarEvent["end"]["dateTime"] = str(endDatetime)
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
    input()


if __name__ == '__main__':
    main()
