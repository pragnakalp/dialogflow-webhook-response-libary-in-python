#==============================================================================
# title              : facebook_template_lib.py
# description        : This library is used to prepare custom payload for Facebook Messenger generic template with elements like image, title, subtitle, URL button and postback button. It will automatically create carousel if more than 1 generic templates are passed. 
# author             : Pragnakalp Techlabs
# email              : letstalk@pragnakalp.com
# website            : https://www.pragnakalp.com
#==============================================================================

class FacebookTemplate():
    '''Create generic facebook messenger tempalte. '''
    def __init__(self):
        self.payload = {
                    "facebook": {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type":"generic",
                            "elements": [

                            ]
                        }
                    }
                }
            }

    def add_element(self, element_obj):
        self.payload['facebook']['attachment']['payload']['elements'].append(element_obj)

    def get_payload(self):
        return self.payload

class TemplateElement():
    ''' Add title, subtitle, image, buttons and action elements in generic template response.'''
    def __init__(self, title, subtitle):
        self.element = {
                    "title": title,
                    "subtitle": subtitle
            }

    def add_image_url(self, url):
        self.element['image_url'] = url

    def add_default_action(self, url, type, webview_height_ratio):
        self.element["default_action"]={
                        "url":url,
                        "type": type,
                        "webview_height_ratio": webview_height_ratio
                }

    def add_button(self, button_obj):
        self.element['buttons']=[button_obj]

    def get_element(self):
        return self.element

class TemplateElementButton():
    '''Types of buttons that can be added in response.'''
    def __init__(self, button_type, title):
        self.button = {
                "type": button_type,
                "title": title 
            }

    def add_web_url(self, url):
        assert self.button['type']=='web_url', "Error: button type must be 'web_url'" 
        self.button['url'] = url

    def add_payload(self, payload):
        assert self.button['type']=='postback', "Error:button type must be 'postback'"
        self.button['payload'] = payload

    def get_button(self):
        return self.button