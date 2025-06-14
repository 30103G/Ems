from django.shortcuts import render,redirect
from . models import *
# Create your views here.
def faculty(request):
 if request.session.get('unm'):
  return redirect('fac_dashboard')
 # else:
 #  print('user not in session')
 if request.method=='POST':
  unm=request.POST.get('unm')
  pwd=request.POST.get('pwd')
  fac=Faculty.objects.filter(unm=unm, pwd=pwd)
  if fac:
   print(fac)
   request.session['fid']=fac.first().id
   request.session['name']=fac.first().name
   request.session['unm']=unm
   request.session['type']='faculty'
   return redirect('fac_dashboard')
  else:
   print('Wrong Username')
 return render(request, 'login.html', {'login_type':'Faculty'})

def student(request):
 if request.session.get('unm'):
  return redirect('std_dashboard')
 # else:
 #  print('user not in session')
 if request.method=='POST':
  unm = request.POST.get('unm')
#   name=request.POST.get('name')
  pwd=request.POST.get('pwd')
  std=Student.objects.filter(unm=unm, pwd=pwd)
  if std:
   print(std)
   request.session['id']=std.first().id
   request.session['name']=std.first().name
   request.session['unm']=unm
   request.session['type']='prog'
   return redirect('std_dashboard')
  else:
   print('Wrong Username')
 return render(request, 'login.html', {'login_type':'Student'})


def home(request):
 return render(request,'index.html')

def fac_dashboard(request):
 if not request.session.get('unm'):
  return redirect('faculty')
 
 return render(request, 'faculty_dashboard.html')

def logout(request):
 if request.session.get('unm'):
  request.session.clear()
  return redirect('/')

from .models import *
from . serialisers import ExamSerializer,StudentSerializer,QuestionSerializer
from rest_framework import viewsets # type: ignore

class ExamViewSet(viewsets.ModelViewSet):
 queryset=Exam.objects.all()
 serializer_class = ExamSerializer


def fac_exam(request):
#  fac=request.session.get('user')
 fac_dict={'id': request.session.get('fid'),'name':request.session.get('name')}
 
 return render(request, 'fac_exam.html', {'fac':fac_dict})

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def fac_questions(request):
    exams = Exam.objects.all()
    return render(request, 'fac_questions.html', {'exams': exams})

def std_dashboard(request):
    cont = {'msg':'','exams':[], 'results':[]}
    unm=''
    pwd=''
    if request.method=='POST':
      unm = request.POST.get('unm')
      pwd = request.POST.get('pwd')
      sid=request.POST.get('sid')
      request.session['sid']=sid
    stud = Student.objects.filter(unm=unm,pwd=pwd)
    if stud:
      assessment= Assesment.objects.filter(student_id=sid, is_attempt=False)
      for i in assessment:
        exams= Exam.objects.filter(id=i.exam_id)
        if exams:
          cont['exams'].extend(exams)

      assessment= Assesment.objects.filter(student_id=sid, is_attempt=True)
      for i in assessment:
        exams= Exam.objects.filter(id=i.exam_id)
        if exams:
          cont['results'].extend(exams)
  
        else:
          cont['msg']='please Check all values'
    return render(request, 'students.html', cont)

def stud_exam(request, eid=1):
  cont={'eid':eid}
  if request.method=='POST':
    qans=request.POST.copy()
    qans.pop('csrfmiddlewaretoken')
    qans.pop('eid')
    exam = Exam.objects.filter(id=eid).first()
    for i,j in qans.items():
      aa=AssementAnswer()
      aa.answer=j
      aa.exam=exam
      aa.scored=0
      aa.save()
    assesment = Assesment.objects.filter(exam_id=eid,student_id=request.session.get('sid')).first()
    assesment.is_attempt=True
    assesment.save()
    return redirect('sd')
  ques = Question.objects.filter(exam_id=eid)
  cont['ques']=ques
  return render(request, 'stud_exam.html', cont)

def stud_res(req, eid=1):
  cont={'eid':eid, 'answered':[]}
  assesmet= Assesment.objects.filter(is_attempt=True,
                                      student_id=req.session.get('sid')).first()
  assestans=AssementAnswer.objects.filter(exam_id=assesmet.exam_id)
  ques=Question.objects.filter(exam_id=eid)
  answered=[]
  total = 0
  for a, q in zip(assestans,ques):
    total+=a.scored
    answered.append({'que':q.que, 'ans':a.answer, 'score':a.scored})

  cont['answered']=answered
  cont['total']=total
  return render(req, 'stud_res.html',cont)