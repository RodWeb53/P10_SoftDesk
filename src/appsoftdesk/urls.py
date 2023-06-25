from django.urls import path, include
from rest_framework_nested import routers

from .views import ProjectsViewset, ContributorsViewset, IssuesViewset, CommentsViewset


router = routers.SimpleRouter()
router.register('projects', ProjectsViewset, basename="projects")

projects_router = routers.NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('users', ContributorsViewset, basename="project_users")
projects_router.register('issues', IssuesViewset, basename="project_issues")

issues_router = routers.NestedSimpleRouter(projects_router, "issues", lookup="issue")
issues_router.register('comments', CommentsViewset, basename="comments")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
]
