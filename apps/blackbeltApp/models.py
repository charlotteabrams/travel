from __future__ import unicode_literals
from ..loginRegister.models import User
from django.contrib import messages
from django.db import models
import datetime


class TravelManager(models.Manager):

	def isValidAdd(self, travelInfo, data):
		passflag = True
		errors = []
		if len(travelInfo['destination']) < 1:
			errors.append('Destination field cannot be blank.')
			passflag = False
		if len(travelInfo['description']) < 1:
			errors.append('Description field cannot be blank.')
			passflag = False
		travelfrom = datetime.datetime.strptime(travelInfo['travelfrom'], '%Y-%m-%d').date()
		travelto = datetime.datetime.strptime(travelInfo['travelto'], '%Y-%m-%d').date()
		today = datetime.date.today()
		if ((today.year, today.month, today.day) >= (travelfrom.year, travelfrom.month, travelfrom.day)):
			passflag = False
			errors.append("Travel from date must be after current date.")
		if ((travelto.year, travelto.month, travelto.day) <= (travelfrom.year, travelfrom.month, travelfrom.day)):
			passflag = False
			errors.append("Travel to date must be after current date.")
		if passflag==True:
			travel = self.create(destination = travelInfo['destination'], description = travelInfo['description'], travelfrom = travelInfo['travelfrom'], travelto = travelInfo['travelto'], creator = data['user'])
		return [passflag, errors]


class Travel(models.Model):
	destination = models.TextField(max_length=255)
	description = models.TextField(max_length=1000)
	travelto = models.DateField()
	travelfrom = models.DateField()
	creator = models.ForeignKey(User, related_name="creator")
	travellers = models.ManyToManyField(User, related_name="travellers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	travelManager = TravelManager()
	objects = models.Manager()