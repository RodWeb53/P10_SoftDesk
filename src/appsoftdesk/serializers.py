from .models import Projects, Contributors, Issues, Comments
from rest_framework.serializers import ModelSerializer, StringRelatedField, SerializerMethodField, SlugRelatedField
from django.contrib.auth import get_user_model


class ProjectsListSerializer(ModelSerializer):
    author_user = StringRelatedField()

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
    author_user = StringRelatedField()
    contributors = SerializerMethodField()
    issues = SerializerMethodField()

    class Meta:
        model = Projects
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author_user",
            "contributors",
            "issues",
        ]

    def get_contributors(self, instance):
        queryset = instance.contributors.all()
        serializer = ContributorsSerializer(queryset, many=True)
        return serializer.data

    def get_issues(self, instance):
        queryset = instance.issues.all()
        serializer = IssuesSerializer(queryset, many=True)
        return serializer.data


class ContributorsSerializer(ModelSerializer):

    project = StringRelatedField()
    author_user = SlugRelatedField(queryset=get_user_model().objects.all(),
                                   slug_field="email")

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

    author_user = StringRelatedField(read_only=True)
    project = StringRelatedField(read_only=True)
    comments = SerializerMethodField()

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
            "created_time",
            "comments",
        ]

    def get_comments(self, instance):
        queryset = instance.comments.all()
        serializer = CommentsSerializer(queryset, many=True)
        return serializer.data


class CommentsSerializer(ModelSerializer):

    author_user = StringRelatedField(read_only=True)
    issue = StringRelatedField(read_only=True)

    class Meta:
        model = Comments
        fields = [
            "id",
            "description",
            "author_user",
            "issue",
            "created_time",
        ]
