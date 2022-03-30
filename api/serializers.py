from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile



# ------------------------------------------------------
# Serializers
# ------------------------------------------------------
#
#
#
#
#
#
#
#
#
# ------------------------------------------------------
# <-- Review Serializer -->
# ------------------------------------------------------
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# ------------------------------------------------------
# <-- Profile Serializer -->
# ------------------------------------------------------
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

# ------------------------------------------------------
# <-- Tag Serializer -->
# ------------------------------------------------------
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# ------------------------------------------------------
# <-- Projects Serializer -->
# ------------------------------------------------------

class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)

    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    # it has to start with get_WhatEverYouAreGetting
    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data




