from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter # type:ignore

router =DefaultRouter()
router.register(r'exams',ExamViewSet)
router.register(r'students', StudentViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'assessments', AssesmentViewSet)
router.register(r'AssessmentAnwser',AssementAnswerViewSet)

urlpatterns=[
 path('',home,name='home'),
 path('api/', include(router.urls)),

 path('faculty/', faculty, name='faculty'),
 path('student/', student, name='student'),
 path('fac_dashboard/',fac_dashboard, name='fac_dashboard'),
 path('logout/', logout, name='logout'),
 path('api/',include(router.urls)),
 path('fac_exam/',fac_exam,name='fac_exam'),
 path('fac_questions/', fac_questions, name='fac_questions'),
 path('std_dashboard', std_dashboard, name='std_dashboard'),
 path('exam/<int:eid>/',stud_exam, name='stud_exam'),
 path('res/<int:eid>/',stud_res, name='stud_res'),
]