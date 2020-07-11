
from django.shortcuts import render,redirect
from .models import FreeTime,Appointments,Meetings
from registration.models import MyUser
import datetime

from django.http import Http404


def home (request):
	if request.user.is_active and request.user.is_authenticated:
		pass
	else:
		return redirect('/login/')
	context={}
	hourlist=[]
	minutelist=[]
	for i in range(0,60):
		minutelist.append(i)
	for i in range(0,24):
		hourlist.append(i)
	context['hourlist']=hourlist
	context['minutelist']=minutelist
	return render(request,'main/home.html',context)

def add_slot(request):
	context ={}
	if request.user.is_authenticated and request.user.is_active:
		pass
	else:
		return redirect('/login/')

	if request.method == 'POST':
		pass
	else:
		return redirect("/")
	try:
		selected_date = request.POST.get('datepicker').split('/')
		selected_time = request.POST.get('time').split(':')

		starting_time = datetime.datetime(int(selected_date[2]),int(selected_date[0]),int(selected_date[1]),int(selected_time[0])
			,int(selected_time[1]))
		today = datetime.datetime.now()
		delta = datetime.timedelta(hours=1)
		ending_time = starting_time + delta
		app = FreeTime.objects.filter(user = MyUser.objects.get(id=request.user.id),start_time__range=[starting_time-delta,
		 ending_time])
		if len(app)==0:
			FreeTime.objects.create(user = MyUser.objects.get(id=request.user.id),start_time = starting_time,end_time = ending_time)
			context['message']='valid'
			return render(request,'main/home.html',context)
		else:
			context['message']='Slot is collides with another'
			return render(request,'main/home.html',context)
	except:
		context['message']='Not valid time'
		return render(request,'main/home.html',context)

		


def search(request):
	if request.user.is_active and request.user.is_authenticated:
		pass
	else:
		return redirect("/registration/user_login")

	try:
		search = request.GET['search']
		if(search==""):
			return render(request,'main/search.html',)
	except:
		return render(request,'main/search.html',)
	
	search = request.GET['search']
	search_result = MyUser.objects.filter(name__istartswith=search,is_active=True).exclude(id=request.user.id).order_by('-score').values()
	search_result = [entry for entry in search_result]
	context = {}
	context['search_result'] = search_result
	return render(request,'main/search.html',context)


def profile(request,userid=-1):
	if request.user.is_active and request.user.is_authenticated:
		pass
	else:
		return redirect("/registration/user_login")
	if userid==-1:
		return render(request,'main/selfprofile.html')

	try:
		user_profile_detail = MyUser.objects.get(id=userid)
	except MyUser.DoesNotExist:
		raise Http404("User does not exist")

	user_profile_detail = MyUser.objects.get(id=userid)
	freeslots = FreeTime.objects.filter(user = MyUser.objects.get(id=user_profile_detail.id),appointed=False
		,start_time__gte=datetime.datetime.now()).values()
	freeslots = [entry for entry in freeslots]
	context = {}
	if(len(freeslots)>0):
		context['freeslots']=freeslots
	else:
		context['busy']=True
	context['profile_user']=user_profile_detail

	return render(request,'main/othersprofile.html',context)



def book_appointments(request):
	if not request.user.is_authenticated:
		return redirect('/registration/user_login/')
	if request.method=='POST':
		pass
	else:
		return render(request,'main/home.html')

	slotid = request.POST.get('slot')
	details=FreeTime.objects.get(id=slotid)
	try:
		Appointments.objects.get(details=details)
	except Appointments.DoesNotExist:
		appointment = Appointments.objects.create(client = MyUser.objects.get(id=request.user.id),details=details)
		details.appointed = True
		details.save()
		Meetings.objects.create(provider=MyUser.objects.get(id=details.user.id),details=appointment)

	'''
	if(x.AMPM == "PM"):
		x.time = (x.time+12)%24
	event = {
	'summary': 'calandaly meeting',
	
	'start': {
	'dateTime': str(date(x.date.year,x.date.month,x.date.day))+'T'+str(time(x.time,0,0)),
	'timeZone':'Asia/Kolkata',
	},
	'end': {
	'dateTime': (str(date(x.date.year,x.date.month,x.date.day))+'T'+str(time(x.time+1,0,0))),
	'timeZone':'Asia/Kolkata',
	}
	}

	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('calendar', 'v3', http=http)

    #now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
	cest = pytz.timezone('Asia/Kolkata')
	now = datetime.now(tz=cest) 
	timeMax = datetime(year=now.year, month=now.month, day=now.day, tzinfo=cest) + timedelta(days=90)
	timeMax = timeMax.isoformat()
	now = now.isoformat()
	print('Getting the upcoming 15 events')
	event = service.events().insert(calendarId='primary', body=event).execute()
	eventsResult = service.events().list(
	    calendarId='primary', timeMin=now, timeMax=timeMax, singleEvents=True,
	    orderBy='startTime').execute()
	events = eventsResult.get('items', [])

	#Create and populate list with events
	p = []
	if not events:
	    print('No upcoming events found.')
	for ev in events:
	    if not Event.objects.filter(uniqueTempKey=ev['id']):
	        d = 'No description'
	        try:
	            d= ev['description']
	        except:
	            print ('No description in dictionary for this object')
	        p.append(Event(uniqueTempKey=ev['id'], title=ev['summary'], body=d, date=ev['start'].get('dateTime', ev['start'].get('date'))))

	#Bulk create in sqlite db
	Event.objects.bulk_create(p)
	res = Event.objects.all()'''
	return redirect('/home/',)





def my_appointments(request):
	if request.user.is_authenticated and request.user.is_active:
		pass
	else:
		return redirect('/registration/user_login/')
	detail = FreeTime.objects.filter(start_time__gte=datetime.datetime.now(),appointed=True)
	appointment = Appointments.objects.filter(client = MyUser.objects.get(id=request.user.id),
		details__in=detail)

	meeting = Meetings.objects.filter(provider=MyUser.objects.get(id=request.user.id),
		details__in=Appointments.objects.filter(details__in=detail))
	appointment = [entry for entry in appointment] 
	context={}
	if(len(appointment)==0):
		context['no_appointment']="No future appointment"
	else:
		context['appointment']=appointment
	
	meeting = [entry for entry in meeting] 
	if(len(meeting)==0):
		context['no_meeting']="No future Meetings"
	else:
		context['meeting'] = meeting
	return render(request,'main/myappointment.html',context)

def change_password(request):
	if request.user.is_authenticated:
		pass
	else:
		return redirect('/login/')
	if request.POST:
		pass
	else:
		return render(request,'main/changepassword.html')

	
