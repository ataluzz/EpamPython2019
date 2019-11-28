from collections import defaultdict

def open_file(path):
    f = open(path, "r")
    file = f.read()
    f.close()
    return file

def most_common(list):
    return max(set(list), key = list.count)

def replacements(str):
    str = str.replace("            ", "").replace("['","").replace("']", "").replace("'", "").replace(", ", "\n+ ")
    return str

def merge_files(file1, file2):
    whole_set = set()
    file1 = file1[3:-3].split('}, {')
    file2 = file2[3:-3].split('}, {')
    for wine in file1:
        whole_set.add(wine)
    for wine in file2:
        whole_set.add(wine)
    return whole_set

def parse_json(set):
    wine_list = []
    wine_dict = {}
    for wine in set:
        wine = wine.split(', "')
        for descript in wine:
            descript = descript.split(': ')
            if '"' in descript[0]:
                descript[0] = descript[0].replace('"','')
            if '"' in descript[1]:
                descript[1] = descript[1].replace('"','')
            if descript[1] == 'null':
                descript[1] = None
            wine_dict.update({descript[0]: descript[1]})
        wine_list.append(wine_dict)
        wine_dict = {}
    wine_list = sorted(sorted(wine_list, key = lambda wine: wine['title'], reverse = False),
                       key = lambda wine: int(wine['price']) if wine['price'] is not None else -1, reverse = True)
    return wine_list

def wine_list_dump(wine_list):
    with open("winedata_full.json", "w") as f:
        f.write('[')
        for wdict in wine_list:
            f.write('{')
            for key in wdict:
                if wdict[key] is not None:
                    f.writelines(f'"{key}": "{wdict[key]}", ')
                else:
                    f.writelines(f'"{key}": null, ')
            f.seek(f.tell() - 2)
            f.truncate()
            f.write('}, ')
        f.seek(f.tell() - 2)
        f.truncate()
        f.write(']')
        
def stats_for_sorts(wine_list, sorts):
    wine_prices = []
    wine_counter = 0
    wine_regions = []
    wine_countries = []
    wine_scores = []
    with open("stats.json", "w", encoding="utf-8") as f, \
        open("stats.md", "w", encoding="utf-8") as md:
        f.write('''{"statistics": {
                "wine": {
                     ''')
        md.write('''##Статистика для вин: \n''')
        for var in sorts:
            for wine in wine_list:
                if var == wine['variety']:
                    wine_counter += 1
                    wine_prices.append(wine['price'])
                    wine_scores.append(wine['points'])
                    if wine['region_1'] is not None:
                        wine_regions.append(wine['region_1'])
                    if wine['region_2'] is not None:
                        wine_regions.append(wine['region_2'])
                    wine_countries.append(wine['country'])
            if wine_counter == 0:
                continue
            wine_prices = [int(x) for x in wine_prices] 
            wine_scores = [int(x) for x in wine_scores] 
            average_price = round(sum(wine_prices) / wine_counter, 1)
            average_score = round(sum(wine_scores) / wine_counter, 1)
            min_price = min(wine_prices)
            max_price = max(wine_prices)
            most_common_region = most_common(wine_regions).encode().decode('unicode-escape')
            most_common_country = most_common(wine_countries).encode().decode('unicode-escape')
            f.write(f'''    "{var}":{{"average_price": {average_price}, 
                                    "min_price": {min_price},
                                    "max_price": {max_price}, 
                                    "most_common_region": {most_common_region},
                                    "most_common_country": {most_common_country}, 
                                    "average_score": {average_score}
                                    }},
                     ''')
            md.write(f'''###{var}:
            + average_price: {average_price}, 
            + min_price: {min_price},
            + max_price: {max_price},
            + most\_common_region: {most_common_region},
            + most\_common_country: {most_common_country}, 
            + average_score: {average_score}
            
            '''.replace("            ", ""))
            wine_prices = []
            wine_counter = 0
            wine_regions = []
            wine_countries = []
            wine_scores = []
            
def get_price_stats(wine_list):
    expensive_wines = []
    cheapest_wines = []
    exp_price = wine_list[0]['price']
    cheap_price = wine_list[-1]['price']
    for wine in wine_list:
        if wine['price'] == exp_price:
            expensive_wines.append(wine['title'])
        if wine['price'] == cheap_price:
            cheapest_wines.append(wine['title'])
    return exp_price, expensive_wines, cheap_price, cheapest_wines
        
def get_score_stats(wine_list):
    max_score = wine_list[0]['points']
    min_score = wine_list[0]['points']
    max_score_wine = []
    min_score_wine = []
    for wine in wine_list:
        if wine['points'] > max_score:
            max_score = wine['points']
        if wine['points'] < min_score:
            min_score = wine['points']
    for wine in wine_list:
        if wine['points'] == max_score:
            max_score_wine.append(wine['title'])
        if wine['points'] == min_score:
            min_score_wine.append(wine['title'])
    return max_score, max_score_wine, min_score, min_score_wine

def get_price_for_stats(wine_list):
    prices = defaultdict(list)
    for wine in wine_list:
        if wine['price'] is not None:
            prices[wine['country']].append(wine['price'])
    return prices

def get_expensive_stats_country(wine_list):
    exp = -float("inf")
    p_stats = get_price_for_stats(wine_list)
    expensive_country = defaultdict(list)
    for key, value in p_stats.items():
        val = sum(map(int, value)) / len(value)
        if val > exp:
            exp = val
            expensive_country = defaultdict(list)
            expensive_country[exp].append(key)
        elif val == exp:
            expensive_country[exp].append(key)
    return expensive_country
            
def get_cheap_stats_country(wine_list):
    cc = float("inf")
    p_stats = get_price_for_stats(wine_list)
    cheapest_country = defaultdict(list)
    for key, value in p_stats.items():
        val = sum(map(int, value)) / len(value)
        if val < cc:
            cc = val
            cheapest_country = defaultdict(list)
            cheapest_country[cc].append(key)
        elif val == cc:
            cheapest_country[cc].append(key)
    return cheapest_country

def get_points_for_stats(wine_list):
    points = defaultdict(list)
    for wine in wine_list:
        if wine['points'] is not None:
            points[wine['country']].append(wine['points'])
    return points

def get_most_rated_country(wine_list):
    mrate = -float("inf")
    rates = get_points_for_stats(wine_list)
    mr_country = defaultdict(list)
    for key, value in rates.items():
        val = sum(map(int, value)) / len(value)
        if val > mrate:
            mrate = val
            mr_country = defaultdict(list)
            mr_country[mrate].append(key)
        elif val == mrate:
            mr_country[mrate].append(key)
    return mr_country

def get_underrated_country(wine_list):
    urate = float("inf")
    rates = get_points_for_stats(wine_list)
    ur_country = defaultdict(list)
    for key, value in rates.items():
        val = sum(map(int, value)) / len(value)
        if val < urate:
            urate = val
            ur_country = defaultdict(list)
            ur_country[urate].append(key)
        elif val == urate:
            ur_country[urate].append(key)
        return ur_country
    
def get_active_comment(wine_list):
    tasters = []
    for wine in wine_list:
        if wine['taster_name'] is not None:
            tasters.append(wine['taster_name'])
    ac = most_common(tasters)
    num = tasters.count(ac)
    return num, ac

def stats_for_all(wine_list):
    with open("stats.json", "a", encoding="utf-8") as f, \
        open("stats.md", "a", encoding="utf-8") as md:
        f.write(f'''    "most_expensive_wine": {{"{get_price_stats(wine_list)[0]}": {get_price_stats(wine_list)[1]}}},
                         "cheapest_wine": {{"{get_price_stats(wine_list)[2]}": {get_price_stats(wine_list)[3]}}},
                         "highest_score": {{"{get_score_stats(wine_list)[0]}": {get_score_stats(wine_list)[1]}}},
                         "lowest_score": {{"{get_score_stats(wine_list)[2]}": {get_score_stats(wine_list)[3]}}},
                         "most_expensive_country": {{"{get_expensive_stats_country(wine_list).popitem()[0]}": {get_expensive_stats_country(wine_list).popitem()[1]}}},
                         "cheapest_country": {{"{get_cheap_stats_country(wine_list).popitem()[0]}": {get_cheap_stats_country(wine_list).popitem()[1]}}},
                         "most_rated_country": {{"{get_most_rated_country(wine_list).popitem()[0]}": {get_most_rated_country(wine_list).popitem()[1]}}},
                         "underrated_country": {{"{get_underrated_country(wine_list).popitem()[0]}": {get_underrated_country(wine_list).popitem()[1]}}},
                         "most_active_commentator": {{"{get_active_comment(wine_list)[0]}": {get_active_comment(wine_list)[1]}}}''')
        replaced = replacements((f'''##Общая статистика:
            ### most\_expensive_wine: {get_price_stats(wine_list)[0]}: 
            + {get_price_stats(wine_list)[1]}
            ### cheapest_wine: {get_price_stats(wine_list)[2]}: 
            + {get_price_stats(wine_list)[3]}
            ### highest_score: {get_score_stats(wine_list)[0]}: 
            + {get_score_stats(wine_list)[1]}
            ### lowest_score: {get_score_stats(wine_list)[2]}: 
            + {get_score_stats(wine_list)[3]}
            ### most\_expensive_country: {get_expensive_stats_country(wine_list).popitem()[0]}: 
            + {get_expensive_stats_country(wine_list).popitem()[1]}
            ### cheapest_country: {get_cheap_stats_country(wine_list).popitem()[0]}: 
            + {get_cheap_stats_country(wine_list).popitem()[1]}
            ### most\_rated_country: {get_most_rated_country(wine_list).popitem()[0]}: 
            + {get_most_rated_country(wine_list).popitem()[1]}
            ### underrated_country: {get_underrated_country(wine_list).popitem()[0]}: 
            + {get_underrated_country(wine_list).popitem()[1]}
            ### most\_active_commentator: {get_active_comment(wine_list)[0]}: 
            + {get_active_comment(wine_list)[1]}
            '''))
        md.writelines(replaced)
               
path_1 = "winedata_1.json"
path_2 = "winedata_2.json"
sorts = (
    'Gew\\u00fcrztraminer', 'Riesling', 'Merlot', 
    'Madera', 'Tempranillo', 'Red Blend'
    )

winedata_1 = open_file(path_1)
winedata_2 = open_file(path_2)
wd = merge_files(winedata_1, winedata_2)
wd1 = parse_json(wd)
whole_list = wine_list_dump(wd1)
stats_for_sorts(wd1, sorts)
stats_for_all(wd1)
