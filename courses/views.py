from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Course, Enrollment, Content
from django.http import HttpResponseForbidden

# Create your views here.


# Check if the user is an instructor
def is_instructor(user):
    return user.role == 'instructor'

# Check if the user is an approver
def is_approver(user):
    return user.role == 'approver'

# Instructor: Create or update course
# @login_required
@user_passes_test(is_instructor)
def manage_course(request, course_id=None):
    course = None
    if course_id:
        course = Course.objects.get(id=course_id, instructor=request.user)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        if course:
            course.title = title
            course.description = description
            course.save()
        else:
            Course.objects.create(
                instructor=request.user,
                title=title,
                description=description
            )
        return redirect('course_list')
    
    return render(request, 'manage_course.html', {'course': course})

# Approver: Approve courses
# @login_required
@user_passes_test(is_approver)
def approve_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.approve()
    return redirect('course_list')

# Student: Enroll in a course
# @login_required
def enroll_in_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if course.status == 'Approved':
        Enrollment.objects.create(student=request.user, course=course)
        return redirect('course_list')
    else:
        return HttpResponseForbidden("This course is not approved yet.")

# View enrolled courses for a student
# @login_required
def view_enrolled_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'enrolled_courses.html', {'enrollments': enrollments})

# Upload content to a course (instructor only)
# @login_required
@user_passes_test(is_instructor)
def upload_content(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        file = request.FILES['file']
        content_type = request.POST['content_type']
        title = request.POST['title']
        Content.objects.create(
            course=course,
            content_type=content_type,
            file=file,
            title=title
        )
        return redirect('course_detail', course_id=course.id)

    return render(request, 'upload_content.html', {'course': course})

# @login_required
def course_list(request):
    # Only show courses with status 'Approved'
    courses = Course.objects.filter(status='Approved') 
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, course_id):
    # Get the course by ID or return a 404 if not found
    course = get_object_or_404(Course, id=course_id)

    return render(request, 'course_detail.html', {'course': course})
