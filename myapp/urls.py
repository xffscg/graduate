from django.conf.urls import url, include
import myapp.views

urlpatterns = [
    url(r'hello$', myapp.views.hello, ),
    url(r'get_file_list$', myapp.views.data_filelist, ),
    url(r'result_list$', myapp.views.result_list, ),
    url(r'model_list$', myapp.views.model_list, ),
]
