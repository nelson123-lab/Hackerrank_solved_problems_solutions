from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/e20feb77-4d33-4b76-ada5-caf673298c9a"
iam_apikey_s2t = "wIkudROXZ3ZhuzHsxll84Qvx5ycmsWW5BOwJdkIK4avC"
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t
!wget -O PolynomialRegressionandPipelines.mp3  https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3
filename='PolynomialRegressionandPipelines.mp3'
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    response.result
from pandas.io.json import json_normalize
json_normalize(response.result['results'],"alternatives")
response
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)
