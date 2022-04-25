from django.views.generic import ListView
from DashBoard.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'Admin/students/list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        return Student.objects.all()