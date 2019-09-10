from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import myapp.models
import os
from flask import Flask, render_template,send_file, json, request,redirect,session,jsonify
import time
from time import strftime

set_file = myapp.models.Datasetall()
data_file = myapp.models.Datafileall()


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
    data_file.insert_file(user_id, filename, current_path, set_name, separate, firstLine, create)
    if not set_file.query_set_name(user_id, set_name):
        set_file.insert_set(user_id, set_name, current_path1, create)
    if not os.path.exists(current_path1):
        os.mkdir(current_path1)
    with open(current_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return HttpResponse(json.dumps({'status': "success"}), content_type='application/json')


def data_filelist(request):
    user_id = request.GET.get("userid")
    set_list = set_file.get_all_set(user_id)
    index = 1
    if set_list["data_status"]:
        for item in set_list['DATA']:
            file_list = data_file.get_all_data_files_infolist(user_id, item['setname'])
            item['subFile'] = file_list
            item['index'] = str(index)
            index += 1
    return HttpResponse(json.dumps(set_list), content_type='application/json')


def get_data_detail(request):
    file_id = request.GET.get("fileid")
    result_detail = data_file.get_detail(file_id)
    return HttpResponse(json.dumps(result_detail), content_type='application/json')
