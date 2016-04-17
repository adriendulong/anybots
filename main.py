from flask import Flask
from flask import request
import logging
import json
import messenger_tools
import config
import model_sql
import const


app = Flask(__name__)
#app.debug = True
app.config.from_object(config)

if not app.testing:
    logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.DEBUG)

#Set SQL
with app.app_context():
    model_sql.init_app(app)


@app.route('/')
def hello():
    model_sql.create_message_test()
    logging.info('HELLOOOOOO')
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/sendmessage/<iduser>/<message>')
def sendMessage(iduser,message):
    iduser = const.adrien_facebook_id
    r = messenger_tools.send_message(iduser, message)
    if r.status_code != 200:
        logging.error(r.text)
    else:
        logging.info("Message sent")
    return 'Message "'+message+'" sent to the user '+iduser


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    #Receive a message

    if request.method == 'POST':
        #Get Json message
        update = request.get_json()
        logging.info(update)
        entry = update["entry"][0]
        messaging_events = entry["messaging"]

        #Iterate through messages
        for event in messaging_events:
            if "message" in event:
                #Save the message in the SQL base
                model_sql.create_message(event)
                if "text" in event["message"]:
                    messageReceived = event["message"]["text"]
                    logging.info("Message received : "+messageReceived)

                    #In this case we send a generic message
                    if messageReceived == "Generic":
                        r = messenger_tools.sendGenericMessage(event["sender"]["id"])
                        if r.status_code != 200:
                            logging.error(r.text)
                        else:
                            logging.info("Message sent")
                    #Otherwise we just echo the message
                    else:
                        response = "Echo response : " + event["message"]["text"]
                        r = messenger_tools.send_message(event["sender"]["id"], response)
                        if r.status_code != 200:
                            logging.error(r.text)
                        else:
                            logging.info("Message sent")
            elif "postback" in event:
                logging.info("Just received a POSTBACK")
                r = messenger_tools.send_message(event["sender"]["id"], str(event["postback"]))
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
