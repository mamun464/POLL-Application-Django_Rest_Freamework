from rest_framework import serializers
from .models import Author
from .models import Choice

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author_name', 'author_question']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'Choice_Answer','vote']

class CombinedSerializer(serializers.Serializer):
    author = AuthorSerializer()
    choice = ChoiceSerializer()

    class Meta:
        fields = ["author", "choice",]