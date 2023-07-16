from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.db.models import Q

from .models import Contributors, Projects


class FullAccess(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author_user == request.user:
            return True
        return False


class ContributorReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return False


class ContributorProjectReadOnly(BasePermission):

    def has_permission(self, request, view):
        current_project = int(view.kwargs["project_pk"])

        current_user_contribution = Contributors.objects.filter(Q(
            author_user=request.user))

        current_user_contribution_projects = current_user_contribution.values_list(
            "project", flat=True).distinct()

        current_user_author_contribution_projects = Projects.objects.filter(
            Q(author_user=request.user) | Q(id__in=current_user_contribution_projects)).values_list(
            "id", flat=True).distinct()

        if request.user.is_authenticated and current_project in current_user_author_contribution_projects:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return False
