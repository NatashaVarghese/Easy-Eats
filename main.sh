#! /bin/sh
CURL_RESPONSE=`curl -X POST -u "apikey:52Z4tDujEEKo3-Vw45gifumAEHzI7CCFBfYBAA9e-C6E" --form "images_file=@$1" "https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19"`
echo $CURL_RESPONSE   
