from urllib.parse import quote

from services import get_data, graph_data

parameters = 'source_desc=SURVEY' +  \
                '&' + quote('sector_desc=FARMS & LANDS & ASSETS') + \
                '&' + quote('commodity_desc=FARM OPERATIONS') + \
                '&' + quote('statisticcat_desc=AREA OPERATED') + \
                '&unit_desc=ACRES' + \
                '&freq_desc=ANNUAL' + \
                '&reference_period_desc=YEAR' + \
                '&year__GE=1997' + \
                '&agg_level_desc=NATIONAL' + \
                '&' + quote('state_name=US TOTAL') + \
                '&format=CSV'

get_data(parameters, 'test')
graph_data("../out/test.csv")