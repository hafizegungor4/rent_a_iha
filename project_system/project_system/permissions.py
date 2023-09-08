from rest_framework.permissions import BasePermission, SAFE_METHODS

from rentstate.models import RentState

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsGroupOwner(BasePermission):
    def has_permission(self, request, view):
        group_id = request.data.get('rentstate')
        if not group_id:
            return False
        try:
            group = RentState.objects.get(id=group_id)
        except RentState.DoesNotExist:
            return False
        return group.owner == request.user


class IsStudentOwnerOrStaff(BasePermission):
    def has_permission(self, request, view):
        group_id = request.data.get('rentstate')
        if not group_id:
            return False
        try:
            group = RentState.objects.get(id=group_id)
        except RentState.DoesNotExist:
            return False
        return group.owner == request.user


class IsProjectGroupOwner(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        project_id = request.data.get('group_project')
        if not project_id:
            return False