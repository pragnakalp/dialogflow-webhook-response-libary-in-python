## Dialogflow Fulfillment Webhook Response Library in Python

This library simplifies the JSON response building in Python for Dialogflow fulfillment.

Using this libray you can build the JSON objects with few line.

**Supported Platforms** - Actions on Google, Facebook Messenger and Telegram

## How to use
To get started just import all the functions from the library using the following statement

 `from df_response_lib import *`

## Supported Responses

**Actions on Google**

 - Simple Response
 - Basic Card
 - Suggestion Chips
 - Link out suggestion
 - List Response
 - More will be added soon

**Facebook** and **Telegram**

 - Text Response
 - Card Response
 - Image Response
 - Quick replies

**Dialogflow Fulfillment Responses**

 - Fulfillment Text
 - Fullfillment Messages
 - Followup Event Input
 - Output Contexts

## Actions on Google

### **Simple Response**
```python 
simple_response(responses)
```

***responses*** - list of simple responses
```python
["Text to be displayed", "Text to be spoken", ssml=True|False]
```

ex.
```python
aog_sr = aog.simple_response([
	["Hello", "Hi", False],
	["Hey!!", "<speak>Hey</speak>", True]
])
```

### **Basic Card**

```python
basic_card(title, subtitle="", formattedText="", image=None, buttons=None)
```

***title***  is the title of card - string
***subtitle*** is the subtitle of the card - string
***formattedText*** is the description of the card - limited markdown
***image*** display image in the card - list
```python
image = [imageUri, accessibilityText]
```
***buttons*** add buttons to thr card
```python
buttons = [
	[button_title, url]
]
```
ex.
```python
image = ['https://imagepath.com/path.png', 'sample image']

buttons = [
	['button_1', 'https://www.google.com/'],
	['button 2', 'https://www.facebook.com/']
]

aog_card = aog.basic_card("card title", "card subtitle", "card *description*", image, buttons)
```

### **Suggestion Chips**
```python
suggestion_chips(suggestions)
```
***suggestions*** - list of suggestions upto 8 items (one item length upto 25)
```python
suggestions = ['chip1', 'chip2', 'chip3', 'chip4']
```

ex. 
```python
aog_suggestions = aog.suggestion_chips(suggestions)
```

### **Link out Suggestion**
```python
link_out_suggestion(title, url)
```
***title*** - Text to be shown in suggestion
***url*** - Link URL

ex.
```python
title = "Link to google"
url = "https://www.google.com/"
aog_los = aog.link_out_suggestion(title, url)
```

### **List Select Response**

```python
list_select(list_title, list_elements)
```
***list_title*** - title of the list
***list_elements*** - list of items of the list select
```python
[
	['item_title', 'item_description', item_info=['item_key', item_synonyms=['synonym1', 'synonym2']],
	['item2_title', 'item2_description', item_info=['item_key', item_synonyms=['synonym1', 'synonym2']]
]
```

ex.
```python
list_elements = [
	['item_title', 'item_description', ['item_key', ['synonym1', 'synonym2']],
	['item2_title', 'item2_description', ['item2_key',['synonym1', 'synonym2']]
]

aog_list = aog.list_select("this is a list', list_elements)
```
## Facebook and Telegram

### **Text response**
```python
text_response(texts)
```
***texts*** - list of text
```python
['text1', 'text2', 'text3']
```
ex.
```python
texts = ['text1', 'text2', 'text3']
text_res = fb.text_response(texts)
```

### **Quick Replies**
```python
quick_replies(title, quick_replies_list)
```
***quick_replies_list*** - list of quick replies text
```python
['reply1', 'reply2', 'reply3']
```
ex.
```python
title = "Choose something"
replies= ['reply1', 'reply2', 'reply3']
fb_quick_replies = fb.quick_replies(title, replies)
```
### **Image Response**
```python
image_response(url)
```
***url*** - image URL

ex.
```python
url = "https://www.xyz.com/image.png"
fb_image = fb.image_response(url)
```

### **Card Response**

```python
card_response(title, buttons)
```
***card title*** - title of the card
***buttons*** - list of buttons
```python
[
	['button1', 'hello'],
	['button2', 'hello again']
]
```

ex.
```python
title = "this is a card"
buttons = [
	['button1', 'hello'],
	['button2', 'hello again']
]

fb_card = fb.card_response(title, buttons)
```
---
We are working to add more responses in the future. Please give your feedback and do contribute if you like.

> Developed by Pragnakalp
