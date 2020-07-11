from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from .models import Event
from main.models import Appointments
from datetime import datetime, timedelta
import pytz

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.edit import UpdateView

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Fixmeet'
redirect_uri='http://127.0.0.1:8000/'

#Get OAuth2 credz
def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES, redirect_uri) #Redirect till fel URL ändå...
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

#Request calendar events
def main(request):
    
    creds = get_credentials()
    http = creds.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    appointment_id = request.POST.get('appid')
    
    app = Appointments.objects.get(id=appointment_id)
    start_time = str(app.details.start_time.year)+'-'+str(app.details.start_time.month)+'-'+str(app.details.start_time.day)+'T'+str(app.details.start_time.hour)+':'+str(app.details.start_time.minute)+':00-07:00'
    end_time = str(app.details.end_time.year)+'-'+str(app.details.end_time.month)+'-'+str(app.details.end_time.day)+'T'+str(app.details.end_time.hour)+':'+str(app.details.end_time.minute)+':00-07:00'
    event = {
    'summary': 'Fixmeet with '+app.details.user.name,
    'description': 'To meet '+ app.details.user.title,
    'start': {
    'dateTime': start_time,
    'timeZone': 'Asia/Calcutta',
    },
    'end': {
    'dateTime': end_time,
    'timeZone': 'Asia/Calcutta',
    },

    'attendees': [
    {'email': app.client.email},
    {'email': app.details.user.email},
    ],
    'reminders': {
    'useDefault': False,
    'overrides': [
    {'method': 'email', 'minutes': 24 * 60},
    {'method': 'popup', 'minutes': 10},
    ],
    },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    if event:
        app.added_to_google_calendar = True
        app.save()
    
    return redirect('/home/my-appointment')


#Class based view for updating values. Noooooo idea how this shit works (I do, called from urls.py)
if __name__ == '__main__':
    main()
#Class based view for updating values. Noooooo idea how this shit works (I do, called from urls.py)
class EventUpdate(UpdateView):
    model = Event
    
class EventUpdate(UpdateView):
    model = Event
    fields = ['saleDocLink','salePointsCreated','researchDone','internalMeetingCreated']