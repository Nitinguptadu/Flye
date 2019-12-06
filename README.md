Flye
He team i have tried two approaches
1)Using deep learning 
a) Text detection on recipet data using yolo pretrained model
b) Using CRNN model to convert text to image


2)using opencv tesseract and Regular-Expressions


Approach 1 description

first i tried for pilot project

Steps

1)To train a pre trained model for text detection in images using yolo and mobilenet model
2)then the model provided me detected text in image (and its Coordinate )
3)Now i have the Coordinate of the detected text using opencv i cropped that specific text and saved it in the directory
4)Now i have the cropped images thats contains text
5)I trained a another model which convert image into text using CRNN and LSTM
6)and output of first model is passed to the second model for converting image to text
7)and you can see the output of the model in the ipython notebook


pilot project for text detection using yolo.ipynb ----- for text detection in image

pilot project for image to text converter using crnn.ipynb ----- for image to text converting


For pilot project i have used custom data ( data source ICDAR 2015 )


Now after getting accuracy of 97% on text detection and 92% accuracy on image to text model


I tried for receipt data

for this

steps

Manually labeled the data using labelIng-master software (code source github )

For labeling images i have tried two approaches

I labeled the whole text in receipt data ( you can i find the demo filename X00016469671.txt )

I labeled only date text in receipt data ( you can i find the demo filename X00016469670.txt )

Then repeated the whole step above

but unfortunately model was underfitting the accuracy was very low on test data approx 27 % ( Currently working on it )




second approach
using opencv I have applied some filter on the image to convert it i a format that can be reached easily by tesseract and then pass them to tesseract and applied regex for extracting date data from the raw text and the output is saved into excel file with two column ( image_name and image_date )
total date captured is 381 out of 590 images '

Accuracy = 65%


Request:
POST /extract_date

Payload:
{“base_64_image_content”: <base_64_image_content>}

Response:
If date is present:
{“date”: “YYYY-MM-DD”}
If date is not present:
{“date”: null}


