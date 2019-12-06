# Flye

He team i have tryied two approch 

1) Using deep learning 
  a) Text detection on recipet data using yolo pretrained model 
  b) Using CRNN model to convert text to image 
  
2) using opencv tesseract and Regular-Expressions


Approch 1 description 

first i tried for pilot project 

Steps 

1) To train a pre trained model for text detection in images using yolo and mobilenet model
2) then the model provided me detected text in image (and its Coordinate ) 
3) Now i have the Coordinate of the detected text using opencv i cropped that specific text and saved it in the directory 
4) Now i have the cropped images thats contains text 
5) I trained  a another model which covert image into text using CRNN and LSTM
6) and output of first model is passed to second model for converting iamge to text 
6) and you can see the ouput of the model in the ipython notebook

pilot project for text detection using yolo.ipynb          ----- for text detection in image  
pilot project for image to text coverter using crnn.ipynb  ----- for image to text coverting 

For pilot project i have used  coustom data ( data source ICDAR 2015 )

Now after getting accuracy of 97% on text detection and  92% accuracy on image to text model 


I tried for recipte data 

for this 

steps 

1) Manullay labled the data using labelImg-master software (code source github )

For labling images i have tried two apporch 
1) I labeled whole text in recipt data ( you can i find the demo file name X00016469671.txt )
2) I labeled only date text in recipt data  ( you can i find the demo file name X00016469670.txt )

Then repeated the whole step above 

but unforunately model was underfitting  the accurcy was very low on test data apporx 27 % ( Currenlty working on it )




second apporch 

using opencv i have applied some filter on the image to covert it i a formate that can be readed easily by tesseract
and then pass them to tessaract and applied regex for extracting date from the raw text and the output is saved into
execl file with two coloum ( image_name and image_date )

total date captured is 381 out of 590 iamges 
Accracy = 65%

Request:
POST /extract_date

Payload:
{“base_64_image_content”: <base_64_image_content>}

Response:
If date is present:
{“date”: “YYYY-MM-DD”}
If date is not present:
{“date”: "null"}





