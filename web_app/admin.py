import logging

from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseRedirect


