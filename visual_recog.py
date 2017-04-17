from watson_developer_cloud import VisualRecognitionV3 as vr
import pprint

instance = vr(api_key='', version='2016-05-20')
img = instance.classify(images_url='')

data = img['images'][0]['classifiers'][0]['classes']
pprint.pprint(data)
