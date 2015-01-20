from django.shortcuts import render_to_response, redirect, HttpResponse, render, get_object_or_404
#from models import Doctor, Patient
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import json, codecs
from sotsuapp.models import Diagnosis, Medicine

from django.core import serializers
from django.template import Context, loader

from django.core.paginator import Paginator

from datetime import *
import time


def home(request):
	return render_to_response('home.html', context_instance=RequestContext(request))

def login_view(request):
	user_id = request.POST['user_id']
	password = request.POST['password']
	user = authenticate(username=user_id, password=password)
	if user is not None:
		if user.is_active:
			auth_login(request, user)
			return redirect('/list')
		else:
			return redirect('/home')
	else:
		return HttpResponse("Couldn't login")

def plist(request):
	user = request.user
	if user.get_profile().role==0:
		re_list = user.get_profile().reration.users.all()
		#return render_to_response('list.html', {'re_list':re_list}, context_instance=RequestContext(request))
	else:
		#u_id = user.id
		#return redirect(userinfo(request, u_id))
		re_list = user.get_profile().reration.users.filter(id=user.id)
	
	rela_list = user.get_profile().reration.users.all()
	return render_to_response('list.html', {'re_list':re_list, 'rela_list':rela_list}, context_instance=RequestContext(request))		

	#return render_to_response('list.html', {'re_list':re_list}, context_instance=RequestContext(request))

@login_required
def logout_view(request):
    logout(request)
    return redirect('/home')

def userinfo(request, u_id):
	# to show a doctor patients' information

	diagnosis = Diagnosis.objects.filter(user=u_id)
	json_data = serializers.serialize('json', diagnosis, ensure_ascii=False)
	json_data = json_data.encode('utf_8')
	f = open("./sotsuapp/static/output_d.json", "w")
	f.write(json_data)
	f.close

	medicine = Medicine.objects.filter(user=u_id)
	p = Paginator(medicine, 2)
	cnt = p.count
	inpu = []

	for i in range(cnt):
		m_name = medicine[i].name	
		m_d = medicine[i].department

		# to change gantt's coloer with medicine category
		# I have to change better here after I collect information about medicine.
		m_c = int(medicine[i].category)
		c = "ganttBlue"
		if m_c == 1:
			c = "ganttRed"
		if m_c == 2:
			c = "ganttYellow"
		if m_c == 3:
			c = "ganttGreen"

		#transform datetime from UNIX time stamp
		date_f = int(time.mktime(medicine[i].m_date.timetuple()))
		date_t = date_f+50000
		date_t = date_t+ (int(medicine[i].days)-1)*86400  #86400=1day

		date_ff=str(date_f)
		date_tt=str(date_t)

		date_from = "/Date("+ date_ff+"000)/"
		date_to = "/Date("+ date_tt+"000)/"


		inpu.append({ "name":m_name,"values":[{ "id" : "b0", "from" : date_from
					, "to" : date_to, "desc" : "Link: medical record1", "label" : m_d,"customClass": c }]})


	f = codecs.open("./sotsuapp/static/output_m.json", "w", 'utf-8')
	f.write(json.dumps(inpu, separators=(',', ':'), ensure_ascii=False))	
	f.close
	
	return render(request, 'gantt.html')

def add_relation(request):
	#add_user = User.objects.filter(username=request.POST['user_id'])
	#add_user = User.objects.filter(id=4)
	#request.user.get_profile().reration.users.all()

	""" I could add myself ryuji
	relation = request.user.get_profile().reration.users
	relation.add(request.user)
	"""

	add_users = User.objects.filter(username=request.POST['user_id'])
	#print(add_users)

	if add_users.count() is not 0:
		print(add_users)
		request.user.get_profile().reration.users.add(add_users[0]) #user object
		return redirect('/list')

	else:
		return redirect('/list')

def add_data(request):
	# should make it better
	import os
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./../sotsuprj.settings")

	import csv

	from sotsuapp.models import Diagnosis

	reader = csv.reader(open("sample4swap.csv"))

	#print(reader)

	i=0;
	for r in reader:
		d = Diagnosis()
		d.user_id = 4

		d.date = r[0]
		d.place = r[1]

		d.tanpakuteisei = r[2]
		d.touteisei = r[3]
		d.urobirinogen = r[4]
		d.sennketu = r[5]
		d.birirubin = r[6]
		d.ketontai = r[7]
		d.hijyu = r[8]
		d.ph = r[9]

		d.wbc = r[10]
		d.rbc = r[11]
		d.hb = r[12]
		d.ht = r[13]
		d.kessyoubannsuu = r[14]

		d.soutanpaku = r[15]
		d.arubuminteiryou = r[16]
		d.ag = r[17]
		d.soubirirubin = r[18]
		d.ast = r[19]
		d.alt = r[20]
		d.ld = r[21]
		d.alp = r[22]
		d.ggtp = r[23]
		d.korinesuteraze = r[24]
		d.kettou = r[25]
		d.jds = r[26]
		d.ng = r[27]
		d.soukoresuteroru = r[28]
		d.ldl = r[29]
		d.hdl = r[30]
		d.tg = r[31]
		d.nyousan = r[32]
		d.bun = r[33]
		d.kureatinin = r[34]
		d.egrf = r[35]
		d.crp = r[36]
		d.cpk = r[37]
		d.amy = r[38]

		d.na = r[39]
		d.k = r[40]
		d.cl = r[41]
		d.ca = r[42]
		d.mg = r[43]
	
		d.syukketujikan = r[44]
		d.kasseikatoron = r[45]
		d.ptbyou = r[46]
		d.ptinr = r[47]
		d.fiburinogen = r[48]
		d.ddaima = r[49]
		d.fe = r[50]
		d.feritin = r[51]
	
		d.cea = r[52]
		d.ca199 = r[53]
		d.hukisokuseikoutai = r[54]

		d.save()
		i=i+1

		if i is 3:
			break
		else:
			pass
	return redirect('/list')

def search(request):

	search_user = User.objects.filter(username=request.POST['user_id'])
	#print(add_users)

	if search_user.count() is not 0:
		#print(add_users)
		#request.user.get_profile().reration.users.add(add_users[0]) #user object
		return render_to_response('list.html', {'re_list':search_user}, context_instance=RequestContext(request))		


	else:
		return redirect('/list')
	



