import requests


def get_chuck_norris_joke():

    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": "b90e5dcc2fmshbe6471de1d4ce0ep1a0460jsn3aa043b26779",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        msg = f'Request failed with code {response.status_code}'
        raise RuntimeError(msg)
    joke = response.json()["value"]
    return joke

# print(get_chuck_norris_joke())









    # you can check response with:
    # print(response.json())
    # you can check status code with:
    # print(response.status_code)


'''
Task: write the function what will check that request is success. If response success function should return 
string massage with joke, otherwise function should rice RuntimeError. Write tests for this function with Mock.
1 - with success request (Mock all response json from json file)
2 - with success request (Mock just massage in test)
3 - with not success response and status_code 404
'''

