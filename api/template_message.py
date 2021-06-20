def last_week_statistics_template(one_star, two_star, three_star, four_star, five_star, name, date, median_rating):
    return {
        "channel": "#reviewgator-chat",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Стастика приложения за последнюю неделю:",
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Название приложения*: *{name}*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Средний рейтинг оценок за последнюю неделю : {median_rating}*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f": *{one_star}*"
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text":  f": *{two_star}*",
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text":  f": *{three_star}*",
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828970.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f": *{four_star}*",
                    }
                ]
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "image",
                        "image_url": "https://image.flaticon.com/icons/png/512/1828/1828961.png",
                        "alt_text": "cute cat"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f": *{five_star}*",
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Дата*: _{date}_ :ghost:"
                }
            }
        ]
    }
