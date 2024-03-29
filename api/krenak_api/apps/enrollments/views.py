from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from krenak_api.apps.enrollments.models import Enrollment, Interest

from .serializers import EnrollmentCreationSerializer, EnrollmentSerializer, InterestSerializer

class EnrollmentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of enrollments or create new
    """

    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentCreationSerializer
    queryset = Enrollment.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = Enrollment.objects.filter(enrollee=self.request.user)
        return queryset

    def get_serializer_class(self):
        if hasattr(self, 'request') and hasattr(self.request, 'method') and self.request.method == "POST":
            return EnrollmentCreationSerializer
        return EnrollmentSerializer


class EnrollmentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete enrollments
    """

    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        queryset = Enrollment.objects.filter(enrollee=self.request.user)
        return queryset


class InterestListAPIView(ListAPIView):
    """
    API view to retrieve list of enrollments
    """

    serializer_class = InterestSerializer
    queryset = Interest.objects.all()


class InterestDetailsAPIView(RetrieveAPIView):
    """
    API view to retrieve interests
    """

    permission_classes = [IsAuthenticated]
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()
    lookup_field = "id"
