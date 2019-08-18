import sys
import speedtest
import time
import requests


def get_speed():
    """
    Use Speedtest CLI to test bandwidth speed.
        :return: Download speed in Mbps
    """
    s = speedtest.Speedtest()
    s.download()
    results_dict = s.results.dict()
    return results_dict['download'] / 1048576  # convert bits to megabits


def send_speed(url, data, pw):
    """
    Send bandwidth result to external source.
        :param url: Endpoint to send a POST request to
        :param data: Dictionary of speed, units, and time
        :param pw: Password for the endpoint
        :return: status code of the request
    """
    data['pw'] = pw
    r = requests.post(url, json=data)
    return r.status_code


if __name__ == '__main__':
    endpoint = sys.argv[1]  # endpoint to save results
    pw = sys.argv[2]  # password for endpoint
    speed = get_speed()
    status = send_speed(
        endpoint, {"speed": speed, "units": "Mbps", "date": time.time()}, pw)
    print(status)
