from .models import Projects, Contributors, Issues, Comments
from rest_framework.serializers import ModelSerializer


class ProjectsListSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author_user",
        ]


class ProjectsDetailSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author_user",
        ]


class ContributorsSerializer(ModelSerializer):

    class Meta:
        model = Contributors
        fields = [
            "id",
            "author_user",
            "project",
            "permission",
            "role",
        ]


class IssuesSerializer(ModelSerializer):

    class Meta:
        model = Issues
        fields = [
            "id",
            "title",
            "desc",
            "tag",
            "priority",
            "project",
            "status",
            "author_user",
            "assignee_user",
        ]


class CommentsSerializer(ModelSerializer):

    class Meta:
        model = Comments
        fields = [
            "id",
            "description",
            "author_user",
            "issue",
        ]
