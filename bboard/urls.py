from django.urls import path

from bboard.views import index, by_rubric, BbCreateView

app_name = 'bboard'

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, vals, name='by_rubric'),
    path('', index, name='index'),
]
   # re_path(r'^add/$', BbCreateView.as_view(), name='add'),
   # re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, name='by_rubric'),
    #re_path(r'^$', index, name='index'),
