import requests
from requests.exceptions import HTTPError
from keys import API_KEY, APP_KEY

def request_url(*param, req='search', form='json', api_url='http://api.duma.gov.ru/api/',
                token=API_KEY, app_token=APP_KEY, mode=None):
    """
    Function for API GET-request

    Parameters
    ----------
    :param param: 
    List of request parameters objects
        list, tuple

    :param req: 
    Type of request
        string, default 'search'

    :param form:
    Type of data in response
        string, default 'json'

    :param api_url, token, app_token:
    Components of requested url
        default 'http://api.duma.gov.ru/api/', API_KEY, APP_KEY

    :param mode:
    If 'print' - is printed text form of response
        string, default None

    """

    body = api_url + token + '/' + req + '.' + form + '?' + 'app_token=' + app_token
    if param:
        for i in param:
            body = body + '&' + i
    
    try:
        response = requests.get(body)
        if response.status_code == 200:
            print('200 Success!')
        elif response.status_code == 404:
            print('404 Not Found!')
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred: {}'.format(http_err))
    except Exception as err:
        print('Other error occurred: {}'.format(err))

    if mode == 'print':
        for j in response.json().items():
            print(str(j[0]) + ': ' + str(j[1]))
        
    return response