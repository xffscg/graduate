from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import myapp.models
import os
from flask import Flask, render_template,send_file, json, request,redirect,session,jsonify
import time
from time import strftime

# Create your views here.


user_set = myapp.models.User()
result_file = myapp.models.Result()
model_file = myapp.models.Model()
set_file = myapp.models.Datasetall()
data_file = myapp.models.Datafileall()
alg_file = myapp.models.Algo()


def hello(request):
    s = 'helloWord!'
    html = '<html><head></head><body><h1> xxxxxxxxx</h1><p> %s </p></body></html>'
    return HttpResponse(html)


def userRegister(request):
    user_name = request.GET.get("username")
    password = request.GET.get("password")
    register_result = user_set.register_user(user_name, password)
    return HttpResponse(json.dumps(register_result), content_type='application/json')


def userLogin(request):
    user_name = request.GET.get("username")
    password = request.GET.get("password")
    login_result = user_set.login_user(user_name, password)
    return HttpResponse(json.dumps(login_result), content_type='application/json')


def result_list(request):
    user_id = request.GET.get("userid")
    output_result = result_file.get_result(user_id)
    return HttpResponse(json.dumps(output_result), content_type='application/json')


def model_list(request):
    user_id = request.GET.get("userid")
    output_model = model_file.get_model(user_id)
    return HttpResponse(json.dumps(output_model), content_type='application/json')


def get_all(request):
    user_id = request.GET.get("userid")
    output = dict()
    output["data_status"] = True
    output["DATA"] = dict()
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
        }]}, {
        "Name": "聚类",
        "index": "2-4",
        "subFile": [{
            "id": 11,
            "type": "alg",
            "fileName": "K-Means"
        }, {
            "id": 12,
            "type": "alg",
            "fileName": "层次聚类"
        }]}]
    index = 1
    if set_list["data_status"]:
        for item in set_list['DATA']:
            file_list = data_file.get_all_data_files_infolist(user_id, item['setname'])
            item['subFile'] = file_list
            item['index'] = "1-" + str(index)
            index += 1
        list1["datalist"] = set_list['DATA']
    model_file = myapp.models.Model()
    output_model = model_file.get_model(user_id)
    index = 1
    if output_model["data_status"]:
        for item in output_model['DATA']:
            item['index'] = "3-" + str(index)
            item['dtype'] = 'model'
            index += 1
        list1["modellist"] = output_model['DATA']
    output['DATA'] = list1
    return HttpResponse(json.dumps(output), content_type='application/json')


def get_alg_detail(request):
    alg_id = request.GET.get("algid")
    alg_res = alg_file.get_alg_para(alg_id)
    return HttpResponse(json.dumps(alg_res), content_type='application/json')








