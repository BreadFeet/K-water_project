import pandas as pd
import numpy as np
from config.settings import DATA_DIRS

water = pd.read_excel(DATA_DIRS[0] + '/preprocessed/water.xlsx', index_col=0)
#print(water)
hth = pd.read_excel(DATA_DIRS[0] + '/preprocessed/health.xlsx', index_col=0)
#print(hth)
map = pd.read_excel(DATA_DIRS[0] + '/preprocessed/loc.xlsx', index_col=0)
#print(map)


class waterAnal:
    def locWaterQual(loc):         # loc: 문자열
        ct_water = water[water['지역'].str.contains(loc)]   # 해당 loc의 2008~2019년 수질 데이터
        # 그래프 그릴 컬럼들
        cols =  ['불소(기준:1.5/ 단위:(mg/L))',
                '붕소(기준:1/ 단위:(mg/L))', '알루미늄(기준:0.2/ 단위:(mg/L))', '아연(기준:3/ 단위:(mg/L))',
                '톨루엔(기준:0.7/ 단위:(mg/L))', '총트리할로메탄(기준:0.1/ 단위:(mg/L))',
                '할로아세틱에시드(기준:0.1/ 단위:(mg/L))', '포름알데히드(기준:0.5/ 단위:(mg/L))', '클로로포름(기준:0.08/ 단위:(mg/L))']
        data = []
        for col in cols:
            dic = dict()
            dic['name'] = col
            dic['data'] = ct_water[col].to_list()
            data.append(dic)

        result = {
            'loc': loc,
            'data': data
        }
        #print(result)
        return result


class healthAnal:
    def locHealthQual(loc):
        ct_hth = hth[hth['지역'].str.contains(loc)]    # 해당 loc의 2009~2019 건강 데이터
        # 모든 컬럼을 그래프에 띄울 계획 - 지역, 연도 drop
        ct_hth.drop(['지역', '연도'], axis=1, inplace=True)
        #print(ct_hth.columns.values)

        data = []
        for col in ct_hth.columns.values:
            dic = dict()
            dic['name'] = col
            dic['data'] = ct_hth[col].to_list()
            data.append(dic)

        result = {
            'loc': loc,
            'data': data,
            'fx': 1
        }

        #print(result)
        return result


    def healthMap(year):    # year: int
        # 해당 year의 모든 시도 건강 데이터 추출
        yr_hth = hth[hth['연도'] == year]
        # yr_hth에서 지역은 index로 만들고, 연도는 drop
        yr_hth.set_index('지역', inplace=True)
        yr_hth.drop('연도', axis=1, inplace=True)


        # 지역(시도)마다 인포윈도우에 띄울 string을 담은 list 만들기----------------------------------------------
        contents = []

        for idx in yr_hth.index:
            sr = yr_hth.loc[idx]

            string = '<div style="padding:7px; width:150px; height:220px;"><b>' + idx + '</b><br>'  # Kakao Map에 바로 사용할 수 있는 형식: <div style="padding:5px;">Hello World!<br></div>'
            for s in zip(sr.index, sr.values):
                # print(type(s[0]), type(s[1]))      # str, numpy.float64
                string += s[0] + ': ' + str(s[1]) + '<br>'
            string += '<div>'
            contents.append(string)

        # 지역 & 인포윈도의 string으로 dataframe 만들기
        info = pd.DataFrame({'인포윈도우': contents}, index=yr_hth.index)


        # 17개 시도의 위도, 경도 데이터 추출-----------------------------------------------------------------------
        original = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시',
                    '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
        ct = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시',
              '수원시', '원주시', '청주시', '천안시', '전주시', '광주시', '안동시', '창원시', '제주시']
        map1 = map.set_index('지역')
        #map2 = map.loc[ct]   # ct에 해당하는 index를 뽑으면 17개가 맞는지 확인
        #print(len(map2))

        result = []
        for o, c in zip(original, ct):
            if (year in [2008, 2009, 2010, 2011, 2017, 2018, 2019]) & (o == '세종특별자치시'):
                continue
            dic = dict()
            dic['title'] = o
            dic['lat'] = map1.loc[c, '위도']
            dic['lng'] = map1.loc[c, '경도']
            dic['content'] = info.loc[o, '인포윈도우']
            result.append(dic)
        # 여기서는 데이터 전송을 위해서 json으로 만들고, chart2 페이지에서는 positions에 필요한 형태의 json으로 다시 만들어야 함

        #print(result)
        return result


if __name__ == '__main__':
    #waterAnal.locWaterQual('서울특별시')
    #healthAnal.locHealthQual('제주도')
    healthAnal.healthMap(2015)