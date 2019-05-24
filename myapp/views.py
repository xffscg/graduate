from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import myapp.models
import os
from flask import Flask, render_template,send_file, json, request,redirect,session,jsonify
import time
from time import strftime

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


def uploadDataFile(request):
    path = r'D:\bupt\upload'
    set_name = request.POST.get('name')
    print(set_name)
    firstLine = request.POST.get('firstLine')
    separate = request.POST.get('separate')
    user_id = request.POST.get('userId')
    file = request.FILES.get('file')
    current_path1 = path + "\\" + set_name
    current_path = path + "\\" + set_name + '\\' + file.name
    filename = file.name
    create = strftime("%Y%m%d%H%M%S")
    dataset_file = myapp.models.Datasetall()
    datafile_file = myapp.models.Datafileall()
    datafile_file.insert_file(user_id, filename, current_path, set_name, separate, firstLine, create)
    if not dataset_file.query_set_name(user_id, set_name):
        dataset_file.insert_set(user_id, set_name, current_path1, create)
    if not os.path.exists(current_path1):
        os.mkdir(current_path1)
    with open(current_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return HttpResponse(json.dumps({'status': "success"}), content_type='application/json')
