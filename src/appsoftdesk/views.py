from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Projects, Contributors, Issues, Comments

from .serializers import ProjectsListSerializer, \
    ProjectsDetailSerializer, \
    ContributorsSerializer, \
    IssuesSerializer, \
    CommentsSerializer

from .permissions import ContributorReadOnly, FullAccess, ContributorProjectReadOnly, \
    AuthorDeleteContributor


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsListSerializer
    detail_serializer_class = ProjectsDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve" and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):

        "Définir dans le projet qui est l'auteur ou le contributeur"
        current_user_contributor = Contributors.objects.filter(
            Q(author_user=self.request.user)
        )

        contributor_projet = current_user_contributor.values("project").distinct()
        "Récupération des projets si l'utilisateur est l'auteur ou le contributeur"
        queryset = Projects.objects.filter(
            Q(author_user=self.request.user) | Q(id__in=contributor_projet)).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author_user=self.request.user)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [FullAccess()]
        return [ContributorReadOnly()]


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorsSerializer

    def get_queryset(self):
        return Contributors.objects.filter(project_id=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project = get_object_or_404(Projects, pk=self.kwargs["project_pk"])
        serializer.save(project=project)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT']:
            return [FullAccess()]
        elif self.request.method in ['DELETE']:
            return [AuthorDeleteContributor()]
        return [ContributorProjectReadOnly()]


class IssuesViewset(ModelViewSet):

    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issues.objects.filter(project_id=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project = get_object_or_404(Projects, pk=self.kwargs["project_pk"])
        serializer.save(author_user=self.request.user, project=project)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [FullAccess()]
        return [ContributorProjectReadOnly()]


class CommentsViewset(ModelViewSet):

    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.filter(issue=self.kwargs["issue_pk"])

    def perform_create(self, serializer):
        issue = get_object_or_404(Issues, pk=self.kwargs["issue_pk"])
        return serializer.save(author_user=self.request.user, issue=issue)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [FullAccess()]
        return [ContributorProjectReadOnly()]
