# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
import json
from datetime import date, datetime


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class Algo(models.Model):
    id = models.IntegerField(primary_key=True)
    algopara = models.CharField(db_column='algoPara', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'algo'

    def get_alg_para(self, alg_id):
        all_rows = Algo.objects.filter(id=alg_id)
        alg_res = dict()
        if all_rows is not None and len(all_rows) > 0:
            alg_res["status"] = True
            alg_res["DATA"] = []
            para = json.loads(all_rows[0].algopara)
            for item in para:
                alg_res["DATA"].append(item)
        return alg_res


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Datafile(models.Model):
    jobid = models.IntegerField(db_column='jobId', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    isdeleted = models.IntegerField(blank=True, null=True)
    deletedon = models.DateTimeField(blank=True, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    separate = models.CharField(max_length=10, blank=True, null=True)
    firstline = models.CharField(db_column='firstLine', max_length=5, blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(max_length=5, blank=True, null=True)
    cat_list = models.CharField(max_length=100, blank=True, null=True)
    num_list = models.CharField(max_length=100, blank=True, null=True)
    weights = models.CharField(max_length=10, blank=True, null=True)
    datasetname = models.CharField(db_column='datasetName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firststatus = models.IntegerField(db_column='firstStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datafile'

    def get_all_data_files_infolist(self):
        all_rows = Datafile.objects.filter(userid=4)
        output = dict()
        if all_rows is not None and len(all_rows) > 0:
            output["data_status"] = True
            output["DATA"] = []
            for row in all_rows:
                row_dict = dict()

                row_dict["jobId"] = row.jobid
                row_dict["path"] = row.path
                row_dict["filename"] = row.filename
                row_dict["createdon"] = row.createdon
                output["DATA"].append(row_dict)
        else:
            output["data_status"] = False

        return output


class Datafileall(models.Model):
    fileId = models.IntegerField(db_column='fileId', primary_key=True)  # Field name made lowercase.
    userId = models.IntegerField(db_column='userId', blank=True, null=True)
    filename = models.TextField(db_column='filename', blank=True, null=True)
    path = models.TextField(db_column='path', blank=True, null=True)
    setname = models.CharField(db_column='setname', max_length=40, blank=True, null=True)  # Field name made lowercase.
    separate = models.CharField(max_length=10, blank=True, null=True)
    first = models.CharField(max_length=10, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createtime', max_length=40, blank=True, null=True)
    testWeight = models.FloatField(db_column='testWeight')

    class Meta:
        managed = False
        db_table = 'datafileall'

    def get_all_data_files_infolist(self, user_id, set_name):
        all_rows = Datafileall.objects.filter(userId=user_id, setname=set_name)
        output = []
        if all_rows is not None and len(all_rows) > 0:
            for row in all_rows:
                row_dict = dict()
                row_dict["id"] = row.fileId
                row_dict["fileName"] = row.filename
                row_dict["type"] = 'data'

                output.append(row_dict)
        return output

    def insert_file(self, user_id, filename, path, setname, separate, first, createtime):
        Datafileall.objects.create(userId=user_id, filename=filename, path=path, setname=setname, separate=separate, first=first, createtime=createtime)

    def get_detail(self, file_id):
        all_rows = Datafileall.objects.filter(fileId=file_id)
        file_detail = dict()
        if all_rows is not None and len(all_rows) > 0:
            file_detail["status"] = True
            file_detail["DATA"] = []
            file_detail["DATA"].append({"name": "filename", "value": all_rows[0].filename})
            file_detail["DATA"].append({"name": "path", "value": all_rows[0].path})
            file_detail["DATA"].append({"name": "firstLine", "value": all_rows[0].first})
            file_detail["DATA"].append({"name": "separate", "value": all_rows[0].separate})
            file_detail["DATA"].append({"name": "testWeight", "value": all_rows[0].testWeight})
        else:
            file_detail["status"] = False
        return file_detail


class Dataset(models.Model):
    userId = models.IntegerField(db_column='userId')  # Field name made lowercase.
    datasetName = models.CharField(db_column='datasetName', max_length=20)  # Field name made lowercase.
    datatype = models.CharField(db_column='dataType', max_length=20)  # Field name made lowercase.
    datapath = models.CharField(db_column='dataPath', max_length=100)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dataset'


class Datasetall(models.Model):
    userId = models.IntegerField(db_column='userId',primary_key=True)  # Field name made lowercase.
    setname = models.CharField(db_column='setname', max_length=100)  # Field name made lowercase.
    path = models.CharField(db_column='path', max_length=100)  # Field name made lowercase.
    createtime = models.CharField(db_column='createtime', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datasetall'

    def query_set_name(self, user_id, set_name):
        query = Datasetall.objects.filter(userId=user_id, setname=set_name)
        if len(query) > 0:
            return True
        else:
            return False

    def insert_set(self, user_id, set_name, path, create):
        Datasetall.objects.create(userId=user_id, setname=set_name, path=path, createtime=create)

    def get_all_set(self, user_id):
        all_rows_set = Datasetall.objects.filter(userId=user_id)
        output_set = dict()
        if all_rows_set is not None and len(all_rows_set) > 0:
            output_set["data_status"] = True
            output_set["DATA"] = []
            for row in all_rows_set:
                row_dict = dict()
                row_dict["setname"] = row.setname
                output_set["DATA"].append(row_dict)
        else:
            output_set["data_status"] = False
        return output_set


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Execution(models.Model):
    fileid = models.IntegerField(blank=True, null=True)
    sessionid = models.IntegerField(blank=True, null=True)
    arguments = models.TextField(blank=True, null=True)
    print_output = models.TextField(blank=True, null=True)
    outputlog = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    filename = models.CharField(max_length=30, blank=True, null=True)
    filecontent = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'execution'


class Files(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    deletedon = models.DateTimeField(blank=True, null=True)
    modifiedon = models.DateTimeField(blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    isdeleted = models.IntegerField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    codepath = models.CharField(db_column='codePath', max_length=225, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'files'


class Job(models.Model):
    jobid = models.AutoField(db_column='jobId', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    jobname = models.CharField(db_column='jobName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    property = models.IntegerField(blank=True, null=True)
    print_log = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class Joblist(models.Model):
    jobId = models.AutoField(db_column='jobId', primary_key=True)  # Field name made lowercase.
    userId = models.IntegerField(db_column='userId')  # Field name made lowercase.
    jobName = models.CharField(db_column='jobName', max_length=255)  # Field name made lowercase.
    jobStatus = models.IntegerField(db_column='jobStatus')
    jobType = models.IntegerField(db_column='jobType')
    dataId = models.IntegerField(db_column='dataId')
    dataPara = models.CharField(db_column='dataPara', max_length=255)
    funcId = models.IntegerField(db_column='funcId')
    funcPara = models.CharField(db_column='funcPara', max_length=255)
    result = models.TextField(db_column='result')

    class Meta:
        managed = False
        db_table = 'joblist'

    def insert_job(self, userId, jobName, jobType):
        Joblist.objects.create(userId=userId, jobName=jobName, jobStatus=0, jobType=jobType)
        job_all = Joblist.objects.all()
        job_id = len(job_all)
        new_job_res = dict()
        new_job_res["status"] = True
        new_job_res["jobId"] = job_id
        return new_job_res

    def update_para(self, job_info, res):
        Joblist.objects.filter(jobId=job_info.get("jobId"))\
            .update(jobStatus=2, dataId=job_info.get("dataId"), dataPara=job_info.get("dataPara"),
                    funcId=job_info.get("funcId"), funcPara=job_info.get("funcPara"), result=res)
        return True


class Model(models.Model):
    userId = models.IntegerField(db_column='userId')  # Field name made lowercase.
    jobid = models.IntegerField(db_column='jobId')  # Field name made lowercase.
    modelname = models.CharField(db_column='modelName', max_length=100)  # Field name made lowercase.
    algoname = models.CharField(db_column='algoName', max_length=50)  # Field name made lowercase.
    status = models.IntegerField()
    modelpath = models.TextField(db_column='modelPath')  # Field name made lowercase.
    time = models.CharField(max_length=20, blank=True, null=True)
    algopara = models.CharField(db_column='algoPara', max_length=250, blank=True, null=True)  # Field name made lowercase.
    createtime = models.CharField(db_column='createTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datasetname = models.CharField(db_column='datasetName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'model'

    def get_model(self, user_id):
        all_rows_model = Model.objects.filter(userId=user_id)
        output_model = dict()
        if all_rows_model is not None and len(all_rows_model) > 0:
            output_model["data_status"] = True
            output_model["DATA"] = []
            for row in all_rows_model:
                row_dict = dict()
                row_dict["jobId"] = row.jobid
                row_dict["modelname"] = row.modelname
                row_dict["algoname"] = row.algoname
                row_dict["datasetname"] = row.datasetname
                row_dict["modelpath"] = row.modelpath
                row_dict["createdon"] = row.createtime
                row_dict["time"] = row.time
                row_dict["status"] = row.status
                output_model["DATA"].append(row_dict)
        else:
            output_model["data_status"] = False

        return output_model


class Result(models.Model):
    userId = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    jobid = models.IntegerField(db_column='jobId', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(max_length=200, blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result'

    def get_result(self, user_id):
        all_rows_result = Result.objects.filter(userId=user_id)
        output_result = dict()
        if all_rows_result is not None and len(all_rows_result) > 0:
            output_result["data_status"] = True
            output_result["DATA"] = []
            for row in all_rows_result:
                row_dict = dict()
                row_dict["jobId"] = row.jobid
                row_dict["path"] = row.path
                row_dict["filename"] = row.filename
                row_dict["createdon"] = row.createdon
                output_result["DATA"].append(row_dict)
        else:
            output_result["data_status"] = False

        return output_result


class User(models.Model):
    userId = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', unique=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'

    def find_user(self):
        all = Result.objects.filter(userId=4)
        print(len(all))
        return all

    def register_user(self, username, password):
        check_result = User.objects.filter(username=username)
        output_register = dict()
        if check_result is not None and len(check_result) > 0:
            output_register["status"] = "fail"
            output_register["error"] = "用户名已存在"
        else:
            User.objects.create(username=username, password=password)
            output_register["status"] = "success"
        return output_register

    def login_user(self, username, password):
        check_result = User.objects.filter(username=username, password=password)
        output_login = dict()
        if check_result is not None and len(check_result) > 0:
            output_login["status"] = "success"
            print(check_result[0])
            output_login["userId"] = check_result[0].userId
        else:
            output_login["status"] = "fail"
            output_login["error"] = "用户名与密码不匹配"
        return output_login

