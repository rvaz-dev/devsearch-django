from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from projects.models import Project, Review, Tag
from .serializers import ProjectSerializer

# ------------------------------------------------------
# VIEWS
# ------------------------------------------------------
# IsAdmin, restricts routes just for admins
#
#
#
#
#
#
# ------------------------------------------------------
# <-- API ROUTES -->
# ------------------------------------------------------

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/projects'},                # (GET)   --> Returns all projects
        {'GET':'/api/projects/id'},             # (GET)   --> Returns a single project
        {'POST':'/api/projects/id/vote'},       # (POST)  --> Votes on a single project

        {'POST':'/api/users/token'},            # (GET)   --> Logs a user in
        {'POST':'/api/users/token/refresh'},    # (GET)   --> Refreshes a JSON token
    ]

    return Response(routes)

# ------------------------------------------------------
# <-- (GET) == GET PROJECTS -->
# ------------------------------------------------------

@api_view(['GET'])
def getProjects(request):
    print('USER:', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)

# ------------------------------------------------------
# <-- (GET) == GET PROJECT -->
# ------------------------------------------------------

@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data)

# ------------------------------------------------------
# <-- (POST) == VOTE ON PROJECT -->
# ------------------------------------------------------

@api_view(['POST']) # you could add put to update a vote
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    print('DATA:', data)

    # finds a review and updates it / or creates it
    review, created = Review.objects.get_or_create(
       owner = user,
       project = project,
    )
    # saves value to the database
    review.value = data['value']
    review.save()
    # updates vote count
    project.getVoteCount

    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data)

# ------------------------------------------------------
# <-- (DELETE) == REMOVE TAG -->
# ------------------------------------------------------

@api_view(['DELETE']) # you could add put to update a vote
def  removeTag(request):
    tagId = request.data['tag']
    projectId = request.data['project']

    project = Project.objects.get(id=projectId)
    tag = Tag.objects.get(id=tagId)

    project.tags.remove(tag)

    return Response('Tag was deleted!')
