from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
]