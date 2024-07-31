from rest_framework import serializers

from restapp2.models import Students


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('Student_Id','First_Name','Last_Name','Age','Course','Address','Location','Phone')