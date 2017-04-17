# WatsonVisualRecognition


This is just an introduction on how to use IBM  Watson's Visual Recognition Feature.

Watson is an IBM supercomputer that combines artificial intelligence (AI) and sophisticated analytical software for optimal performance as a “question answering” machine. It is a part of IBM Bluemix. 

IBM Bluemix is a cloud platform as a service (PaaS) developed by IBM. It supports several programming languages and services as well as integrated DevOps to build, run, deploy and manage applications on the cloud. 

Visual Recognition understands the contents of images - visual concepts tag the image, find human faces, approximate age and gender, and find similar images in a collection. You can also train the service by creating your own custom concepts. Use Visual Recognition to detect a dress type in retail, identify spoiled fruit in inventory, and more. 

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
- Paste *api_key* into the file
- Paste url of the image you want to analyse
- Run the script using Python3
