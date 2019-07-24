from django.conf.urls import url, include
import myapp.views
import myapp.data.views
import myapp.job.views

urlpatterns = [
    url(r'hello$', myapp.views.hello, ),
    # data
    url(r'data/uploadDataFile$', myapp.data.views.uploadDataFile, ),
    url(r'data/get_file_list$', myapp.data.views.data_filelist, ),
    url(r'data/get_data_detail$', myapp.data.views.get_data_detail, ),
    # job
    url(r'job/new_job$', myapp.job.views.new_job, ),
    url(r'result_list$', myapp.views.result_list, ),
    url(r'model_list$', myapp.views.model_list, ),
    url(r'get_all$', myapp.views.get_all, ),
    url(r'user_register$', myapp.views.userRegister, ),
    url(r'user_login$', myapp.views.userLogin, ),
    # url(r'new_job$', myapp.views.new_job, ),
]
