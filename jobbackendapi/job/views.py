#pylint:disable=all
from rest_framework import viewsets
from .models import User, Company, Job
from .serializers import UserSerializer, CompanySerializer, JobSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        user = request.user
        # Check if user is authenticated first (should be, due to permission)
        if not user.user_type == "job_poster":
            return Response(
                {"detail": "You do not have permission to view this resource."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().list(request, *args, **kwargs)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        if not user.user_type == "job_poster":
            return Response(
                {"detail": "You do not have permission to create a company."},
                status=status.HTTP_403_FORBIDDEN,
            )
        # Make a mutable copy of request.data to add created_by
        data = request.data.copy()
        data["created_by"] = user.pk

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        user = request.user

        if not (user.user_type == "job_poster"):
            return Response(
                {"detail": "You do not have permission to create a job."},
                status=status.HTTP_403_FORBIDDEN,
            )

        data = request.data.copy()
        data["created_by"] = user.pk

        company_id = data.get("company")
        if not company_id:
            return Response(
                {"detail": "Company field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
