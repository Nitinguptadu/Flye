from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer
from PIL import Image
import pytesseract
import re
import dateutil.parser as dparser
import os
from .models import File

import base64
from io import BytesIO
import string 
import random 


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)


    def post(self, request, *args, **kwargs):

      res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7)) 
      image_data = request.data["base_64_image_content"]
      formatex, imgstr = image_data.split(';base64,')
      ext = formatex.split('/')[-1]

      with open("media/"+str(res)+"."+ext, "wb") as fh:
          fh.write(base64.b64decode(imgstr))

      result = detect_date(str(res)+"."+ext)

      if result == "none":
          return Response({"date": "null"})
      else:
          return Response({"date": result})



def detect_date(image_path):
    im = Image.open("/home/nitin/project/media/"+str(image_path))
    text = pytesseract.image_to_string(im, lang="eng")
    print("-----------------------")
    

    if not re.search("((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))", text) == None:
        a = re.search("((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))", text)
        a=a[0]
    elif not re.search("((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])", text) == None:
        a = re.search("((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])", text)
        a=a[0]
    elif not re.search("([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1])", text) == None:
        a = re.search("([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1])", text)
        a=a[0]
    elif not re.search("([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))", text) == None:
        a = re.search("([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))", text)
        a=a[0]
    elif not re.search("([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))", text) == None:
        a = re.search("([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-]([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))", text)
        a=a[0]
    elif not re.search("([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-|\s]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))", text) == None:
        a = re.search("([1-2](0|1|9)[0-9][0-9]|([0-9][0-9]))[.|/|-]([0][1-9]|[1-2][0-9]|[3][0-1]|[1-9])[.|/|-|\s]((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)|([0][1-9]|[1][0-2]|[1-9]))", text)
        a=a[0]
    else:
        text_lines = text.split("\n")
        for j in text_lines:
            try:
                a = dparser.parse(j, fuzzy=False)
                a = str(a)
                a = a[:-9]
                break
            except:
                a= "none"
    if not a =="none":
        a = dparser.parse(a, fuzzy=False)
        a = str(a)
        a = a[:-9]
    return a

