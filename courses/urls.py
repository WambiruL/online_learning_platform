from django.urls import path
from . import views

urlpatterns = [
    # Instructor views
    path('manage-course/', views.manage_course, name='manage_course'),  # For creating a new course
    path('manage-course/<int:course_id>/', views.manage_course, name='update_course'),  # For updating a course
    path('upload-content/<int:course_id>/', views.upload_content, name='upload_content'),  # For uploading content to a course
    
    # Approver views
    path('approve-course/<int:course_id>/', views.approve_course, name='approve_course'),  # For approving a course
    
    # Student views
    path('enroll-in-course/<int:course_id>/', views.enroll_in_course, name='enroll_in_course'),  # For enrolling in a course
    path('view-enrolled-courses/', views.view_enrolled_courses, name='view_enrolled_courses'),  # For viewing enrolled courses
    
    # Optionally, you can add a page to list courses
    path('course-list/', views.course_list, name='course_list'),  # Display all available courses
    path('course-detail/<int:course_id>/', views.course_detail, name='course_detail'),  # For viewing details of a single course
]
