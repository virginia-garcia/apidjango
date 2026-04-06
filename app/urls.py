from django.urls import path
from .views import UserView, RoleView

urlpatterns = [
    # Rutas para ver todos o crear uno nuevo
    path("users/", UserView.as_view(), name="user-list"),
    path("roles/", RoleView.as_view(), name="role-list"),
    # Para modificar o eliminar uno específico usando su ID
    path("users/<int:pk>/", UserView.as_view(), name="user-detail"),
    path("roles/<int:pk>/", RoleView.as_view(), name="role-detail"),
]