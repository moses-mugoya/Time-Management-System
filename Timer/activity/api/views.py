from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from activity.models import Activities
from .serializers import ActivitySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class ActivityCreateView(CreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ActivityDetailView(RetrieveAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ActivityListView(ListAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ActivityRetrieveApiView(RetrieveAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ActivityUpdateApiView(UpdateAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ActivityDestroyApiView(DestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
