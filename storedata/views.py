from django.shortcuts import render
from .models import StoreGameData , MonthlyGame
from django.db.models import Avg

# Create your views here.

def index(request):
    # 선택한 지역 (기본값: 전체)
    selected_region = request.GET.get('region', '전체')
    
    # 지역 목록 (중복 제거)
    regions = list(set(StoreGameData.objects.values_list('region', flat=True)))
    
    # 기본 쿼리셋
    queryset = StoreGameData.objects.all()
    
    # 특정 지역 선택 시 필터링
    if selected_region != '전체':
        queryset = queryset.filter(region=selected_region)
    
    # 지점 수 계산
    count_locations = queryset.count()
    
    # 고유 보드게임 수 계산 (owned_list에서 중복 제거)
    all_games = set()
    for store in queryset:
        owned_games = store.owned_list.split(';') if store.owned_list else []
        all_games.update(owned_games)
    unique_games = len(all_games)
    
    # 지점별 평균 보유 게임 수
    average_games = queryset.aggregate(avg=Avg('owned_count'))['avg']
    
    # 지점별 데이터 및 각 지점의 상세 정보
    stores_data = []
    for store in queryset:
        owned_list = store.owned_list.split(';') if store.owned_list else []
        missing_list = store.missing_list.split(';') if store.missing_list else []
        store_data = {
            'store': store.store,
            'region': store.region,
            'owned_count': store.owned_count,
            'missing_count': store.missing_count,
            'total': store.owned_count + store.missing_count,
            'owned_list': owned_list,
            'missing_list': missing_list

        }
        stores_data.append(store_data)
    
    # 선택된 지점 정보 (첫 번째 지점 또는 GET 파라미터로 선택한 지점)
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
            location_detail = None

    # 이달이 게임 목록록
    month_games = [game.name for game in MonthlyGame.objects.all()]
    
    context = {
        'selected_region': selected_region,
        'regions': regions,
        'count_locations': count_locations,
        'unique_games': unique_games,
        'average_games': average_games,
        'stores': stores_data,
        'location_detail': location_detail,
        'month_games' : month_games
    }
    
    return render(request, 'storedata/index.html', context)
