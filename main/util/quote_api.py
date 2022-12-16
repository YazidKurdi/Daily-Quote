import requests
from main import scheduler

def get_quote():

    global author,content
    # print('hi')
    response = requests.get("https://api.quotable.io/random")

    if response.status_code == 200:
        data = response.json()
        # content, author = data["content"], data["author"]
        return data["content"], data["author"]
    else:
        return None, None

# author,content = get_quote()

# scheduler.add_job(id="scheduled task", func=get_quote, trigger='interval', seconds=10,replace_existing = True)
# scheduler.start()