from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='homepage'),
    path('new_workspace', new_workspace, name='new_workspace'),
    path('workspaces', all_workspace, name='all_workspace'),
    path('workspace/<int:workspace_id>', open_workspace, name='workspace'),
]