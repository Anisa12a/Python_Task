from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class TaskSerializer(serializers.ModelSerializer):
    # I have used PrimaryKeyRelatedField for foreign key relationship
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Task
        fields = ['task_id', 'task_name', 'task_description', 'task_start_date', 'task_due_date', 'task_status', 'user_id']