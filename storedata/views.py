from django.shortcuts import render
from .models import StoreGameData, MonthlyGame
from django.db.models import Avg

# 한글 → 영어 지역 이름 매핑
REGION_MAP = {
    '서울': 'seoul',
    '대전': 'daejeon',
    '부산': 'busan',
    '광주': 'gwangju',
    '인천': 'incheon',
    '제주': 'jeju',
    '경기': 'gyeonggi',
    '전라': 'jeolla',
    '경상': 'gyeongsang',
    '충청': 'chungcheong',
    '울산': 'ulsan',
    '대구': 'daegu'

}

def index(request):
    selected_region = request.GET.get('region', '전체')

    region_order = ['서울', '경기', '인천', '충청', '대전', '대구', '경상', '전라', '광주', '울산', '부산', '제주']
    regions = list(set(StoreGameData.objects.values_list('region', flat=True)))
    regions = [region for region in region_order if region in regions]

    queryset = StoreGameData.objects.all()
    if selected_region != '전체':
        queryset = queryset.filter(region=selected_region)

    count_locations = queryset.count()

    all_games = []
    for store in queryset:
        if store.owned_list:
            games = [game.strip() for game in store.owned_list.split(',')]
            all_games.extend(games)

    unique_games = len(set(all_games))

    average_games = queryset.aggregate(avg=Avg('owned_count'))['avg']

    stores_data = []
    for store in queryset:
        owned_list = store.owned_list.split(';') if store.owned_list else []
        missing_list = store.missing_list.split(';') if store.missing_list else []
        stores_data.append({
            'store': store.store,
            'region': store.region,
            'owned_count': store.owned_count,
            'missing_count': store.missing_count,
            'total': store.owned_count + store.missing_count,
            'owned_list': owned_list,
            'missing_list': missing_list
        })

    selected_store = request.GET.get('store', None)
    location_detail = None
    if selected_store:
        try:
            store_obj = queryset.get(store=selected_store)
            location_detail = {
                'store': store_obj.store,
                'region': store_obj.region,
                'owned_count': store_obj.owned_count,
                'missing_count': store_obj.missing_count,
                'total_games': store_obj.owned_count + store_obj.missing_count
            }
        except StoreGameData.DoesNotExist:
            pass

    month_games = [game.name for game in MonthlyGame.objects.all()]

    english_region = REGION_MAP.get(selected_region, 'default')  

    context = {
        'selected_region': selected_region,
        'regions': regions,
        'count_locations': count_locations,
        'unique_games': unique_games,
        'average_games': average_games,
        'stores': stores_data,
        'location_detail': location_detail,

        'owned_list': owned_list,
        'missing_list': missing_list,
        'month_games': month_games,
        'english_region': english_region

    }

    return render(request, 'storedata/index.html', context)