import pandas as pd
import numpy as np
from config.settings import DATA_DIRS

water = pd.read_excel(DATA_DIRS[0] + '/preprocessed/water.xlsx', index_col=0)
#print(water)

class waterAnal:
    def locWaterQual(loc):         # loc: 문자열
        ct_water = water[water['지역'].str.contains(loc)]   # 해당 loc의 2008~2019년 데이터
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
        print(result)
        return result


class healthAnal:
    def locHealthQual(loc):
        pass



if __name__ == '__main__':
    #waterAnal.locWaterQual('서울특별시')
    healthAnal.locHealthQual('전라북도')