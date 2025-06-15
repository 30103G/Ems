from rest_framework import serializers # type: ignore
from .models import *

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AssesmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assesment
        fields = '__all__'

class AssementAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssementAnswer
        fields = '__all__'