import csv
from django.core.management.base import BaseCommand
from storedata.models import StoreGameData

class Command(BaseCommand):
    help = "CSV 파일로부터 스토어 데이터 불러오기"
    
    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str)

    def handle(self, *args, **options):
        csv_path = options["csv_path"]

        with open(csv_path, newline='', encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            # 기존 데이터 삭제 (선택사항)
            StoreGameData.objects.all().delete()

            count = 0
            for row in reader:
                StoreGameData.objects.create(
                    region=row["지역"],
                    store=row["지점명"],
                    owned_count=int(row["보유 게임 수"]),
                    missing_count=int(row["미보유 게임 수"]),
                    owned_list=row["보유 게임 목록"],
                    missing_list=row["미보유 게임 목록"]
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {count}개의 데이터가 성공적으로 업로드되었습니다."))
