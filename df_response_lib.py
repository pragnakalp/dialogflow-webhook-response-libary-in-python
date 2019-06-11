# Responses for Actions On Google
class actions_on_google_response():

    # class variable initializer initializer
    def __init__(self):
        self.platform = "ACTIONS_ON_GOOGLE"

    """
    Actions on Google Simple Response Builder
    @param name=display_text, type=list
    Sample example of display_text ex. [["Text to be displayed", "Text to  be spoken", True]]
    """
    def simple_response(self, responses):

        if len(responses) > 2:
            raise Exception(
                "Responses argument in simple response should have at most two elements only.")
        else:
            # a list to store the responses
            responses_json = []
            # iterate through the list of responses given by the user
            for response in responses:
                # if SSML = True, build the ssml response, else build textToSpeech
                # response[2] = SSML boolean
                if response[2]:
                    # response dictionary
                    response_dict = {
                        # text to be diplayed
                        "displayText": str(response[0]),
                        # ssml response to be spoken
                        "ssml": str(response[1])
                    }
                else:
                    response_dict = {
                        # text to be displayed
                        "displayText": str(response[0]),
                        # text to speech text
                        "textToSpeech": str(response[1])
                    }

                # add the response dict to the responses list
                responses_json.append(response_dict)

            # return the simple response JSON
            return {
                "platform": self.platform,
                "simpleResponses": {
                    "simpleResponses": responses_json
                }
            }

    """"
    Actions on Google Basic Card Builder
    @param title = string
    @param subtitle = string
    @param formattedText = string
    @param image = list [image_url, accessibility_text]
    @param buttons = list of [button_title, url_link]
    """
    def basic_card(self, title, subtitle="", formattedText="", image=None, buttons=None):
        # list to store buttons responses
        buttons_json = []
        if buttons is not None:
            # iterate through the buttons list
            for button in buttons:
                # add the buttons response to the buttons list
                buttons_json.append(
                    {
                        # title of the button
                        "title": button[0],
                        # url to be opened by the button
                        "openUriAction": {
                            "uri": button[1]
                        }
                    }
                )

            # return basic card JSON
            response = {
                "platform": self.platform,
                "basicCard": {
                    "title": title,
                    "subtitle": subtitle,
                    "formattedText": formattedText,
                    "buttons": buttons_json,
                    "image": {
                        "imageUri": image[0],
                        "accessibilityText": image[1]
                    }
                }
            }

        else:
            # return basic card JSON
            response = {
                "platform": self.platform,
                "basicCard": {
                    "title": title,
                    "subtitle": subtitle,
                    "formattedText": formattedText,
                    "image": {
                        "imageUri": image[0],
                        "accessibilityText": image[1]
                    }
                }
            }

        return response

    """
    Actions on Google List response
    @param list_title = string
    @param list_elements = list of list response items
    """
    def list_select(self, list_title, list_elements):
        # as per the actions on google response list items must be between 2 and 30
        if len(list_elements) > 30 or len(list_elements) < 2:
            raise Exception("List items must be two or less than 30.")
        else:
            # items list to store list elements
            items_list = []
            # iterate through the list elements list
            for list_element in list_elements:
                # append the items to the items_list
                items_list.append(
                    {
                        # title of the list item
                        "title": list_element[0],
                        # description of the list item
                        "description": list_element[1],
                        # info aabout the list item
                        "info": {
                            # key of the list items, key is used as user say string
                            "key": list_element[2][0],
                            # synonyms are the words that can be used as a value for the option when the user types instead of selecting from the list
                            "synonyms": list_element[2][1]
                        },
                        # list image
                        "image": {
                            # URL
                            "imageUri": list_element[3][0],
                            # accessibility text to be spoken
                            "accessibilityText": list_element[3][1]
                        }
                    }
                )

        # return the list response
        return {
            "platform": self.platform,
            "listSelect": {
                "title": list_title,
                "items": items_list
            }
        }

    """
    Actions on Google Suggestions chips resoponse
    @param suggestions = list of strings
    """    
    def suggestion_chips(self, suggestions):
        # suggestions_json to store the suggestions JSON
        suggestions_json = []
        # iterate through the suggestions list
        for suggestion in suggestions:
            # append the suggestion to the suggestions_json list
            suggestions_json.append(
                {
                    # title text to be displayed in the chip
                    "title": str(suggestion)
                }
            )

        # return the suggestion chips response JSON
        return {
            "platform": self.platform,
            "suggestions": {
                "suggestions": suggestions_json
            }
        }

    """
    Actions on Google Linkout suggestions
    @param title = string
    @param url = string (a valid URL)
    """
    def link_out_suggestion(self, title, url):
        # title should not be null
        if title == "" or url == "":
            raise Exception(
                "Provide the title and URL for link out suggestion response.")
        else:
            # return the link out suggestion response
            return {
                "platform": self.platform,
                "linkOutSuggestion": {
                    "destinationName": str(title),
                    "uri": str(url)
                }
            }

# Responses for Facebook
class facebook_response():

    # class variable initializer initializer
    def __init__(self):
        self.platform = "FACEBOOK"

    def text_response(self, texts):
        # text should contain at least one string
        if len(texts) <= 0:
            raise Exception("Provide the text for the text response")
        else:
            # text_obj list for storing the text variations
            text_obj = []
            for text in texts:
                text_obj.append(str(text))

            # return the text response
            return {
                "text": {
                    "text": text_obj
                },
                "platform": self.platform
            }

    def quick_replies(self, title, quick_replies_list):
        if title == "":
            raise Exception("Title is required for basic card in facebook.")
        # quick_replies_list must contains at least one string
        elif len(quick_replies_list) <= 0:
            raise Exception(
                "Quick replies response must contain at least on text string.")
        else:
            # quick replies list to store the quick replie text
            quick_replies = []
            for quick_reply in quick_replies_list:
                # append to the list
                quick_replies.append(
                    str(quick_reply)
                )

            # return the response JSON
            return {
                "quickReplies": {
                    "title": str(title),
                    "quickReplies": quick_replies
                },
                "platform": self.platform
            }

    def image_response(self, url):
        # check url
        if url == "":
            raise Exception("URL in the image response is required.")
        else:
            # return the JSON response
            return {
                "image": {
                    "imageUri": str(url)
                },
                "platform": self.platform
            }

    def card_response(self, title, buttons):
        buttons_json = []
        for button in buttons:
            buttons_json.append(
                {
                    "text": str(button[0]),
                    "postback": str(button[1])
                }
            )

        # return the card
        return {
            "card": {
                "title": str(title),
                "buttons": buttons_json
            },
            "platform": self.platform
        }

# Responses for Telegram
class telegram_response():

    # class variable initializer initializer
    def __init__(self):
        self.platform = "TELEGRAM"

    def text_response(self, texts):
        # text should contain at least one string
        if len(texts) <= 0:
            raise Exception("Provide the text for the text response")
        else:
            # text_obj list for storing the text variations
            text_obj = []
            for text in texts:
                text_obj.append(str(text))

            # return the text response
            return {
                "text": {
                    "text": text_obj
                },
                "platform": self.platform
            }

    def quick_replies(self, title, quick_replies_list):
        if title == "":
            raise Exception("Title is required for basic card in facebook.")
        # quick_replies_list must contains at least one string
        elif len(quick_replies_list) <= 0:
            raise Exception(
                "Quick replies response must contain at least on text string.")
        else:
            # quick replies list to store the quick replie text
            quick_replies = []
            for quick_reply in quick_replies_list:
                # append to the list
                quick_replies.append(
                    str(quick_reply)
                )

            # return the response JSON
            return {
                "quickReplies": {
                    "title": str(title),
                    "quickReplies": quick_replies
                },
                "platform": self.platform
            }

    def image_response(self, url):
        # check url
        if url == "":
            raise Exception("URL in the image response is required.")
        else:
            # return the JSON response
            return {
                "image": {
                    "imageUri": str(url)
                },
                "platform": self.platform
            }

    def card_response(self, title, buttons):
        buttons_json = []
        for button in buttons:
            buttons_json.append(
                {
                    "text": str(button[0]),
                    "postback": str(button[1])
                }
            )

        return {
            "card": {
                "title": str(title),
                "buttons": buttons_json
            },
            "platform": self.platform
        }


# dialogflow fulfillment response
class fulfillment_response():

    def __init__(self):
        pass

    # fulfillment text builder
    # @param fulfillmentText = string
    def fulfillment_text(self, fulfillmentText):        
        if fulfillmentText == "":
            raise Exception("Fulfillment text should not be empty.")
        else:
            return {
                "fulfillment_text": str(fulfillmentText)
            }

    # fulfillment messages builder
    # @param response_objects (AOG response, FB response, Telegram response)
    def fulfillment_messages(self, response_objects):
        if len(response_objects) <= 0:
            raise Exception(
                "Response objects must contain at least one response object.")
        else:
            return {
                "fulfillment_messages": response_objects
            }

    # dialogflow output contexts
    # @param session = dialogflow session id
    # @param contexts = context name (string)
    def output_contexts(self, session, contexts):
        contexts_json = []
        for context in contexts:
            contexts_json.append({
                "name": session + "/contexts/" + context[0],
                "lifespanCount": context[1],
                "parameters": context[2]
            })

        # return the output context json
        return {
            "output_contexts": contexts_json
        }

    # dialogflow followup event JSON
    # @param name = event name
    # @param parameters = key value pair of parameters to be passed
    def followup_event_input(self, name, parameters):
        return {
            "followup_event_input": {
                "name": str(name),
                "parameters": parameters
            }
        }

    # main response with fulfillment text and fulfillment messages
    # @param fulfillment_text = fulfillment_text JSON
    # @param fulfillment_messages = fulfillment_messages JSON
    # @param output_contexts = output_contexts JSON
    # @param followup_event_input = followup_event_input JSON
    def main_response(self, fulfillment_text, fulfillment_messages=None, output_contexts=None, followup_event_input=None):
        if followup_event_input is not None:
            if output_contexts is not None:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages'],
                        "outputContexts": output_contexts['output_contexts'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "outputContexts": output_contexts['output_contexts'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
            else:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "followupEventInput": followup_event_input['followup_event_input']
                    }
        else:
            if output_contexts is not None:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages'],
                        "outputContexts": output_contexts['output_contexts']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "outputContexts": output_contexts['output_contexts']
                    }
            else:
                if fulfillment_messages is not None:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text'],
                        "fulfillmentMessages": fulfillment_messages['fulfillment_messages']
                    }
                else:
                    response = {
                        "fulfillmentText": fulfillment_text['fulfillment_text']
                    }

        # return the main dialogflow response
        return response
