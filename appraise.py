import argparse
import typing
import re
import requests
import json
import catboost
import argparse


def get_real_estate_json(url):
    split_one = url.split('/')
    part_with_id = split_one[-1]
    split_two = part_with_id.split('#')
    house_id = split_two[0]

    api_url = 'https://www.sreality.cz/api/cs/v2/estates/'
    jsn = requests.get(api_url+house_id)
    return json.loads(jsn.text)

def extract_area():
    pass

def extract_area_land():
    pass

def extract_gps_coordinates():
    pass



class Appraisor:

    def __init__(self,url,model_path):
        self.model_path = model_path
        self.model = self.load_model(model_path)
        self.url = url
        re_dict = self.get_data_from_ad(url)
        self.re_attributes = self.prepare_data(re_dict)

    def load_model(self,model_path):
        from_file = catboost.CatBoostRegressor()
        model = from_file.load_model(model_path)
        return model
    
    def get_data_from_ad(self,url):
        re_d = get_real_estate_json(url)
        return re_d

    def prepare_data(self,re_d):
        area = extract_area(re_d)
        area_land = extract_area_land(re_d)
        gps_lat, gps_lon = extract_gps_coordinates(re_d) 
        re_attributes = pd.Series({'area':area,'area_land':area_land, 'gps_lat':gps_lat, 'gps_lon': gps_lon})
        return re_attributes

    def predict(self,):
        return self.model.predict(self.attributes)


if __name__ == "__main__":
    # argument parsing from CLI
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--url', 
                        help='an integer for the accumulator')
    parser.add_argument('--model_path')
    args = parser.parse_args()
    url = args.url
    model_path = args.model_path

    app = Appraisor(url, model_path)
    app.predict()
