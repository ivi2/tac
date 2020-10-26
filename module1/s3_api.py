"""Testing web APIs with HTTP GET method"""

import json
import sys

import requests


def love_calculation(first_name, second_name):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"fname":first_name,"sname":second_name}

    headers = {
        'x-rapidapi-host': "love-calculator.p.rapidapi.com",
        'x-rapidapi-key': "4a17219b1dmsh97bc19de5759eedp1bf0c4jsnf3cbe76baeed"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_result = json.loads(response.text)

    fname = json_result['fname']
    sname = json_result['sname']
    percentage = json_result['percentage']
    result = json_result['result']

    print(fname + " and "+ sname + ", your love percentage is: "+ percentage +"%. "+ result)



if __name__ == "__main__":
    try:
        name_1 = sys.argv[1]
        name_2 = sys.argv[2]

        try:
            love_calculation(name_1, name_2)
        except IndexError:
            print("Please enter two names")
    except IndexError:
        print("Missing action, please enter two names")
