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



