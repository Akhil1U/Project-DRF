# myapp/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date']

   
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True
    )
    status = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'published', 'is_available', 'author', 'author_id', 'status']

    def get_status(self, obj):
        return "Available" if obj.is_available else "Checked Out"

    def validate_published(self, value):
        if value > date.today():
            raise serializers.ValidationError("Publish date can't be in the future.")
        return value
