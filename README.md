# WatsonVisualRecognition


This is just an introduction on how to use IBM  Watson's Visual Recognition Feature.

Watson is an IBM supercomputer that combines artificial intelligence (AI) and sophisticated analytical software for optimal performance as a “question answering” machine. It is a part of IBM Bluemix. 

IBM Bluemix is a cloud platform as a service (PaaS) developed by IBM. It supports several programming languages and services as well as integrated DevOps to build, run, deploy and manage applications on the cloud. 

## Create a Bluemix account
- Visit this [Link](https://www.ibm.com/cloud-computing/bluemix/) and signup for a 30 days free trial account.
- Click **Services**
- Click **Watson**
- Click **Create Watson**
- Click **Visual Recognition**
- You don't have to change anything there, just click **Create**
- Click on your visual recognition service
- Goto **Service Credentials**
- Click **View Credentials** and copy the *api_key*

## Local Setup
We are using Python3.

Install Watson Developer module
`pip3 install watson_developer_cloud`

## Execution
- Run the script using Python3
- You have 3 choices
  1. Visual Recognotion
  2. Text Recognition
  3. Facial Recognition

### Visual Recognition
Visual Recognition understands the contents of an image
![Alt text](Sample%20images/car.jpg?raw=true)

Output of analyzing above image will be
```
[{'class': 'subcompact car',
  'score': 0.948,
  'type_hierarchy': '/vehicle/subcompact car'},
 {'class': 'car', 'score': 0.974},
 {'class': 'vehicle', 'score': 0.974},
 {'class': 'compact car',
  'score': 0.53,
  'type_hierarchy': '/vehicle/compact car'},
 {'class': 'steel blue color', 'score': 0.894}]
```

### Text Recognition
Text Recognition tries to read the text in a given image
![Alt text](Sample%20images/hospital-sign-board.jpg?raw=true)

Output of analyzing above image will be
```
hospital
```

### Facial Recognition
Facial recognition tries to find human faces, approximate age, gender etc
![Alt text](Sample%20images/barack_obama.jpg?raw=true)

Output of analyzing above image will be
```
Name : Barack Obama
Gender : MALE
Age : 55-64
```
