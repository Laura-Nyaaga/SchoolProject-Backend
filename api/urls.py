from django.urls import path

from .views import StudentListView, ClassPeriodListView, TeacherListView, CourseListView, ClassPeriodDetailView, StudentDetailView, Student_ClassListView, Student_ClassDetailView, TeacherDetailView, CourseDetailView

# from .views import ClassroomListView, ClassroomDetailView


urlpatterns = [
    path("students/", StudentListView.as_view(), name="student_list_view"),
    path("teachers/", TeacherListView.as_view(), name="teachers_list_view"),
    path("classperiods/", ClassPeriodListView.as_view(), name="ClassPeriod_list_view"),
    path('student_classes/', Student_ClassListView.as_view(), name = "student_class_list_view"),
    path("courses/", CourseListView.as_view(), name="course_list_view"),

    path('student_classes/<int:id>/', Student_ClassDetailView.as_view()),
    path('student/<int:id>/', StudentDetailView.as_view(), name='student_detail_view'),
    path('course/<int:id>/', CourseDetailView.as_view(), name='course_detail_view'),
    path('teacher/<int:id>/', TeacherDetailView.as_view(), name='teacher_detail_view'),
    path('classperiod/<int:id>/', ClassPeriodDetailView.as_view(), name='course_detail_view'),
     # path("classrooms/", ClassroomListView.as_view(), name="classroom_list_view"),
    # path('classroom/<int:id>/', ClassroomDetailView.as_view(), name='course_detail_view'),
]