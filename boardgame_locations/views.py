from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Count
from .models import Location, Store
import random

def location_list(request):

    example_locations = [
        {'name': '서울', 'note': '강남, 명동, 홍대...'},
        {'name': '경기', 'note': '수원, 분당, 일산...'},
        {'name': '인천', 'note': '송도, 부평, 계양구...'},
        {'name': '충청', 'note': '대전, 청주, 천안...'},
        {'name': '대전', 'note': '유성구, 서구, 중구...'},
        {'name': '대구', 'note': '동성로, 수성구, 달서구...'},
        {'name': '경상', 'note': '부산, 울산, 포항...'},
        {'name': '전라', 'note': '광주, 전주, 여수...'},
        {'name': '광주', 'note': '충장로, 금남로, 상무지구...'},
        {'name': '울산', 'note': '남구, 동구, 북구...'},
        {'name': '제주', 'note': '제주시, 서귀포시...'},
    ]

    return render(request, 'boardgame_locations/location_list.html', {
        'locations':example_locations
    })

def location_detail(request, location_name):
    location_stores = []
    
    store_counts = {
        '서울':8,
        '경기':6,
        '인천':4,
        '대전':3,
        '대구':4,
        '광주':3,
        '울산':3,
        '충청':5,
        '경상':6,
        '전라':4,
        '제주':2
    }

    num_stores = store_counts.get(location_name)

    all_games = [
        '스플렌더', '다빈치 코드', '뱅', '카탄', '티켓 투 라이드', 
        '할리갈리', '우노', '젠가', '루미큐브', '다이xit',
        '7 원더스', '코드네임', '카르카손', '블루밍 가든', '팬데믹',
        '마블 좀비', '어드벤처 랜드', '러브레터', '스몰월드', '메이히어',
        '글룸헤이븐', '테라포밍 마스', '스컬', '아줄', '카요'
    ]

    for i in range(26, 101):
        
        store_games_dict = {}
        all_games_in_region = set()

    for i in range(1, num_stores + 1):
        store_name = f"{location_name} 매장"

        base_owned = random.randint(10, 30)
        owned = int(base_owned)

        store_games = random.sample(all_games, min(base_owned, len(all_games)))

        store_games_dict[store_name] = store_games
        all_games_in_region.update(store_games)

        owned = len(store_games)

        location_stores.append({
            'name':store_name,
            'owned_games':owned,
            'not_owned_games':0,
            'games':store_games
        })
    
    region_unique_games_count = len(all_games_in_region)

    for store in location_stores:
        store['not_owned_games'] = region_unique_games_count - store['owned_games']

    total_stores = len(location_stores)
    total_owned_games = sum(store['owned_games'] for store in location_stores)

    location_info = {
        'name':location_name,
        'count_locations':total_stores,
        'unique_games':region_unique_games_count,
        'average_games_by_location':total_owned_games // total_stores if total_stores else 0
    }

    return render(request, 'boardgame_locations/location_detail.html', {
        'location':location_info,
        'stores':location_stores,
        'store_games':store_games_dict
    })