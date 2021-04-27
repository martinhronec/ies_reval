import argparse
import typing
import requests
import json 

def get_real_estate_json(url):
    pass

def extract_area():
    pass

def extract_area_land(url):
    jsn = get_real_estate_json(url)
    real_estate_land_area = jsn['items'][9]['value']
    return real_estate_land_area

def extract_gps_coordinates():
    pass

def train_model():
    pass


class Appraisor:

    def __init__(self,url,area,area_land,gps_lat,gps_lon,model_path):
        pass

    def load_model():
        pass
    
    def get_data_from_ad(self):
        pass

    def prepare_data(self):
        pass

    def predict(self):
        pass


if __name__ == "__main__":
    # argument parsing from CLI
    app = Appraisor()
    app.predict()