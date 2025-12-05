from django.contrib.admin import AdminSite
from projects.models import Project
from contact.models import ContactMessage

class CustomAdminSite(AdminSite):
    site_header = "Ahsan Sheeraz Dashboard"

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['total_projects'] = Project.objects.count()
        extra_context['total_messages'] = ContactMessage.objects.count()
        extra_context['latest_projects'] = Project.objects.order_by('-created_at')[:5]
        extra_context['latest_messages'] = ContactMessage.objects.order_by('-created_at')[:5]
        return super().index(request, extra_context)
