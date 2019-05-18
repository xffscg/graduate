from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import myapp.models
from flask import Flask, render_template,send_file, json, request,redirect,session,jsonify

# Create your views here.


def hello(request):
    s = 'helloWord!'
    html = '<html><head></head><body><h1> xxxxxxxxx</h1><p> %s </p></body></html>'
    return HttpResponse(html)


def data_filelist(request):
    # userName = 'hdp'
    # password = 'test'
    # userId = OutManager.OutputDataManager().authentication(userName, password)
    # if userId == -1:
    #     return jsonify({"status": "fail", "info": "用户验证失败"})
    # userId = str(userId)
    # dml = OutManager.OutputDataManager()
    data_file = myapp.models.Datafile()
    output = data_file.get_all_data_files_infolist()

    return HttpResponse(json.dumps(output), content_type='application/json')


def result_list(request):
    user_id = request.GET.get("userid")
    result_file = myapp.models.Result()
    output_result = result_file.get_result(user_id)
    return HttpResponse(json.dumps(output_result), content_type='application/json')


def model_list(request):
    user_id = request.GET.get("userid")
    model_file = myapp.models.Model()
    output_model = model_file.get_model(user_id)
    return HttpResponse(json.dumps(output_model), content_type='application/json')
