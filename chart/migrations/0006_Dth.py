import csv
import os
from django.db import migrations
from django.conf import settings

# csv 파일의 해당 열 번호를 상수로 정의
Date= 0  # 날짜
France = 1
Germany = 2
Korea_South = 3
US = 4
United_Kingdom = 5

def add_deaths(apps, schema_editor):
    Deaths = apps.get_model('chart', 'Deaths')  # (app_label, model_name)
    csv_file = os.path.join(settings.BASE_DIR, 'dth_19.csv')
    with open(csv_file) as dataset:                   # 파일 객체 dataset
        reader = csv.reader(dataset)                    # 파일 객체 dataset에 대한 판독기 획득
        next(reader)  # ignore first row (headers)      # __next__() 호출 때마다 한 라인 판독
        for entry in reader:                            # 판독기에 대하여 반복 처리
            Deaths.objects.create(                       # DB 행 생성
                Date=entry[Date],
                France=entry[France],
                Germany=entry[Germany],
                Korea_South=entry[Korea_South],
                US=entry[US],
                United_Kingdom=entry[United_Kingdom],
            )

class Migration(migrations.Migration):
    dependencies = [                            # 선행 관계
        ('chart', '0005_deaths'),         # app_label, preceding migration file
    ]
    operations = [                              # 작업
        migrations.RunPython(add_deaths),   # add_deaths 함수를 호출
    ]