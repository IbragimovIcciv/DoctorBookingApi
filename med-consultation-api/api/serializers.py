from rest_framework import serializers
from api.models import Doctor, User, News, Date
from root import settings


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "avatar"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.avatar:
            representation['avatar'] = settings.BASE_URL + instance.avatar.url
        else:
            representation['avatar'] = None
        return representation


class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "avatar"]


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'specialization', 'experience', 'location', 'clinic_name',
                  'consultation_fee', 'is_consultation_free', 'available_today',
                  'rating_percentage', 'patient_stories', ]


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Doctor
        fields = ['user', 'id', 'specialization', 'experience', 'location', 'clinic_name', 'consultation_fee',
                  'is_consultation_free', 'available_today', 'rating_percentage', 'patient_stories']


class NewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = News
        fields = ["user", "title", "img", "created_at"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.img:
            representation['img'] = settings.BASE_URL + instance.img.url
        else:
            representation['img'] = None
        return representation


class DateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Date
        fields = ['id', 'user', 'doctor', 'date', 'time', 'status']


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Date
        fields = ['id', 'user', 'doctor', 'date', 'time', 'status']
