from django.db import models
from django.contrib.auth.models import  User

class Relation(models.Model):
	name = models.CharField(max_length=20)
	users = models.ManyToManyField(User)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	role = models.IntegerField()
	reration = models.ForeignKey(Relation)

class Diagnosis(models.Model):
	user = models.ForeignKey(User)

	date = models.DateField()
	place = models.CharField(max_length=20)

	tanpakuteisei = models.CharField(max_length=20)
	touteisei = models.CharField(max_length=20)
	urobirinogen = models.CharField(max_length=20)
	sennketu = models.CharField(max_length=20)
	birirubin = models.CharField(max_length=20)
	ketontai = models.CharField(max_length=20)
	hijyu = models.CharField(max_length=20)
	ph = models.CharField(max_length=20)

	wbc = models.CharField(max_length=20)
	rbc = models.CharField(max_length=20)
	hb = models.CharField(max_length=20)
	ht = models.CharField(max_length=20)
	kessyoubannsuu = models.CharField(max_length=20)

	soutanpaku = models.CharField(max_length=20)
	arubuminteiryou = models.CharField(max_length=20)
	ag = models.CharField(max_length=20)
	soubirirubin = models.CharField(max_length=20)
	ast = models.CharField(max_length=20)
	alt = models.CharField(max_length=20)
	ld = models.CharField(max_length=20)
	alp = models.CharField(max_length=20)
	ggtp = models.CharField(max_length=20)
	korinesuteraze = models.CharField(max_length=20)
	kettou = models.CharField(max_length=20)
	jds = models.CharField(max_length=20)
	ng = models.CharField(max_length=20)
	soukoresuteroru = models.CharField(max_length=20)
	ldl = models.CharField(max_length=20)
	hdl = models.CharField(max_length=20)
	tg = models.CharField(max_length=20)
	nyousan = models.CharField(max_length=20)
	bun = models.CharField(max_length=20)
	kureatinin = models.CharField(max_length=20)
	egrf = models.CharField(max_length=20)
	crp = models.CharField(max_length=20)
	cpk = models.CharField(max_length=20)
	amy = models.CharField(max_length=20)

	na = models.CharField(max_length=20)
	k = models.CharField(max_length=20)
	cl = models.CharField(max_length=20)
	ca = models.CharField(max_length=20)
	mg = models.CharField(max_length=20)

	syukketujikan = models.CharField(max_length=20)
	kasseikatoron = models.CharField(max_length=20)
	ptbyou = models.CharField(max_length=20)
	ptinr = models.CharField(max_length=20)
	fiburinogen = models.CharField(max_length=20)
	ddaima = models.CharField(max_length=20)
	fe = models.CharField(max_length=20)
	feritin = models.CharField(max_length=20)

	cea = models.CharField(max_length=20)
	ca199 = models.CharField(max_length=20)
	hukisokuseikoutai = models.CharField(max_length=20)

	def __unicode__(self):
		return self.date

class Medicine(models.Model):
	user = models.ForeignKey(User)

	m_date = models.DateField()
	m_place = models.CharField(max_length=20)
	department = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	amount = models.CharField(max_length=20)
	days = models.FloatField()
	category = models.FloatField()

	def __unicode__(self):
		return self.name

