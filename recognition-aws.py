import boto3

def detect_labels(photo, bucket):
    client = boto3.client('rekognition', region_name='eu-west-2')

    print(f"Requesting recognition")
    print(f"Bucket: {bucket}")
    print(f"Photo: {photo}\n")

    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10
    )

    print(f"Detected labels for {photo}:\n")
    for label in response['Labels']:
        print(f"Label: {label['Name']} (Confidence: {label['Confidence']:.2f}%)")

    return len(response['Labels'])

def main():
    bucket = "test-bucket-09-11-1601"
    images = ["car.jpg", "milk.jpg", "dog.jpg"]

    for img in images:
        detect_labels(img, bucket)

if __name__ == "__main__":
    main()
