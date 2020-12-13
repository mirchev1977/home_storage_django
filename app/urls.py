from django.urls import path

from app.views.container import ContainerNewView, ContainersAllView, ContainerDeleteView, ContainerUpdateView
from app.views.location import LocationUpdateView, LocationsAllView
from app.views.test import test
from app.views.user import UserNewView, UserLoginView, UserDeleteView, UserUpdateView, UsersAllView, UserLogoutView

urlpatterns = [
    #user routes
    path('users/new', UserNewView.as_view(), name='user-new'),
    path('user/login', UserLoginView.as_view(), name='user-login'),
    path('users/<int:id>/delete', UserDeleteView.as_view(), name='user-delete'),
    path('users/<int:id>/update', UserUpdateView.as_view(), name='user-update'),
    path('users/all', UsersAllView.as_view(), name='user-all'),
    path('user/logout', UserLogoutView.as_view(), name='user-logout'),

    #location routes
    path('locations/all', LocationsAllView.as_view(), name='location-all'),
    path('locations/<int:id>/update', LocationUpdateView.as_view(), name='location-update'),

    #container routes
    path('containers/new', ContainerNewView.as_view(), name='container-new'),
    path('containers/all', ContainersAllView.as_view(), name='containers-all'),
    path('containers/<int:id>/delete', ContainerDeleteView.as_view(), name='container-delete'),
    path('container/<int:id>/update', ContainerUpdateView.as_view(), name='container-update'),

    #test
    path('', test, name='test'),
]
