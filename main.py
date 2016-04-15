from flask import Flask
from flask import request
import logging
import messenger_tools


app = Flask(__name__)
#app.debug = True

if not app.testing:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def hello():
    logging.info('HELLOOOOOO')
    logging.debug("Coolllll")
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    #Receive a message

    if request.method == 'POST':
        #return "coucou"
        update = request.get_json()
        logging.info(update)
        entry = update["entry"][0]
        messaging_events = entry["messaging"]

        for event in messaging_events:
            if "message" in event:
                logging.info(event["message"]["text"])
                response = "Echo response : " + event["message"]["text"]
                r = messenger_tools.send_message(event["sender"], response)
                if r.status_code != 200:
                    logging.error(r.text)
                else:
                    logging.info("Message sent")
        return "coco"

    #Verify
    else:
        if request.args["hub.verify_token"] == "adrien":
            return request.args["hub.challenge"]
        else:
            return 'Hello World!'



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
# [END app]
