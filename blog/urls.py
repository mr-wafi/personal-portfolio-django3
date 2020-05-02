from django.urls import path
from . import views

app_name = 'blog'#why we add this becouse we want to tell django to check for blog id and id detials

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
    #here the <int:blog_id> means anything which cam after blog which is integer pass it here and after it came here this will
    #pass it to the views.detail page and we will check this in that page
]
