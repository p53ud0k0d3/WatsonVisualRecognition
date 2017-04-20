from watson_developer_cloud import VisualRecognitionV3 as vr
import pprint

api_key = input("Enter you api key : ")
instance = vr(api_key=api_key, version='2016-05-20')

def visualRecog(self):

    images_url = input("Enter the url of the image :\n")
    img = self.classify(images_url=images_url)
    data = img['images'][0]['classifiers'][0]['classes']
    pprint.pprint(data)


def textRecog(self):

    images_url = input("Enter the url of the image :\n")
    img = self.recognize_text(images_url=images_url)
    print(img['images'][0]['text'])


def facialRecog(self):

    images_url = input("Enter the url of the image :\n")
    img = self.detect_faces(images_url=images_url)
    for identity in img['images'][0]['faces']:
        if('identity' in identity):
             print("Name : "+identity['identity']['name']+"\n",
                   "Gender : "+identity['gender']['gender']+"\n",
                   "Age : %s-%s\n***"%(identity['age']['min'],identity['age']['max'])
                  )
        else:
            print("Name : Unidentified\n",
                  "Gender : "+identity['gender']['gender']+"\n",
                  "Age : %s-%s\n***"%(identity['age']['min'],identity['age']['max'])
                 )


print("1.Visual Recognition\n2.Text Recognition\n3.Facial Recognition\n")
opt = input("Enter your choice : ")
if (opt == '1'):
    visualRecog(instance)
elif (opt == '2'):
    textRecog(instance)
elif (opt == '3'):
    facialRecog(instance)
else:
    print("Invalid Choice")

