from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import myapp.models
import os
from flask import Flask, render_template,send_file, json, request,redirect,session,jsonify
import time
from time import strftime
import sklearn
from sklearn import model_selection
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd


job_file = myapp.models.Joblist()
data_file = myapp.models.Datafileall()


def new_job(request):
    userId = request.GET.get("userid")
    jobName = request.GET.get("jobname")
    jobType = request.GET.get("jobtype")
    jobInfo = job_file.insert_job(userId, jobName, jobType)
    return HttpResponse(json.dumps(jobInfo), content_type='application/json')


def go_run(request):
    job_info = json.loads(request.body)
    run_res = []
    if job_info.get("jobType") == "1":
        if job_info.get("funcId") == 9:
            run_res = linear_regression(job_info)
    job_file.update_para(job_info, run_res)
    return HttpResponse(json.dumps("Success"), content_type='application/json')


def linear_regression(job_info):
    data_train, data_test, label_train, label_test = get_data(job_info.get("dataId"))
    linearReg = linear_model.LinearRegression()
    linearReg.fit(data_train, label_train)
    predict_res = linearReg.predict(data_test)
    mse = mean_squared_error(label_test, predict_res)
    rmse = np.sqrt(mse)
    linear_res = []
    linear_res.append({"name": "intercept", "value": linearReg.intercept_})
    linear_res.append({"name": "coefficient", "value": linearReg.coef_})
    linear_res.append({"name": "mse", "value": mse})
    linear_res.append({"name": "rmse", "value": rmse})
    return linear_res



def get_data(file_id):
    data_info = data_file.get_detail(file_id)
    data_path = data_info["DATA"][1]["value"]
    return get_file(data_path, data_info["DATA"][2]["value"], data_info["DATA"][3]["value"], data_info["DATA"][4]["value"])


def get_file(path, f_l, separate, weight):
    if (f_l == "1") and (separate == ","):
        data = pd.read_csv(path)
    elif (f_l == "0") and (separate == ","):
        data = pd.read_csv(path, header=None)
    data_feature, label = data.ix[:, 0:(data.shape[1]-2)], data.ix[:, data.shape[1]-1]
    string_to_int = preprocessing.LabelEncoder()
    string_to_int.fit(label)
    label_int = string_to_int.transform(label)
    data_feature_train, data_feature_test, label_train, label_test \
        = model_selection.train_test_split(data_feature, label_int, test_size=float(weight))
    return data_feature_train, data_feature_test, label_train, label_test



