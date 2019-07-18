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


def userRegister(request):
    user_name = request.GET.get("username")
    password = request.GET.get("password")
    user_set = myapp.models.User()
    register_result = user_set.register_user(user_name, password)
    return HttpResponse(json.dumps(register_result), content_type='application/json')


def userLogin(request):
    user_name = request.GET.get("username")
    password = request.GET.get("password")
    user_set = myapp.models.User()
    login_result = user_set.login_user(user_name, password)
    return HttpResponse(json.dumps(login_result), content_type='application/json')


def data_filelist(request):
    user_id = request.GET.get("userid")
    set_file = myapp.models.Datasetall()
    data_file = myapp.models.Datafileall()
    set_list = set_file.get_all_set(user_id)
    index = 1
    for item in set_list['DATA']:
        file_list = data_file.get_all_data_files_infolist(user_id, item['setname'])
        item['subFile'] = file_list
        item['index'] = str(index)
        index += 1
    return HttpResponse(json.dumps(set_list), content_type='application/json')


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


def get_all(request):
    user_id = request.GET.get("userid")
    output = dict()
    output["data_status"] = True
    output["DATA"] = dict()
    set_file = myapp.models.Datasetall()
    data_file = myapp.models.Datafileall()
    set_list = set_file.get_all_set(user_id)
    list1 = dict()
    list1["datalist"] = []
    list1["modellist"] = []
    list1["alglist"] = []
    list1["alglist"] = [{
        "Name": "关联",
        "index": "2-1",
        "subFile": [{
            "id": 1,
            "type": "alg",
            "fileName": "Cor协相关算法"
        }, {
            "id": 2,
            "type": "alg",
            "fileName": "Apriori"
        }]
    }, {
        "Name": "分类",
        "index": "2-2",
        "subFile": [{
            "id": 3,
            "type": "alg",
            "fileName": "决策树分类"
        }, {
            "id": 4,
            "type": "alg",
            "fileName": "支持向量机"
        }, {
            "id": 5,
            "type": "alg",
            "fileName": "朴素贝叶斯"
        }, {
            "id": 6,
            "type": "alg",
            "fileName": "PU分类"
        }]
    }, {
        "Name": "回归",
        "index": "2-3",
        "subFile": [{
            "id": 7,
            "type": "alg",
            "fileName": "逻辑回归"
        }, {
            "id": 8,
            "type": "alg",
            "fileName": "迭代回归"
        }, {
            "id": 9,
            "type": "alg",
            "fileName": "线性回归"
        }, {
            "id": 10,
            "type": "alg",
            "fileName": "岭回归"
        }]}]
    index = 1
    for item in set_list['DATA']:
        file_list = data_file.get_all_data_files_infolist(user_id, item['setname'])
        item['subFile'] = file_list
        item['index'] = "1-" + str(index)
        index += 1
    list1["datalist"] = set_list['DATA']
    model_file = myapp.models.Model()
    output_model = model_file.get_model(user_id)
    index = 1
    for item in output_model['DATA']:
        item['index'] = "3-" + str(index)
        item['dtype'] = 'model'
        index += 1
    list1["modellist"] = output_model['DATA']
    output['DATA'] = list1
    return HttpResponse(json.dumps(output), content_type='application/json')




