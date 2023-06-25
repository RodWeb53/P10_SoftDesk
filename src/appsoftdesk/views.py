from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from .models import Projects, Contributors, Issues, Comments
from .serializers import ProjectsListSerializer, ProjectsDetailSerializer, \
    ContributorsSerializer, IssuesSerializer, CommentsSerializer


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsListSerializer
    detail_serializer_class = ProjectsDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Projects.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)


class ContributorsViewset(ModelViewSet):

    serializer_class = ContributorsSerializer

    def get_queryset(self):
        return Contributors.objects.filter(project_id=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project = get_object_or_404(Projects, pk=self.kwargs["project_pk"])
        serializer.save(project=project)


class IssuesViewset(ModelViewSet):

    serializer_class = IssuesSerializer

    def get_queryset(self):
        return Issues.objects.filter(project_id=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        project = get_object_or_404(Projects, pk=self.kwargs["project_pk"])
        serializer.save(project=project)


class CommentsViewset(ModelViewSet):

    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.filter(issue=self.kwargs["issue_pk"])

    def perform_create(self, serializer):
        issue = get_object_or_404(Issues, pk=self.kwargs["issue_pk"])
        return serializer.save(issue=issue)
