from django.contrib import admin
from django.urls import path, include
from apps.common.views import HomeView,SignUpView, DashboardView, ProfileView,ProfileUpdateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from crudop.views import CrudView, CreateCrudUser, UpdateCrudUser
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'
    ),
         name='login'),
    path('crud/', CrudView.as_view(), name='crud'),
    path('crud/create', CreateCrudUser.as_view(), name='create-crud'),
    path('crud/update', UpdateCrudUser.as_view(), name='update-crud'),

    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ),
         name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),
 path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
          name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
