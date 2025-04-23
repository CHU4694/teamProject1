import csv
from django.core.management.base import BaseCommand
from storedata.models import MonthlyGame

class Command(BaseCommand):
    help = "CSV 파일로부터 이달의 게임 데이터 불러오기"
    
    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="CSV 파일 경로")

    def handle(self, *args, **options):
        csv_path = options["csv_path"]

        with open(csv_path, newline='', encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            # 기존 데이터 삭제 (선택사항)
            MonthlyGame.objects.all().delete()

            count = 0
            for row in reader:
                MonthlyGame.objects.create(
                    name=row["게임명"]
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {count}개의 이달의 게임이 성공적으로 업로드되었습니다.")) 