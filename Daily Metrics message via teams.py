import requests

# Your webhook URL
TEST_ROHIT = "https://dpz.webhook.office.com/webhookb2/bceadde6-e3cd-48a5-9597-62dfa2d497a6@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/2481ad04259a44858b9845b36d006718/dbec4612-7385-4673-b29b-fbe8d79f51fa/V2bGymXpz0hdQbheBzwQDwIo9jakGDl2pwEo4uMLbJq6E1"
RELEASE_TEAM_CHAT = "https://dpz.webhook.office.com/webhookb2/57b5f37d-d48f-4e71-99fa-1939cef465b5@7c30dbb8-800e-499b-b8d6-68776f8bc954/IncomingWebhook/21b1291156e34237bc0faad6864d98a7/dbec4612-7385-4673-b29b-fbe8d79f51fa/V2b0dyWP6PwnKSDeAUAsrFTc9F61Ydk0BI43qKSOjtnEI1"
#WEBHOOK_URL_3 = ""

# Define the message content
message = {
    "text": "Good morning Everyone !! Here is release metrics for 01/27/2025 Major Release. 🌞",
    "themeColor": "0076D7",  # Optional: Hex code for a colored header
    "summary": "Daily Update",  # Optional: Summary text
    "sections": [
        {
            "activityTitle": "Cadence",
            "facts": [
                {"name": "01/13/2024 (Week 1 of sprint)", "value": ""}, 
                {"name": "", "value": """\n
- Please make sure that all tickets (artifact, configs, LaunchDarkly) for the 01/27/2025 Major release are added to the Production Release Board.
- Monday - Friday: QA testing continues and moving to preprod\n"""},

                {"name": "01/20/2025 (week 2 of sprint)", "value": ""},
                {"name": "", "value": """\n
- Monday 01/20/2025: Holiday
- Tuesday 01/21/2025: Done in Preprod by EOD
- Wednesday 01/22/2025: Moving to inactive
- Thursday 01/23/2025: Fully deployed to inactive by 5:00 PM
- Friday 01/24/2025: No new deploys"""}
            ],
            "markdown": True  # This enables markdown formatting in Teams
        }
    ]
}

# Send the POST request
response_1 = requests.post(TEST_ROHIT, json=message)
response_2 = requests.post(RELEASE_TEAM_CHAT, json=message)
#response_3 = requests.post(WEBHOOK_URL_3, json=message)

# Check the responses for each webhook URL
if response_1.status_code == 200:
    print("Message sent successfully to TEST_ROHIT!")
else:
    print(f"Failed to send message to TEST_ROHIT: {response_1.status_code}, {response_1.text}")

if response_2.status_code == 200:
    print("Message sent successfully to RELEASE_TEAM_CHAT!")
else:
    print(f"Failed to send message to RELEASE_TEAM_CHAT: {response_2.status_code}, {response_2.text}")

#if response_3.status_code == 200:
#    print("Message sent successfully to WEBHOOK_URL_3!")
#else:
#    print(f"Failed to send message to WEBHOOK_URL_3: {response_3.status_code}, {response_3.text}")
