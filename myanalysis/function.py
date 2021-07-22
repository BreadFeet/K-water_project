# Jupyter Notebook 수질 데이터 전처리에 사용하는 함수를 모듈로 만듦
import pandas as pd
import numpy as np

class fx:
    def waterQualByCity(water, year):
        '''
        water: 전처리와 결측치 처리가 끝난 dataframe. Column index=3에서 '일반세균' 항목으로 시작해야 함
        year: 해당 연도
        각 지역별 1년 평균 물질 농도를 계산하여 dataframe을 반환
        '''

        lst = []  # Dataframe 만들기 위해서 준비
        cities = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도',
                  '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
        concs = water.columns[3:]

        for city in cities:
            ct_conc = [year, city]  # 하나의 도시에 대해, 이름과 모든 물질의 농도를 모은 리스트
            for conc in concs:
                df = water[water['지역'].str.contains(city)]
                ct_water = df.copy()

                if conc == '일반세균(기준:100/ 단위:(CFU/mL))':
                    ct_water['월별물질농도(CFU/일)'] = ct_water['시설용량(㎥/일)'] * ct_water[conc] * (10 ** 6)
                    if ct_water['시설용량(㎥/일)'].sum() == 0:
                        t_conc = 0    # 세종시가 없던 연도에는 0으로 채워진다
                    else:
                        t_conc = (ct_water['월별물질농도(CFU/일)'].sum() / ct_water['시설용량(㎥/일)'].sum()) * (
                                    10 ** -6)  # 2018년, xx지역, 일반세균 평균 농도(CFU/mL)

                elif conc == '수소이온농도(기준:5.8 ~ 8.5/ 단위:-)':
                    ct_water[conc] = ct_water[conc].apply(lambda x: 1 / 10 ** x)  # pH를 [H+](단위:mol/L)로 바꾸는 과정
                    ct_water['월별물질농도(mol/일)'] = ct_water['시설용량(㎥/일)'] * ct_water[conc] * 1000
                    if ct_water['시설용량(㎥/일)'].sum() == 0:
                        t_conc = 0
                    else:
                        t_conc = (ct_water['월별물질농도(mol/일)'].sum() / ct_water[
                            '시설용량(㎥/일)'].sum()) * 0.001  # 2018년, xx지역, 수소이온 평균 농도(mol/L)
                        t_conc = -np.log10(t_conc)  # 원래대로 pH로 변환

                else:  # '색도' 포함
                    ct_water['월별물질농도(mg/일)'] = ct_water['시설용량(㎥/일)'] * ct_water[conc] * 1000
                    if ct_water['시설용량(㎥/일)'].sum() == 0:
                        t_conc = 0
                    else:
                        t_conc = (ct_water['월별물질농도(mg/일)'].sum() / ct_water[
                            '시설용량(㎥/일)'].sum()) * 0.001  # 2018년, xx지역, xx 물질 평균 농도(mg/L)

                ct_conc.append(t_conc)
            lst.append(ct_conc)

        result = pd.DataFrame(lst, columns=['연도', '지역'] + list(concs))
        return result


if __name__ == '__main__':
    fx.waterQualByCity(water)