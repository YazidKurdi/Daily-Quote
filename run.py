from main import app,scheduler
from main.util.quote_api import get_quote


if __name__ == "__main__":
    # scheduler.add_job(id = "scheduled task",func= get_quote,trigger = 'interval',seconds = 5)
    # scheduler.start()
    app.run(host = "0.0.0.0", port = 5000)

