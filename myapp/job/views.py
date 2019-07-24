from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import myapp.models
import os
from flask import Flask, render_template,send_file, json, request,redirect,session,jsonify
import time
from time import strftime


def new_job(request):
    userId = request.GET.get("userid")
    jobName = request.GET.get("jobname")
    jobType = request.GET.get("jobtype")
    job = myapp.models.Joblist()
    jobInfo = job.insert_job(userId, jobName, jobType)
    return HttpResponse(json.dumps(jobInfo), content_type='application/json')

