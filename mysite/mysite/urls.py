from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path('save_signup/', views.save_signup, name='save_signup'),
    path('save_signup/', views.save_signup, name='save_signup'),
    path('', views.Page5View, name='signup'),
    path('admin/', admin.site.urls),
    path('savevalue/<int:signup_id>/', views.save_value, name='savevalue'),
    path('savenovalue/<int:signup_id>/', views.save_novalue, name='savenovalue'),
    path('login/', views.login_action, name='login'),
    path('novalue/<int:signup_id>/', views.Page2View, name='novalue'),
    path('value/<int:signup_id>/', views.Page1View, name='value'),
    path('logout/', views.logout_action, name='logout'),
    path('login/success/', views.Page6View, name='login_success'),
    path('page/<int:signup_id>/', views.base_action, name='page'),
    path('page2/<int:signup_id>/', views.display_action, name='page2'),
    path('page3/<int:signup_id>/', views.selection_action, name='page3'),


    #path('signup/', views.Page5View, name='signup'),  # Use function-based view
    #path('save/', views.Page6View, name='save'),  # Use function-based view
    #path('save_signup/', views.save_signup, name='save_signup'),
    #path('generate-image/', views.generate_wordle_view, name='generate_image'),
    path('generate_wordle/<int:signup_id>/', views.generate_wordle_view, name='generate_wordle'),
    #path('save_wordle_entry/', views.save_wordle_entry, name='save_wordle_entry'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)