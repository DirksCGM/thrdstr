from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from .views import (
    index,
    SignupView,
    edit_profile_view,
    groups,
    groups_user,
    groups_create,
    groups_edit,
    groups_delete,
    groups_subscribe,
    groups_unsubscribe,
)

admin.autodiscover()

urlpatterns = [
    # Root URLs
    path(r"", index, name="index"),
    path("admin/", admin.site.urls),
    # User URLs
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # This is for the login and logout views
    path("accounts/signup/", SignupView.as_view(), name="signup"),
    path("accounts/profile/", edit_profile_view, name="profile"),
    # Groups URLs
    path("groups/", groups, name="groups"),
    path("groups/user/", groups_user, name="groups_user"),
    path("groups/create/", groups_create, name="groups_create"),
    path("groups/edit/<int:pk>/", groups_edit, name="groups_edit"),
    path("groups/delete/<int:pk>/", groups_delete, name="groups_delete"),
    path("groups/subscribe/<int:pk>/", groups_subscribe, name="groups_subscribe"),
    path("groups/unsubscribe/<int:pk>/", groups_unsubscribe, name="groups_unsubscribe"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
