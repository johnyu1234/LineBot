import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, TemplateAction, Template, PostbackTemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, ImageSendMessage, ImagemapSendMessage, CarouselTemplate, CarouselColumn
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
def push_message(userid, msg):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message(userid, TextSendMessage(text=msg))
    return "OK"

def send_image_carousel(id, imglinks, labels, texts):
    line_bot_api = LineBotApi(channel_access_token)
    cols = []
    for i, url in enumerate(imglinks):
        print(i)
        cols.append(
            ImageCarouselColumn(
                    image_url=url,
                    action=MessageTemplateAction(
                    label=labels[i],
                    text=texts[i]
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(id, message)
    return "OK"
def send_button_message(id, img, title, uptext, labels, texts):
    line_bot_api = LineBotApi(channel_access_token)
    
    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
        thumbnail_image_url=img,
        title=title,
        text=uptext,
        actions=acts
        )
    )
    line_bot_api.push_message(id, message)
    return "OK"
def send_button_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cdn.thewirecutter.com/wp-content/uploads/2020/04/laptops-lowres-2x1--1024x512.jpg',
                    title='Laptop',
                    text='What would you like to do?',
                    actions=[
                        MessageTemplateAction(
                            label='Search for a laptop',
                            text='search laptop'
                        ),
                        MessageTemplateAction(
                            label='Standings',
                            text='show standing'
                        ),
                        MessageTemplateAction(
                            label='Game Schedule',
                            text='show schedule'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.howtogeek.com/wp-content/uploads/2018/10/cpu_lede.png',
                    title='CPU',
                    text='What would you like to do?',
                    actions=[
                        MessageTemplateAction(
                            label='Top 5 Laptop CPU',
                            text='top laptop cpu'
                        ),
                        MessageTemplateAction(
                            label='Game Result',
                            text='game box score'
                        ),
                        MessageTemplateAction(
                            label='Search Player',
                            text='search player'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.reviewsontop.com/wp-content/uploads/2020/03/X5TyA8uvkGXoNyjFzxcowS-1200-80.jpg',
                    title='New to buying your own laptop?',
                    text='click here to find the right one',
                    actions=[
                        MessageTemplateAction(
                            label='High Tier Gaming',
                            text='high game'
                        ),
                        MessageTemplateAction(
                            label='Mid Tier Gaming',
                            text='mid game'
                        ),
                        MessageTemplateAction(
                            label='Programming',
                            text='program'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"
def send_image_url(id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
        )
    line_bot_api.reply_message(id, message)

    return "OK"
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
