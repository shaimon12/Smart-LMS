# utils/routing.py

from app.student_panel import show_student_panel as student_panel
from app.teacher_panel import show_teacher_panel as teacher_panel
from app.admin_panel import show_admin_panel as admin_panel

def show_student_panel():
    student_panel()

def show_teacher_panel():
    teacher_panel()

def show_admin_panel():
    admin_panel()
