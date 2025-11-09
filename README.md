# Image recognition powered by AWS Rekogntion and S3 buckets

This project uses Amazon Rekognition to automatically analyse images stored within an s3 bucket and return the descriptive labels. I built this with the use of serverless image processing and cloud based machine learning.

The python script connects using AWS SDK, requesting the image to Rekognition and prints out the label with confidence. It currently processes three images with a maximum amount of ten placed in at the moment but this can be extended to larger datasets.

## Potential use cases

This application can extend to things such as:  
* Smart photo gallery
This can process data in real time and using things such as a prompt can find all the pictures of a Cat for example given a threshold of confidence.

* Content moderation
Using content uploaded by users can identify the safety of content before displaying them on a website.

* Providing accessibility options for the visually impaired
This can be extended to provide speech and can describe to the user the visualisations seen in an automated way.

## Technologies utilised

* Python version 3
  * boto3 python library
* AWS CLI
* AWS SDK

## How to use the project?

Copying the github repository to a folder of your choice:  
```git
git clone https://github.com/gurvirdhillon/image-recognition-aws 
```

Change directory:
```terminal
cd image-recognition-aws
```

```pip
pip install -r requirements.txt
```


Sanity check:
```terminal
python3 bucket-check.py
```

```terminal
python3 recognition-aws.py
```


### AWS resources Utilised

* IAM for the management of access and authorisation
* S3 for the storage of pictures and the access of pictures
* Rekognition: A tool used to automate and recognise content for applications.

# Resources utilised:

<a href="https://youtu.be/PyjDVZ--cfs?si=HlL_DCb7T3EO4Zra">Inspired by Tiny Technical Tutorials</a>
