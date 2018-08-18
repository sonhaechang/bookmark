from django.urls import path, re_path
from bookmark import views

# url 이름을 가지고 패턴을 찾고자할때 namespace를 사용할려면 app_name이 필수
app_name = 'bookmark'

urlpatterns = [
    # path('', views.bookmark_list, name='list'),
    re_path(r'^$', views.bookmark_list, name='list'),
    # path('write/', views.bookmark_create, name='create'),
    re_path(r'^write/$', views.bookmark_create, name='create'),
    # path('update/<int:pk>/', views.bookmark_update, name='update'),
    re_path(r'^update/(?P<pk>\d+)/$', views.bookmark_update, name='update'),
    # path('delete/<int:pk>', views.bookmark_delete, name='delete'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.bookmark_delete, name='delete'),
    # path('detail/<int:pk>/', views.bookmark_detail, name='detail'),
    re_path(r'^detail/(?P<pk>\d+)/$', views.bookmark_detail, name='detail'),
]
