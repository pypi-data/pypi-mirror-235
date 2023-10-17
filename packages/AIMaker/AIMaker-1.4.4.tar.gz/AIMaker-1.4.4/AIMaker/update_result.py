import os
import requests
import json
import logging
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

KEY_RESULT_VALUE = "result"
KEY_SCORE_VALUE = "scores"
KEY_POD_NAME = "podName"                                                               
                                                                                                              
def retry_session(session=None):                                                                              
    session = session or requests.Session()                                                                   
    retry = Retry(                                                                                            
        total=5,                                                                                              
        read=5,                                                                                               
        status_forcelist=[408, 429, 500, 502, 503, 504, 524, 598],                                                           
        connect=5,                                                                                            
        backoff_factor=2,                                                                                     
        method_whitelist=False,                                                                               
    )                                                                                                         
    adapter = HTTPAdapter(max_retries=retry)                                                                  
    session.mount('http://', adapter)                                                                         
    session.mount('https://', adapter)                                                                        
    return session

def sendUpdateRequest(result):

    if isinstance(result, (int, float)) is False:
        logging.error(
            "[TypeError] Data type ({}) of result is not allowed".format(str(type(result))))
        return "Update result failed, please check data type of result."

    try:
        ASUS_CLOUDINFRA_VERIFY_ENABLE = 'True'
        if "ASUS_CLOUDINFRA_VERIFY_ENABLE" in os.environ:
            ASUS_CLOUDINFRA_VERIFY_ENABLE = os.getenv('ASUS_CLOUDINFRA_VERIFY_ENABLE')

        if ASUS_CLOUDINFRA_VERIFY_ENABLE == 'True' or ASUS_CLOUDINFRA_VERIFY_ENABLE == 'true':
            ASUS_CLOUDINFRA_VERIFY_ENABLE = True
        if ASUS_CLOUDINFRA_VERIFY_ENABLE == 'False' or ASUS_CLOUDINFRA_VERIFY_ENABLE == 'false':
            ASUS_CLOUDINFRA_VERIFY_ENABLE = False

        if "ASUS_CLOUDINFRA_JOB_ID" in os.environ:
            jobId = os.getenv('ASUS_CLOUDINFRA_JOB_ID')
        if "ASUS_CLOUDINFRA_RUN_ID" in os.environ:
            trialId = os.getenv('ASUS_CLOUDINFRA_RUN_ID')
        if "ASUS_CLOUDINFRA_TOKEN" in os.environ:
            token = os.getenv('ASUS_CLOUDINFRA_TOKEN')
        if "ASUS_CLOUDINFRA_API_HOST" in os.environ:
            url = os.getenv('ASUS_CLOUDINFRA_API_HOST')

        # This environment value was deprecated
        if "ASUS_JOB_ID" in os.environ:
            jobId = os.getenv('ASUS_JOB_ID')
        if "ASUS_JOB_RUN_ID" in os.environ:
            trialId = os.getenv('ASUS_JOB_RUN_ID')
        if "AI_MAKER_TOKEN" in os.environ:
            token = os.getenv('AI_MAKER_TOKEN')
        if "AI_MAKER_HOST" in os.environ:
            url = os.getenv('AI_MAKER_HOST')

        # For hybrid cloud
        if "ASUS_CLOUDINFRA_TRIAL_ID" in os.environ:
            trialId = os.getenv('ASUS_CLOUDINFRA_TRIAL_ID')
        if "ASUS_CLOUDINFRA_SERVICE_TYPE" in os.environ:
            serviceType = os.getenv('ASUS_CLOUDINFRA_SERVICE_TYPE')

    except KeyError as e:
        logging.error("[KeyError] Please assign {} value".format(str(e)))
        return "Update result failed, please contact your system administrator"

    # If ASUS_CLOUDINFRA_AUTH_KEY exist, call v3 api
    if "ASUS_CLOUDINFRA_AUTH_KEY" in os.environ:
        HEADERS = {"content-type": "application/json"}
        auth = os.getenv('ASUS_CLOUDINFRA_AUTH_KEY')
        # Remote job
        if serviceType == "SMTR":
            url = url+"/api/v3/ai-maker/callback/results/remote-jobs/"+jobId+"/trials/"+trialId+"/?auth="+auth
        # Local job
        else:
            url = url+"/api/v3/ai-maker/callback/results/jobs/"+jobId+"/trials/"+trialId+"/?auth="+auth
    else:
        HEADERS = {"content-type": "application/json", "Authorization": "bearer "+token}
        # Remote job
        if serviceType == "SMTR":
            url = url+"/api/v1/ai-maker/callback/results/remote-jobs/"+jobId+"/trials/"+trialId
        # Local job
        else:
            url = url+"/api/v1/ai-maker/callback/results/jobs/"+jobId+"/trials/"+trialId

    body = json.dumps({KEY_RESULT_VALUE: float(result)})

    logging.debug("Headers: {}".format(HEADERS))
    logging.debug("Body: {}".format(body))
    logging.debug("Url: {}".format(url))

    try:                                                                                                      
        requests = retry_session()                                                                            
        r = requests.post(url, data=body, headers=HEADERS, verify=ASUS_CLOUDINFRA_VERIFY_ENABLE)                              
        logging.debug("Reponse: {}".format(r.text))                                                           
        r.raise_for_status()                                                                                  
        return "Update result OK"                                                                             
    except Exception as e:                                                                                    
        print(e)                                                                                              
        return "Update result failed, please contact your system administrator"


def sendScoresRequest(scores):

    # check data type is dict
    if isinstance(scores, dict) is False:
        logging.error(
            "[TypeError] Data type ({}) of scores is not allowed".format(str(type(scores))))
        return "Update scores failed, please check data type of scores."

    try:
        ASUS_CLOUDINFRA_VERIFY_ENABLE = 'True'
        if "ASUS_CLOUDINFRA_VERIFY_ENABLE" in os.environ:
            ASUS_CLOUDINFRA_VERIFY_ENABLE = os.getenv('ASUS_CLOUDINFRA_VERIFY_ENABLE')

        if ASUS_CLOUDINFRA_VERIFY_ENABLE == 'True' or ASUS_CLOUDINFRA_VERIFY_ENABLE == 'true':
            ASUS_CLOUDINFRA_VERIFY_ENABLE = True
        if ASUS_CLOUDINFRA_VERIFY_ENABLE == 'False' or ASUS_CLOUDINFRA_VERIFY_ENABLE == 'false':
            ASUS_CLOUDINFRA_VERIFY_ENABLE = False

        if "ASUS_CLOUDINFRA_JOB_ID" in os.environ:
            jobId = os.getenv('ASUS_CLOUDINFRA_JOB_ID')
        if "ASUS_CLOUDINFRA_RUN_ID" in os.environ:
            trialId = os.getenv('ASUS_CLOUDINFRA_RUN_ID')
        if "ASUS_CLOUDINFRA_TOKEN" in os.environ:
            token = os.getenv('ASUS_CLOUDINFRA_TOKEN')
        if "ASUS_CLOUDINFRA_API_HOST" in os.environ:
            url = os.getenv('ASUS_CLOUDINFRA_API_HOST')

        # This environment value was deprecated
        if "ASUS_JOB_ID" in os.environ:
            jobId = os.getenv('ASUS_JOB_ID')
        if "ASUS_JOB_RUN_ID" in os.environ:
            trialId = os.getenv('ASUS_JOB_RUN_ID')
        if "AI_MAKER_TOKEN" in os.environ:
            token = os.getenv('AI_MAKER_TOKEN')
        if "AI_MAKER_HOST" in os.environ:
            url = os.getenv('AI_MAKER_HOST')

        # For hybrid cloud
        if "ASUS_CLOUDINFRA_TRIAL_ID" in os.environ:
            trialId = os.getenv('ASUS_CLOUDINFRA_TRIAL_ID')
        if "ASUS_CLOUDINFRA_SERVICE_TYPE" in os.environ:
            serviceType = os.getenv('ASUS_CLOUDINFRA_SERVICE_TYPE')

    except KeyError as e:
        logging.error("[KeyError] Please assign {} value".format(str(e)))
        return "Update scores failed, please contact your system administrator"

    # If ASUS_CLOUDINFRA_AUTH_KEY exist, call v3 api
    if "ASUS_CLOUDINFRA_AUTH_KEY" in os.environ:
        HEADERS = {"content-type": "application/json"}
        auth = os.getenv('ASUS_CLOUDINFRA_AUTH_KEY')
        # Remote job
        if serviceType == "SMTR":
            url = url+"/api/v3/ai-maker/callback/scores/remote-jobs/"+jobId+"/trials/"+trialId+"/?auth="+auth
        # Local job
        else:
            url = url+"/api/v3/ai-maker/callback/scores/jobs/"+jobId+"/trials/"+trialId+"/?auth="+auth
    else:
        HEADERS = {"content-type": "application/json", "Authorization": "bearer "+token}
        # Remote job
        if serviceType == "SMTR":
            url = url+"/api/v1/ai-maker/callback/scores/remote-jobs/"+jobId+"/trials/"+trialId
        # Local job
        else:
            url = url+"/api/v1/ai-maker/callback/scores/jobs/"+jobId+"/trials/"+trialId

    body = json.dumps({KEY_SCORE_VALUE: scores})

    logging.debug("Headers: {}".format(HEADERS))
    logging.debug("Body: {}".format(body))
    logging.debug("Url: {}".format(url))

    try:                                                                                                      
        requests = retry_session()                                                                            
        r = requests.post(url, data=body, headers=HEADERS, verify=ASUS_CLOUDINFRA_VERIFY_ENABLE)                              
        logging.debug("Reponse: {}".format(r.text))                                                           
        r.raise_for_status()                                                                                  
        return "Update result OK"                                                                             
    except Exception as e:                                                                                    
        print(e)                                                                                              
        return "Update scores failed, please contact your system administrator"


def saveValidationResult(result):

    if isinstance(result, (int, float)) is False:
        logging.error(
            "[TypeError] Data type ({}) of result is not allowed".format(str(type(result))))
        return "Update result failed, please check data type of result."

    try:
        ASUS_CLOUDINFRA_VERIFY_ENABLE = 'True'
        if "ASUS_CLOUDINFRA_VERIFY_ENABLE" in os.environ:
            ASUS_CLOUDINFRA_VERIFY_ENABLE = os.getenv('ASUS_CLOUDINFRA_VERIFY_ENABLE')

        if ASUS_CLOUDINFRA_VERIFY_ENABLE == 'True' or ASUS_CLOUDINFRA_VERIFY_ENABLE == 'true':
            ASUS_CLOUDINFRA_VERIFY_ENABLE = True
        if ASUS_CLOUDINFRA_VERIFY_ENABLE == 'False' or ASUS_CLOUDINFRA_VERIFY_ENABLE == 'false':
            ASUS_CLOUDINFRA_VERIFY_ENABLE = False
            
        if "ASUS_CLOUDINFRA_JOB_ID" in os.environ:
            jobId = os.getenv('ASUS_CLOUDINFRA_JOB_ID')
        if "ASUS_CLOUDINFRA_TOKEN" in os.environ:
            token = os.getenv('ASUS_CLOUDINFRA_TOKEN')
        if "ASUS_CLOUDINFRA_API_HOST" in os.environ:
            url = os.getenv('ASUS_CLOUDINFRA_API_HOST')
        if "HOSTNAME" in os.environ:
            HOSTNAME = os.getenv('HOSTNAME')

        # This environment value was deprecated
        if "AI_MAKER_CRONJOB_ID" in os.environ:
            jobId = os.getenv('AI_MAKER_CRONJOB_ID')
        if "AI_MAKER_TOKEN" in os.environ:
            token = os.getenv('AI_MAKER_TOKEN')
        if "AI_MAKER_HOST" in os.environ:
            url = os.getenv('AI_MAKER_HOST')

    except KeyError as e:
        logging.error("[KeyError] Please assign {} value".format(str(e)))
        return "Update result failed, please contact your system administrator"

    # If ASUS_CLOUDINFRA_AUTH_KEY exist, call v3 api
    if "ASUS_CLOUDINFRA_AUTH_KEY" in os.environ:
        HEADERS = {"content-type": "application/json"}
        auth = os.getenv('ASUS_CLOUDINFRA_AUTH_KEY')
        url = url+"/api/v3/ai-maker/callback/results/validations/"+jobId+"/?auth="+auth
    else:
        HEADERS = {"content-type": "application/json", "Authorization": "bearer "+token}
        url = url+"/api/v1/ai-maker/callback/results/validations/"+jobId

    body = json.dumps({KEY_RESULT_VALUE: float(result), KEY_POD_NAME: str(HOSTNAME)})

    logging.debug("Headers: {}".format(HEADERS))
    logging.debug("Body: {}".format(body))
    logging.debug("Url: {}".format(url))

    try:                                                                                                      
        requests = retry_session()                                                                            
        r = requests.post(url, data=body, headers=HEADERS, verify=ASUS_CLOUDINFRA_VERIFY_ENABLE)                              
        logging.debug("Reponse: {}".format(r.text))                                                           
        r.raise_for_status()                                                                                  
        return "Update validation result OK"                                                                             
    except Exception as e:                                                                                    
        print(e)                                                                                              
        return "Update validation result failed, please contact your system administrator"
