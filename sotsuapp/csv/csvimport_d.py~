import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "./sotsuprj.settings")

import csv

from ./sotsuapp.models import Diagnosis

reader = csv.reader(open("sample4swap.csv"))

for r in reader:
	print r
	d = Diagnosis()
	d.user_id = 1

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
