from django.contrib.auth.models import User, Group
from rest_framework import serializers
from polls.models import Choice, Question


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Question
            fields = ['url','id',"question_text",]
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Choice
            fields = ['url','id','question',"choice_text",'votes']
