import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sotsuprj.settings")

import csv
from sotsuapp.models import Medicine

reader = csv.reader(open("sample4m.csv"))

for r in reader:
	print r
	m = Medicine()
	m.user_id = 2
	m.m_date = r[0]
	m.m_place = r[1]
	m.department = r[2]
	m.name = r[3]
	m.amount = r[4]
	m.days = r[5]
	m.category = r[6]
	m.save()

