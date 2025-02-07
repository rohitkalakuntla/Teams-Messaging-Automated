import requests

with open('message.md', 'r') as file:
    message_text = file.read()

message = {
    "text": message_text,
    "markdown": True
}


# Your webhook URL
TEST_ROHIT = "https://dpz.webhook.office.com/webhookb2/bceadde6-e3cd-48a5-9597-62dfa2d497a6@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/2481ad04259a44858b9845b36d006718/dbec4612-7385-4673-b29b-fbe8d79f51fa/V2bGymXpz0hdQbheBzwQDwIo9jakGDl2pwEo4uMLbJq6E1"
#RELEASE_TEAM_CHAT = "https://dpz.webhook.office.com/webhookb2/57b5f37d-d48f-4e71-99fa-1939cef465b5@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/21b1291156e34237bc0faad6864d98a7/dbec4612-7385-4673-b29b-fbe8d79f51fa/V2b0dyWP6PwnKSDeAUAsrFTc9F61Ydk0BI43qKSOjtnEI1"
#MAJOR_OFFCADENCE_CHANNEL = "https://dpz.webhook.office.com/webhookb2/57b5f37d-d48f-4e71-99fa-1939cef465b5@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/91461501af614041a0f87cc91fe2377c/dbec4612-7385-4673-b29b-fbe8d79f51fa/V2vc_7sRnOHObE6dFin50F-zPDelL3dCrmOAY__44umN01"
#ALSEA_ECOMMERCE = "https://dpz.webhook.office.com/webhookb2/58926fbd-0a22-4c0f-9e83-04ebd293865e@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/54eea45a794e4db6a315b700b681e95d/f3f3bc7c-2955-4f51-b6a0-37416ba9890b/V2_wdKkZ6kZpE4TSeZQLOq4mZcvjzJUK7Qtj9dJVCDgfc1"
#CANADA_ECOMMERCE = "https://dpz.webhook.office.com/webhookb2/7e5dce89-7232-442d-8297-a3fe35f79d87@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/d81c0eec3e0a4961a9bf881349be010e/f3f3bc7c-2955-4f51-b6a0-37416ba9890b/V2Xc5Ldon4DrbjVgAOWEaTlszkIbwUxfWAbGwXNS-fwfc1"
#GLOBAL_ECOMM_DEVOPS = "https://dpz.webhook.office.com/webhookb2/8afcd368-f423-4039-b7ff-50eb5819fe3e@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/78d565dfa2124b91ae971fe6b656e947/f3f3bc7c-2955-4f51-b6a0-37416ba9890b/V2cTkmdY2oknPyOV2qaL359GsuzcRJdS6cTQfIItzcHmo1"
#WEBHOOK_URL_3 = ""

# Send the POST request
response_1 = requests.post(TEST_ROHIT, json=message)
#response_2 = requests.post(RELEASE_TEAM_CHAT, json=message)
#response_3 = requests.post(MAJOR_OFFCADENCE_CHANNEL, json=message)
#response_4 = requests.post(ALSEA_ECOMMERCE, json=message)
#response_5 = requests.post(CANADA_ECOMMERCE, json=message)
#response_6 = requests.post(GLOBAL_ECOMM_DEVOPS, json=message)

# Check the responses for each webhook URL
if response_1.status_code == 200:
    print("Message sent successfully to TEST_ROHIT!")
else:
    print(f"Failed to send message to TEST_ROHIT: {response_1.status_code}, {response_1.text}")

#if response_2.status_code == 200:
#    print("Message sent successfully to RELEASE_TEAM_CHAT!")
#else:
#    print(f"Failed to send message to RELEASE_TEAM_CHAT: {response_2.status_code}, {response_2.text}")
#
#if response_3.status_code == 200:
#    print("Message sent successfully to MAJOR_OFFCADENCE_CHANNEL!")
#else:
#    print(f"Failed to send message to MAJOR_OFFCADENCE_CHANNEL: {response_3.status_code}, {response_3.text}")
#
#if response_4.status_code == 200:
#    print("Message sent successfully to ALSEA_ECOMMERCE!")
#else:
#    print(f"Failed to send message to ALSEA_ECOMMERCE: {response_4.status_code}, {response_4.text}")
#
#if response_5.status_code == 200:
#    print("Message sent successfully to CANADA_ECOMMERCE!")
#else:
#    print(f"Failed to send message to CANADA_ECOMMERCE: {response_5.status_code}, {response_5.text}")
#
#if response_6.status_code == 200:
#    print("Message sent successfully to GLOBAL_ECOMM_DEVOPS!")
#else:
#    print(f"Failed to send message to GLOBAL_ECOMM_DEVOPS: {response_6.status_code}, {response_6.text}")
#
#if response_3.status_code == 200:
#    print("Message sent successfully to WEBHOOK_URL_3!")
#else:
#    print(f"Failed to send message to WEBHOOK_URL_3: {response_3.status_code}, {response_3.text}")
