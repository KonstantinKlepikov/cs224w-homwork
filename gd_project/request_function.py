import requests
from requests.exceptions import HTTPError
from keys import API_KEY, APP_KEY

def request_url(*param, req='search', form='json', api_url='http://api.duma.gov.ru/api/',
                token=API_KEY, app_token=APP_KEY, mode=None):
    """
    Function for API GET-request

    Format
    ------

    http://api.duma.gov.ru/api/:token/:request.:format?app_token=:app_token&param1=1&param2=2

    :token — API-key;
    :app_token — APP-key;
    :request — mode of request;
    :format — fomat of data;
    param1, param2 — parameters of request.

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
            if mode == 'print':
                print('200 Success!')
                if response.json():
                    for j in response.json().items():
                        print(str(j[0]) + ': ' + str(j[1]))
                else:
                    print(body)
                    print('Empty json in response')
                print('')

        elif response.status_code == 404:
            print('404 Not Found!')
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred: {}'.format(http_err))
    except Exception as err:
        print('Other error occurred: {}'.format(err))
        
    return response