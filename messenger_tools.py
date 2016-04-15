import requests

def send_message(sender, text):
    payload = {'access_token': 'CAAYY6pv7jEUBAPtKvZCNZC7ktoZBP782EfPWXLXULdSOEtt7Vp8m6L40oO4bdZCZADomd4gEGZAkUulNWfnGpNV7PPtJUOs1ufZA7Tr3424lLtZC29PEVMC0r75rUwI8gSZCb0P7FrkbBZAUnlNN43OM9ZCOWWYMAHFVWZCXh5vKLCp2t7xtpvhk1m8j3J1YVndbm0b0xnNi3ZCZAQOQZDZD'}
    json_payload = {'recipient': {"id" : sender["id"]}, "message" : {"text" : text}}
    r = requests.post(
        'https://graph.facebook.com/v2.6/me/messages',
        params = payload,
        json = json_payload)
    return r

def sendGenericMessage(sender):
    messageData = {
    	"attachment": {
    		"type": "template",
    		"payload": {
    			"template_type": "generic",
    			"elements": [{
    				"title": "First card",
    				"subtitle": "Element #1 of an hscroll",
    				"image_url": "http://messengerdemo.parseapp.com/img/rift.png",
    				"buttons": [{
    					"type": "web_url",
    					"url": "https://www.messenger.com/",
    					"title": "Web url"
    				}, {
    					"type": "postback",
    					"title": "Postback",
    					"payload": "Generic payload"
    				}]
    			}, {
    				"title": "Second card",
    				"subtitle": "Element #2 of an hscroll",
    				"image_url": "http://messengerdemo.parseapp.com/img/gearvr.png",
    				"buttons": [{
    					"type": "postback",
    					"title": "Postback",
    					"payload": "Payload for second element in a generic bubble"
    				}]
    			}]
    		}
    	}
    }

    payload = {'access_token': 'CAAYY6pv7jEUBAPtKvZCNZC7ktoZBP782EfPWXLXULdSOEtt7Vp8m6L40oO4bdZCZADomd4gEGZAkUulNWfnGpNV7PPtJUOs1ufZA7Tr3424lLtZC29PEVMC0r75rUwI8gSZCb0P7FrkbBZAUnlNN43OM9ZCOWWYMAHFVWZCXh5vKLCp2t7xtpvhk1m8j3J1YVndbm0b0xnNi3ZCZAQOQZDZD'}
    json_payload = {'recipient': {"id" : sender["id"]}, "message" : messageData}
    r = requests.post(
        'https://graph.facebook.com/v2.6/me/messages',
        params = payload,
        json = json_payload)
    return r
