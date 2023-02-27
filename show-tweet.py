import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r

def get_tweets(ids):
    s = ids[0]
    for i in range(1, len(ids)-1):
      s=s+","+ids[i]
    response = requests.get(
        "https://api.twitter.com/2/tweets?ids="+s+"&tweet.fields=geo,attachments&expansions=attachments.media_keys,geo.place_id&place.fields=geo&media.fields=height,url", auth=bearer_oauth, stream=False,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))


def get_geo(id):
    response = requests.get(
        "https://api.twitter.com/1.1/geo/id/"+id+".json", auth=bearer_oauth, stream=False,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))

def main():
    get_tweets(["1626948664026333186"])
    #get_geo("7519d5ef0b317d8f")


if __name__ == "__main__":
    main()

