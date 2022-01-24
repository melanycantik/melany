from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None


class Home(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Halaman Home": [
                        {
                            "header": [
                                {
                                    "top": [
                                        {
                                            "left":
                                            {
                                                "img": "game warrior",
                                                "url": "https://preview.colorlib.com/theme/gamewarrior/index.html"
                                            }
                                        },
                                        {
                                            "right": [
                                                {
                                                    "text": "home",
                                                    "url": "https://preview.colorlib.com/theme/gamewarrior/index.html"
                                                },
                                                {
                                                    "text": "game",
                                                    "url": "https://preview.colorlib.com/theme/gamewarrior/review.htm"
                                                },
                                                {
                                                    "text": "blog",
                                                    "url": "https://preview.colorlib.com/theme/gamewarrior/categories.html"
                                                },
                                                {
                                                    "text": "forums",
                                                    "url": "https://preview.colorlib.com/theme/gamewarrior/community.html"
                                                },
                                                {
                                                    "text": "contact",
                                                    "url": "https://preview.colorlib.com/theme/gamewarrior/contact.html"
                                                },
                                                {
                                                    "icons": "lonjong",
                                                    "text": "login/register",
                                                    "url": "https://preview.colorlib.com/theme/gamewarrior/#"

                                                }

                                            ]
                                        }
                                    ]

                                }
                            ],
                            "sliderbar": [
                                {
                                    "image slider": [
                                        {
                                            "img": "foto 1",
                                            "url": "img/slider-1.jpg"

                                        },
                                        {
                                            "img": "foto 2",
                                            "url": "img/slider-2.jpg"

                                        },
                                        {
                                            "img": "foto 3",
                                            "url": "img/slider-1.jpg"

                                        },
                                        {
                                            "img": "foto 4",
                                            "url": "img/slider-2.jpg"

                                        }
                                    ]
                                },
                                {
                                    "text slider": [
                                        {
                                            "text": "the best games out there"
                                        },
                                        {
                                            "text": "lorem ipsum dolor sit amet,consectetur adipiscin elit."
                                        },
                                        {
                                            "text": "read more"
                                        },
                                        {
                                            "text": "01"
                                        },
                                        {
                                            "text": "02"
                                        },
                                        {
                                            "left":
                                            {
                                                "text": "latest news"
                                            }
                                        },
                                        {
                                            "right": [
                                                {
                                                    "text": "new"
                                                },
                                                {
                                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "strategy"
                                                },
                                                {
                                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "racing"
                                                },
                                                {
                                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "body 1": [
                                {
                                    "template": [
                                        {
                                            "template 1": [
                                                {
                                                    "img": "foto one"
                                                },
                                                {
                                                    "text": "new"
                                                },
                                                {
                                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "3 comments"
                                                }
                                            ],
                                            "template 2": [
                                                {
                                                    "img": "foto two"
                                                },
                                                {
                                                    "text": "strategy"
                                                },
                                                {
                                                    "text": "justo tempor, rutrum erat id, molestie"
                                                },
                                                {
                                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "3 comments"
                                                }
                                            ],
                                            "template 3": [
                                                {
                                                    "img": "foto three"
                                                },
                                                {
                                                    "text": "new"
                                                },
                                                {
                                                    "text": "nullam lacinia ex eleifend orci porttitor"
                                                },
                                                {
                                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "3 comments"
                                                }
                                            ],
                                            "template 4": [
                                                {
                                                    "img": "foto four"
                                                },
                                                {
                                                    "text": "racing"
                                                },
                                                {
                                                    "text": "lacinia ex eleifend orci suscipit"
                                                },
                                                {
                                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "3 comments"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "body 2": [
                                {
                                    "permainan baru": [
                                        {
                                            "text": "new"
                                        },
                                        {
                                            "text": "recent games"
                                        },
                                        {
                                            "game 1": [
                                                {
                                                    "img": "foto 1",
                                                    "url": "img/recent-game-bg.png"
                                                },
                                                {
                                                    "text": "new"
                                                },
                                                {
                                                    "text judul": "Suspendisse ut justo tem por, rutrum"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                },
                                                {
                                                    "text": "3 comments"
                                                },
                                                {
                                                    "img": "foto bintang",
                                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                },
                                                {
                                                    "img": "foto love",
                                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                }
                                            ],
                                            "game 2": [
                                                {
                                                    "img 2": "foto 2",
                                                    "url": "img/recent-game/2.jpg"
                                                },
                                                {
                                                    "text": "racing"
                                                },
                                                {
                                                    "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                },
                                                {
                                                    "text": "3 comments"
                                                },
                                                {
                                                    "img": "foto bintang",
                                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                },
                                                {
                                                    "img": "foto love",
                                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                }
                                            ],
                                            "game 3": [
                                                {
                                                    "img 3": "foto3",
                                                    "url": "img/recent-game/3.jpg"
                                                },
                                                {
                                                    "text": "adventure"
                                                },
                                                {
                                                    "text judul": "Suspendisse ut justo tem por, rutrum"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                },
                                                {
                                                    "text": "3 comments"
                                                },
                                                {
                                                    "img": "foto bintang",
                                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                },
                                                {
                                                    "img": "foto love",
                                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "body 3": [
                                {
                                    "turnamen": [
                                        {
                                            "text": "tournaments"
                                        },
                                        {
                                            "turnamen 1": [
                                                {
                                                    "text": "premium tournament"
                                                },
                                                {
                                                    "img": "foto 1",
                                                    "url": "img/tournament/1.jpg"
                                                },
                                                {
                                                    "text judul": "World Of WarCraft"
                                                },
                                                {
                                                    "text beggins": "Tournament Beggins:June 20, 2018"
                                                },
                                                {
                                                    "text ends": "Tounament Ends:July 01, 2018"
                                                },
                                                {
                                                    "text participants": "Participants:10 teams"
                                                },
                                                {
                                                    "text tournament": "Tournament Author:Admin"
                                                },
                                                {
                                                    "text prizes": "prizes:1st place $2000, 2nd place: $1000, 3rd place: $500"
                                                }
                                            ],
                                            "turnamen 2": [
                                                {
                                                    "text": "premium tournament"
                                                },
                                                {
                                                    "img": "foto 2",
                                                    "url": "img/tournament/2.jpg"
                                                },
                                                {
                                                    "text judul": "DOOM"
                                                },
                                                {
                                                    "text beggins": "Tournament Beggins:June 20, 2018"
                                                },
                                                {
                                                    "text ends": "Tounament Ends:July 01, 2018"
                                                },
                                                {
                                                    "text participants": "Participants:10 teams"
                                                },
                                                {
                                                    "text tournament": "Tournament Author:Admin"
                                                },
                                                {
                                                    "text prizes": "prizes:1st place $2000, 2nd place: $1000, 3rd place: $500"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "body 4": [
                                {
                                    "ulasan terbaru": [
                                        {
                                            "text": "new"
                                        },
                                        {
                                            "text": "recent reviews"
                                        },
                                        {
                                            "ulasan 1": [
                                                {
                                                    "img": "foto ulasan 1",
                                                    "url": "img/review/1.jpg"
                                                },
                                                {
                                                    "icon": "icon yellow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "Assasin’’s Creed"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "ulasan 2": [
                                                {
                                                    "img": "foto ulasan 2",
                                                    "text": "img/review/2.jpg"
                                                },
                                                {
                                                    "icon": "icon purple",
                                                    "number": "9.5"
                                                },
                                                {
                                                    "text judul": "Doom"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "ulasan 3": [
                                                {
                                                    "img": "foto ulasan 3",
                                                    "text": "img/review/3.jpg"
                                                },
                                                {
                                                    "icon": "icon green",
                                                    "number": "9.1"
                                                },
                                                {
                                                    "text judul": "Overwatch"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "ulasan 4": [
                                                {
                                                    "img": "foto ulasan 1",
                                                    "text": "img/review/3.jpg"
                                                },
                                                {
                                                    "icon": "icon pink",
                                                    "number": "9.7"
                                                },
                                                {
                                                    "text judul": "GTA"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            "footer": [
                                {
                                    "footer atas": [
                                        {
                                            "logo": "game warrior"
                                        },
                                        {
                                            "text": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                        },
                                        {
                                            "left": [
                                                {
                                                    "text": "Latest Posts"
                                                },
                                                {
                                                    "img 1": "foto 1",
                                                    "url": "img/latest-blog/1.jpg"
                                                },
                                                {
                                                    "text date": "june 21,2018",
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum",
                                                    "text": "by admin"
                                                },
                                                {
                                                    "img 2": "foto 2",
                                                    "url": "img/latest-blog/2.jpg"
                                                },
                                                {
                                                    "text date": "june 21,2018",
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum",
                                                    "text": "by admin"
                                                },
                                                {
                                                    "img 3": "foto 3",
                                                    "url": "img/latest-blog/3.jpg"
                                                },
                                                {
                                                    "text date": "june 21,2018",
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum",
                                                    "text": "by admin"
                                                }
                                            ],
                                            "right": [
                                                {
                                                    "text": "Top Comments"
                                                },
                                                {
                                                    "img": "foto 1",
                                                    "url": "img/authors/1.jpg"
                                                },
                                                {
                                                    "text": "James Smith on  Lorem ipsum dolor sit amet, co",
                                                    "text date": "june 21,2018"
                                                },
                                                {
                                                    "img": "foto 2",
                                                    "url": "img/authors/2.jpg"
                                                },
                                                {
                                                    "text": "James Smith on  Lorem ipsum dolor sit amet, co",
                                                    "text date": "june 21,2018"
                                                },
                                                {
                                                    "img": "foto 3",
                                                    "url": "img/authors/3.jpg"
                                                },
                                                {
                                                    "text": "James Smith on  Lorem ipsum dolor sit amet, co",
                                                    "text date": "june 21,2018"
                                                },
                                                {
                                                    "img": "foto 4",
                                                    "url": "img/authors/4.jpg"
                                                },
                                                {
                                                    "text": "James Smith on  Lorem ipsum dolor sit amet, co",
                                                    "text date": "june 21,2018"
                                                }
                                            ]
                                        }
                                    ],
                                    "footer bawah": [
                                        {
                                            "text 1": "home"
                                        },
                                        {
                                            "text 2": "games"
                                        },
                                        {
                                            "text 3": "blog"
                                        },
                                        {
                                            "text 4": "forums"
                                        },
                                        {
                                            "text 5": "contact"
                                        },
                                        {
                                            "text copyright": "Copyright © 2022 All rights reserved | This template is made with ",
                                            "icon": "heart",
                                            "by": "colorlib"
                                        }

                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_template(Resource):
    def get(self):
        return {
            "data": [
                {
                    "template": [
                        {
                            "template 1": [
                                {
                                    "img": "foto one"
                                },
                                {
                                    "text": "new"
                                },
                                {
                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "3 comments"
                                }
                            ],
                            "template 2": [
                                {
                                    "img": "foto two"
                                },
                                {
                                    "text": "strategy"
                                },
                                {
                                    "text": "justo tempor, rutrum erat id, molestie"
                                },
                                {
                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "3 comments"
                                }
                            ],
                            "template 3": [
                                {
                                    "img": "foto three"
                                },
                                {
                                    "text": "new"
                                },
                                {
                                    "text": "nullam lacinia ex eleifend orci porttitor"
                                },
                                {
                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "3 comments"
                                }
                            ],
                            "template 4": [
                                {
                                    "img": "foto four"
                                },
                                {
                                    "text": "racing"
                                },
                                {
                                    "text": "lacinia ex eleifend orci suscipit"
                                },
                                {
                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "3 comments"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_game(Resource):
    def get(self):
        return {
            "data": [
                {
                    "permainan baru": [
                        {
                            "text": "new"
                        },
                        {
                            "text": "recent games"
                        },
                        {
                            "game 1": [
                                {
                                    "img": "foto 1",
                                    "url": "img/recent-game-bg.png"
                                },
                                {
                                    "text": "new"
                                },
                                {
                                    "text judul": "Suspendisse ut justo tem por, rutrum"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "foto bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "foto love",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ],
                            "game 2": [
                                {
                                    "img 2": "foto 2",
                                    "url": "img/recent-game/2.jpg"
                                },
                                {
                                    "text": "racing"
                                },
                                {
                                    "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "foto bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "foto love",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ],
                            "game 3": [
                                {
                                    "img 3": "foto3",
                                    "url": "img/recent-game/3.jpg"
                                },
                                {
                                    "text": "adventure"
                                },
                                {
                                    "text judul": "Suspendisse ut justo tem por, rutrum"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "foto bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "foto love",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_turnamen(Resource):
    def get(self):
        return {
            "data": [
                {
                    "turnamen": [
                        {
                            "text": "tournaments"
                        },
                        {
                            "turnamen 1": [
                                {
                                    "text": "premium tournament"
                                },
                                {
                                    "img": "foto 1",
                                    "url": "img/tournament/1.jpg"
                                },
                                {
                                    "text judul": "World Of WarCraft"
                                },
                                {
                                    "text beggins": "Tournament Beggins:June 20, 2018"
                                },
                                {
                                    "text ends": "Tounament Ends:July 01, 2018"
                                },
                                {
                                    "text participants": "Participants:10 teams"
                                },
                                {
                                    "text tournament": "Tournament Author:Admin"
                                },
                                {
                                    "text prizes": "prizes:1st place $2000, 2nd place: $1000, 3rd place: $500"
                                }
                            ],
                            "turnamen 2": [
                                {
                                    "text": "premium tournament"
                                },
                                {
                                    "img": "foto 2",
                                    "url": "img/tournament/2.jpg"
                                },
                                {
                                    "text judul": "DOOM"
                                },
                                {
                                    "text beggins": "Tournament Beggins:June 20, 2018"
                                },
                                {
                                    "text ends": "Tounament Ends:July 01, 2018"
                                },
                                {
                                    "text participants": "Participants:10 teams"
                                },
                                {
                                    "text tournament": "Tournament Author:Admin"
                                },
                                {
                                    "text prizes": "prizes:1st place $2000, 2nd place: $1000, 3rd place: $500"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class home_ulasan(Resource):
    def get(self):
        return {
            "data": [
                {
                    "ulasan terbaru": [
                        {
                            "text": "new"
                        },
                        {
                            "text": "recent reviews"
                        },
                        {
                            "ulasan 1": [
                                {
                                    "img": "foto ulasan 1",
                                    "url": "img/review/1.jpg"
                                },
                                {
                                    "icon": "icon yellow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "Assasin’’s Creed"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "ulasan 2": [
                                {
                                    "img": "foto ulasan 2",
                                    "text": "img/review/2.jpg"
                                },
                                {
                                    "icon": "icon purple",
                                    "number": "9.5"
                                },
                                {
                                    "text judul": "Doom"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "ulasan 3": [
                                {
                                    "img": "foto ulasan 3",
                                    "text": "img/review/3.jpg"
                                },
                                {
                                    "icon": "icon green",
                                    "number": "9.1"
                                },
                                {
                                    "text judul": "Overwatch"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "ulasan 4": [
                                {
                                    "img": "foto ulasan 1",
                                    "text": "img/review/3.jpg"
                                },
                                {
                                    "icon": "icon pink",
                                    "number": "9.7"
                                },
                                {
                                    "text judul": "GTA"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Game(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Halaman game": [
                        {
                            "body 1": [
                                {
                                    "slider": [
                                        {
                                            "left":
                                            {
                                                "text": "latest news"
                                            }
                                        },
                                        {
                                            "right": [
                                                {
                                                    "text": "new"
                                                },
                                                {
                                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "strategy"
                                                },
                                                {
                                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "racing"
                                                },
                                                {
                                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                                }
                                            ]
                                        }
                                    ],
                                    "content": [
                                        {
                                            "img": "image background",
                                            "url": "img/page-top-bg/3.jpg"
                                        },
                                        {
                                            "text judul": "game reviews"
                                        },
                                        {
                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum."
                                        }
                                    ]
                                }
                            ],
                            "body 2": [
                                {
                                    "template": [
                                        {
                                            "template 1": [
                                                {
                                                    "img": "background halloween"
                                                },
                                                {
                                                    "icon": "icon yellow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "overwatch halloween"
                                                },
                                                {
                                                    "icon rating": "bintang 1"
                                                },
                                                {
                                                    "icon rating": "bintang 2"
                                                },
                                                {
                                                    "icon rating": "bintang 3"
                                                },
                                                {
                                                    "icon rating": "bintang 4"
                                                },
                                                {
                                                    "icon rating": "bintang 5"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }

                                            ],
                                            "template 2": [
                                                {
                                                    "img": "background grand theft",
                                                    "url": "img/review/6.jpg"
                                                },
                                                {
                                                    "icon": "icon yellow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "grand theft auto"
                                                },
                                                {
                                                    "icon rating": "bintang 1"
                                                },
                                                {
                                                    "icon rating": "bintang 2"
                                                },
                                                {
                                                    "icon rating": "bintang 3"
                                                },
                                                {
                                                    "icon rating": "bintang 4"
                                                },
                                                {
                                                    "icon rating": "bintang 5"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "template 3": [
                                                {
                                                    "img": "background avatar",
                                                    "url": "img/review/7.jpg"
                                                },
                                                {
                                                    "icon": "icon yellow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "avatar"
                                                },
                                                {
                                                    "icon rating": "bintang 1"
                                                },
                                                {
                                                    "icon rating": "bintang 2"
                                                },
                                                {
                                                    "icon rating": "bintang 3"
                                                },
                                                {
                                                    "icon rating": "bintang 4"
                                                },
                                                {
                                                    "icon rating": "bintang 5"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "template 4": [
                                                {
                                                    "img": "background anthem",
                                                    "url": "img/review/8.jpg"
                                                },
                                                {
                                                    "icon": "icon yellow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "anthem"
                                                },
                                                {
                                                    "icon rating": "bintang 1"
                                                },
                                                {
                                                    "icon rating": "bintang 2"
                                                },
                                                {
                                                    "icon rating": "bintang 3"
                                                },
                                                {
                                                    "icon rating": "bintang 4"
                                                },
                                                {
                                                    "icon rating": "bintang 5"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "template 5": [
                                                {
                                                    "img": "background cyberpunk",
                                                    "url": "img/review/9.jpg"
                                                },
                                                {
                                                    "icon": "icon yellow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "cyberpunk 2077"
                                                },
                                                {
                                                    "icon rating": "bintang 1"
                                                },
                                                {
                                                    "icon rating": "bintang 2"
                                                },
                                                {
                                                    "icon rating": "bintang 3"
                                                },
                                                {
                                                    "icon rating": "bintang 4"
                                                },
                                                {
                                                    "icon rating": "bintang 5"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "template 6": [
                                                {
                                                    "img": "background spiderman",
                                                    "url": "img/review/10.jpg"
                                                },
                                                {
                                                    "icon": "icon yellow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "spiderman"
                                                },
                                                {
                                                    "icon rating": "bintang 1"
                                                },
                                                {
                                                    "icon rating": "bintang 2"
                                                },
                                                {
                                                    "icon rating": "bintang 3"
                                                },
                                                {
                                                    "icon rating": "bintang 4"
                                                },
                                                {
                                                    "icon rating": "bintang 5"
                                                },
                                                {
                                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ]
                                        },
                                        {
                                            "button": "load more"
                                        }
                                    ]
                                }
                            ],
                            "body 3": [
                                {
                                    "ulasan baru": [
                                        {
                                            "button": "new"
                                        },
                                        {
                                            "text": "recent reviews"
                                        },
                                        {
                                            "ulasan 1": [
                                                {
                                                    "img": "foto 1",
                                                    "url": "img/review/1.jpg"
                                                },
                                                {
                                                    "icon": "icon yeelow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "assasin's creed"
                                                },
                                                {
                                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "ulasan 2": [
                                                {
                                                    "img": "foto 2",
                                                    "url": "img/review/2.jpg"
                                                },
                                                {
                                                    "icon": "icon yeelow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "Doom"
                                                },
                                                {
                                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "ulasan 3": [
                                                {
                                                    "img": "foto 3",
                                                    "url": "img/review/3.jpg"
                                                },
                                                {
                                                    "icon": "icon yeelow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "overwatch"
                                                },
                                                {
                                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ],
                                            "ulasan 4": [
                                                {
                                                    "img": "foto 4",
                                                    "url": "img/review/4.jpg"
                                                },
                                                {
                                                    "icon": "icon yeelow",
                                                    "number": "9.3"
                                                },
                                                {
                                                    "text judul": "GTA"
                                                },
                                                {
                                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Game_slider(Resource):
    def get(self):
        return {
            "data": [
                {
                    "slider": [
                        {
                            "left":
                            {
                                "text": "latest news"
                            }
                        },
                        {
                            "right": [
                                {
                                    "text": "new"
                                },
                                {
                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "strategy"
                                },
                                {
                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "racing"
                                },
                                {
                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Game_Template(Resource):
    def get(self):
        return {
            "data": [
                {
                    "template": [
                        {
                            "template 1": [
                                {
                                    "img": "background halloween"
                                },
                                {
                                    "icon": "icon yellow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "overwatch halloween"
                                },
                                {
                                    "icon rating": "bintang 1"
                                },
                                {
                                    "icon rating": "bintang 2"
                                },
                                {
                                    "icon rating": "bintang 3"
                                },
                                {
                                    "icon rating": "bintang 4"
                                },
                                {
                                    "icon rating": "bintang 5"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }

                            ],
                            "template 2": [
                                {
                                    "img": "background grand theft",
                                    "url": "img/review/6.jpg"
                                },
                                {
                                    "icon": "icon yellow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "grand theft auto"
                                },
                                {
                                    "icon rating": "bintang 1"
                                },
                                {
                                    "icon rating": "bintang 2"
                                },
                                {
                                    "icon rating": "bintang 3"
                                },
                                {
                                    "icon rating": "bintang 4"
                                },
                                {
                                    "icon rating": "bintang 5"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "template 3": [
                                {
                                    "img": "background avatar",
                                    "url": "img/review/7.jpg"
                                },
                                {
                                    "icon": "icon yellow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "avatar"
                                },
                                {
                                    "icon rating": "bintang 1"
                                },
                                {
                                    "icon rating": "bintang 2"
                                },
                                {
                                    "icon rating": "bintang 3"
                                },
                                {
                                    "icon rating": "bintang 4"
                                },
                                {
                                    "icon rating": "bintang 5"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "template 4": [
                                {
                                    "img": "background anthem",
                                    "url": "img/review/8.jpg"
                                },
                                {
                                    "icon": "icon yellow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "anthem"
                                },
                                {
                                    "icon rating": "bintang 1"
                                },
                                {
                                    "icon rating": "bintang 2"
                                },
                                {
                                    "icon rating": "bintang 3"
                                },
                                {
                                    "icon rating": "bintang 4"
                                },
                                {
                                    "icon rating": "bintang 5"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "template 5": [
                                {
                                    "img": "background cyberpunk",
                                    "url": "img/review/9.jpg"
                                },
                                {
                                    "icon": "icon yellow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "cyberpunk 2077"
                                },
                                {
                                    "icon rating": "bintang 1"
                                },
                                {
                                    "icon rating": "bintang 2"
                                },
                                {
                                    "icon rating": "bintang 3"
                                },
                                {
                                    "icon rating": "bintang 4"
                                },
                                {
                                    "icon rating": "bintang 5"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "template 6": [
                                {
                                    "img": "background spiderman",
                                    "url": "img/review/10.jpg"
                                },
                                {
                                    "icon": "icon yellow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "spiderman"
                                },
                                {
                                    "icon rating": "bintang 1"
                                },
                                {
                                    "icon rating": "bintang 2"
                                },
                                {
                                    "icon rating": "bintang 3"
                                },
                                {
                                    "icon rating": "bintang 4"
                                },
                                {
                                    "icon rating": "bintang 5"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ]
                        },
                        {
                            "button": "load more"
                        }
                    ]
                }
            ]
        }


class Game_review(Resource):
    def get(self):
        return {
            "data": [
                {
                    "ulasan baru": [
                        {
                            "button": "new"
                        },
                        {
                            "text": "recent reviews"
                        },
                        {
                            "ulasan 1": [
                                {
                                    "img": "foto 1",
                                    "url": "img/review/1.jpg"
                                },
                                {
                                    "icon": "icon yeelow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "assasin's creed"
                                },
                                {
                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "ulasan 2": [
                                {
                                    "img": "foto 2",
                                    "url": "img/review/2.jpg"
                                },
                                {
                                    "icon": "icon yeelow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "Doom"
                                },
                                {
                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "ulasan 3": [
                                {
                                    "img": "foto 3",
                                    "url": "img/review/3.jpg"
                                },
                                {
                                    "icon": "icon yeelow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "overwatch"
                                },
                                {
                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ],
                            "ulasan 4": [
                                {
                                    "img": "foto 4",
                                    "url": "img/review/4.jpg"
                                },
                                {
                                    "icon": "icon yeelow",
                                    "number": "9.3"
                                },
                                {
                                    "text judul": "GTA"
                                },
                                {
                                    "tex isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame."
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Blog(Resource):
    def get(self):
        return {
            "data": [
                {
                    "Halaman blog": [
                        {
                            "body 1": [
                                {
                                    "slider": [
                                        {
                                            "left":
                                            {
                                                "text": "latest news"
                                            }
                                        },
                                        {
                                            "right": [
                                                {
                                                    "text": "new"
                                                },
                                                {
                                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "strategy"
                                                },
                                                {
                                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                                },
                                                {
                                                    "text": "racing"
                                                },
                                                {
                                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                                }
                                            ]
                                        }
                                    ],
                                    "content": [
                                        {
                                            "img": "image background",
                                            "url": "img/page-top-bg/3.jpg"
                                        },
                                        {
                                            "text judul": "Video Gallery"
                                        },
                                        {
                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum."
                                        }
                                    ]
                                }
                            ],
                            "body 2": [
                                {
                                    "content": [
                                        {
                                            "bagian game": [
                                                {
                                                    "game 1": [
                                                        {
                                                            "img": "bg 1",
                                                            "url": "img/recent-game/1.jpg"
                                                        },
                                                        {
                                                            "button text": "racing"
                                                        },
                                                        {
                                                            "text judul": "Suspendisse ut justo tem por, rutrum"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "game 2": [
                                                        {
                                                            "img": "bg 2",
                                                            "url": "img/recent-game/2.jpg"
                                                        },
                                                        {
                                                            "button text": "racing"
                                                        },
                                                        {
                                                            "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "game 3": [
                                                        {
                                                            "img": "bg 3",
                                                            "url": "img/recent-game/3.jpg"
                                                        },
                                                        {
                                                            "button text": "adventure"
                                                        },
                                                        {
                                                            "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "game 4": [
                                                        {
                                                            "img": "bg 4",
                                                            "url": "img/recent-game/4.jpg"
                                                        },
                                                        {
                                                            "button text": "racing"
                                                        },
                                                        {
                                                            "text judul": "Suspendisse ut justo tem por, rutrum"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "game 5": [
                                                        {
                                                            "img": "bg 5",
                                                            "url": "img/recent-game/5.jpg"
                                                        },
                                                        {
                                                            "button text": "racing"
                                                        },
                                                        {
                                                            "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "game 6": [
                                                        {
                                                            "img": "bg 6",
                                                            "url": "img/recent-game/6.jpg"
                                                        },
                                                        {
                                                            "button text": "adventure"
                                                        },
                                                        {
                                                            "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "game 7": [
                                                        {
                                                            "img": "bg 7",
                                                            "url": "img/recent-game/7.jpg"
                                                        },
                                                        {
                                                            "button text": "racing"
                                                        },
                                                        {
                                                            "text judul": "Suspendisse ut justo tem por, rutrum"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "game 8": [
                                                        {
                                                            "img": "bg 8",
                                                            "url": "img/recent-game/8.jpg"
                                                        },
                                                        {
                                                            "button text": "racing"
                                                        },
                                                        {
                                                            "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                                        },
                                                        {
                                                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                                        },
                                                        {
                                                            "text": "3 comments"
                                                        },
                                                        {
                                                            "img": "bintang",
                                                            "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                                        },
                                                        {
                                                            "img": "heart",
                                                            "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "button number": "01"
                                                },
                                                {
                                                    "button number": "02"
                                                },
                                                {
                                                    "button number": "03"
                                                }
                                            ]
                                        }
                                    ],
                                    "sidebar": [
                                        {
                                            "button": "search"
                                        },
                                        {
                                            "text": "search"
                                        },
                                        {
                                            "icon": "search"
                                        },
                                        {
                                            "bagian latest post": [
                                                {
                                                    "text": "Latest Posts"
                                                },
                                                {
                                                    "pots 1": [
                                                        {
                                                            "img": "foto 1"
                                                        },
                                                        {
                                                            "date": "june 21, 2018"
                                                        },
                                                        {
                                                            "text isi": "Ipsum dolor sit amet, consectetur adipisc ing consecips"
                                                        },
                                                        {
                                                            "text": "by admin"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "pots 2": [
                                                        {
                                                            "img": "foto 2",
                                                            "url": "img/latest-blog/1.jpg"
                                                        },
                                                        {
                                                            "date": "june 21, 2018"
                                                        },
                                                        {
                                                            "text isi": "Ipsum dolor sit amet, consectetur adipisc ing consecips"
                                                        },
                                                        {
                                                            "text": "by admin"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "pots 3": [
                                                        {
                                                            "img": "foto 3"
                                                        },
                                                        {
                                                            "date": "june 21, 2018"
                                                        },
                                                        {
                                                            "text isi": "Ipsum dolor sit amet, consectetur adipisc ing consecips"
                                                        },
                                                        {
                                                            "text": "by admin"
                                                        }
                                                    ]
                                                }
                                            ],
                                            "bagian top comment": [
                                                {
                                                    "text": "Top Comments"
                                                },
                                                {
                                                    "comment 1": [
                                                        {
                                                            "img1": "foto 1",
                                                            "url": "img/authors/1.jpg",
                                                            "text": "James Smith on Lorem consec ipsum dolor sit amet, co",
                                                            "date": "june 21, 2018"
                                                        },
                                                        {
                                                            "img2": "foto 2",
                                                            "url": "img/authors/2.jpg",
                                                            "text": "Michael James onCras sit amet sapien aliquam",
                                                            "date": "june 21, 2018"
                                                        },
                                                        {
                                                            "img3": "foto 3",
                                                            "url": "img/authors/3.jpg",
                                                            "text": "Justin More on Lorem ipsum dolor consecsit",
                                                            "date": "june 21, 2018"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Blog_slider(Resource):
    def get(self):
        return {
            "data": [
                {
                    "slider": [
                        {
                            "left":
                            {
                                "text": "latest news"
                            }
                        },
                        {
                            "right": [
                                {
                                    "text": "new"
                                },
                                {
                                    "text": "lorem ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "strategy"
                                },
                                {
                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                },
                                {
                                    "text": "racing"
                                },
                                {
                                    "text": "ipsum dolor sit amet,consectetur adipiscing elit"
                                }
                            ]
                        }
                    ],
                    "content": [
                        {
                            "img": "image background",
                            "url": "img/page-top-bg/3.jpg"
                        },
                        {
                            "text judul": "Video Gallery"
                        },
                        {
                            "text isi": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum."
                        }
                    ]
                }
            ]
        }


class Blog_bagian_game(Resource):
    def get(self):
        return {
            "data": [
                {
                    "bagian game": [
                        {
                            "game 1": [
                                {
                                    "img": "bg 1",
                                    "url": "img/recent-game/1.jpg"
                                },
                                {
                                    "button text": "racing"
                                },
                                {
                                    "text judul": "Suspendisse ut justo tem por, rutrum"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        },
                        {
                            "game 2": [
                                {
                                    "img": "bg 2",
                                    "url": "img/recent-game/2.jpg"
                                },
                                {
                                    "button text": "racing"
                                },
                                {
                                    "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        },
                        {
                            "game 3": [
                                {
                                    "img": "bg 3",
                                    "url": "img/recent-game/3.jpg"
                                },
                                {
                                    "button text": "adventure"
                                },
                                {
                                    "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        },
                        {
                            "game 4": [
                                {
                                    "img": "bg 4",
                                    "url": "img/recent-game/4.jpg"
                                },
                                {
                                    "button text": "racing"
                                },
                                {
                                    "text judul": "Suspendisse ut justo tem por, rutrum"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        },
                        {
                            "game 5": [
                                {
                                    "img": "bg 5",
                                    "url": "img/recent-game/5.jpg"
                                },
                                {
                                    "button text": "racing"
                                },
                                {
                                    "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        },
                        {
                            "game 6": [
                                {
                                    "img": "bg 6",
                                    "url": "img/recent-game/6.jpg"
                                },
                                {
                                    "button text": "adventure"
                                },
                                {
                                    "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        },
                        {
                            "game 7": [
                                {
                                    "img": "bg 7",
                                    "url": "img/recent-game/7.jpg"
                                },
                                {
                                    "button text": "racing"
                                },
                                {
                                    "text judul": "Suspendisse ut justo tem por, rutrum"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        },
                        {
                            "game 8": [
                                {
                                    "img": "bg 8",
                                    "url": "img/recent-game/8.jpg"
                                },
                                {
                                    "button text": "racing"
                                },
                                {
                                    "text judul": "Susce pulvinar metus nulla, vel facilisis sem"
                                },
                                {
                                    "text isi": "Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit amet, consectetur elit."
                                },
                                {
                                    "text": "3 comments"
                                },
                                {
                                    "img": "bintang",
                                    "url": "img/icons/xstar.png.pagespeed.ic.yQ0TdmQfU3.webp"
                                },
                                {
                                    "img": "heart",
                                    "url": "img/icons/xheart.png.pagespeed.ic.LNwm9aZI3I.webp"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Blog_sidebar_post(Resource):
    def get(self):
        return {
            "data": [
                {
                    "bagian latest post": [
                        {
                            "text": "Latest Posts"
                        },
                        {
                            "pots 1": [
                                {
                                    "img": "foto 1"
                                },
                                {
                                    "date": "june 21, 2018"
                                },
                                {
                                    "text isi": "Ipsum dolor sit amet, consectetur adipisc ing consecips"
                                },
                                {
                                    "text": "by admin"
                                }
                            ]
                        },
                        {
                            "pots 2": [
                                {
                                    "img": "foto 2",
                                    "url": "img/latest-blog/1.jpg"
                                },
                                {
                                    "date": "june 21, 2018"
                                },
                                {
                                    "text isi": "Ipsum dolor sit amet, consectetur adipisc ing consecips"
                                },
                                {
                                    "text": "by admin"
                                }
                            ]
                        },
                        {
                            "pots 3": [
                                {
                                    "img": "foto 3"
                                },
                                {
                                    "date": "june 21, 2018"
                                },
                                {
                                    "text isi": "Ipsum dolor sit amet, consectetur adipisc ing consecips"
                                },
                                {
                                    "text": "by admin"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class Blog_sidebar_comment(Resource):
    def get(self):
        return {
            "data": [
                {
                    "bagian top comment": [
                        {
                            "text": "Top Comments"
                        },
                        {
                            "comment 1": [
                                {
                                    "img1": "foto 1",
                                            "url": "img/authors/1.jpg",
                                            "text": "James Smith on Lorem consec ipsum dolor sit amet, co",
                                            "date": "june 21, 2018"
                                },
                                {
                                    "img2": "foto 2",
                                            "url": "img/authors/2.jpg",
                                            "text": "Michael James onCras sit amet sapien aliquam",
                                            "date": "june 21, 2018"
                                },
                                {
                                    "img3": "foto 3",
                                            "url": "img/authors/3.jpg",
                                            "text": "Justin More on Lorem ipsum dolor consecsit",
                                            "date": "june 21, 2018"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class forums(Resource):
    def get(self):
        return{
            "data": [
                {
                    "Halaman forums": [
                        {
                            "left":
                            {
                                "text judul": "All Members (344)"
                            }
                        },
                        {
                            "right": [
                                {
                                    "text": "Show"
                                },
                                {
                                    "tombol dropdown": [
                                        {
                                            "tex": "Everything"
                                        },
                                        {
                                            "text": "Everything"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "testimoni": [
                                {
                                    "testimoni 1": [
                                        {
                                            "img": "foto 1",
                                            "url": "img/authors/1.jpg",
                                            "nama": "James Smith",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum."
                                        }
                                    ]
                                },
                                {
                                    "testimoni 2": [
                                        {
                                            "img": "foto 2",
                                            "url": "img/authors/2.jpg",
                                            "nama": "Partik Williams",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum.",
                                            "img2": "foto testimoni"
                                        }
                                    ]
                                },
                                {
                                    "testimoni 3": [
                                        {
                                            "img": "foto 3",
                                            "url": "img/authors/3.jpg",
                                            "nama": "Cris The Man",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum."
                                        }
                                    ]
                                },
                                {
                                    "testimoni 4": [
                                        {
                                            "img": "foto 4",
                                            "url": "img/authors/4.jpg",
                                            "nama": "James Smith",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum."
                                        }
                                    ]
                                },
                                {
                                    "testimoni 5": [
                                        {

                                            "img": "foto 5",
                                            "url": "img/authors/5.jpg",
                                            "nama": "Cris The Man",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum."
                                        }
                                    ]
                                },
                                {
                                    "testimoni 6": [
                                        {
                                            "img": "foto 6",
                                            "url": "img/authors/6.jpg",
                                            "nama": "James Smith",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum."
                                        }
                                    ]
                                },
                                {
                                    "testimoni 7": [
                                        {
                                            "img": "foto 7",
                                            "url": "img/authors/7.jpg",
                                            "nama": "James Smith",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum."
                                        }
                                    ]
                                },
                                {
                                    "testimoni 8": [
                                        {
                                            "img": "foto 8",
                                            "url": "img/authors/8.jpg",
                                            "nama": "Maria Doe",
                                            "update": "posted an update",
                                            "date": "june 21, 2018",
                                            "isi": "Lorem ipsum dolor sit amet, cdictum nisl onsectetur adipisc ing ipsum dolor sit ame. Lorem ipsum dolor sit amet, consectetur adipisc ing ipsum dolor sit ame.Donec venenatis at eros sit amet aliquam. Donec vel orci efficitur, dictum nisl vitae, scelerisque nibh. Curabitur eget ipsum pulvinar nunc gravida interdum."
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }


api.add_resource(Home, '/home/')
api.add_resource(home_template, '/home/template/')
api.add_resource(home_game, '/home/game/')
api.add_resource(home_turnamen, '/home/turnamen/')
api.add_resource(home_ulasan, '/home/ulasan/')
api.add_resource(Game, '/game/')
api.add_resource(Game_slider, '/game/slider/')
api.add_resource(Game_Template, '/game/template/')
api.add_resource(Game_review, '/game/review/')
api.add_resource(Blog, '/blog/')
api.add_resource(Blog_slider, '/blog/slider/')
api.add_resource(Blog_bagian_game, '/blog/bagian_game/')
api.add_resource(Blog_sidebar_post, '/blog/sidebar_post/')
api.add_resource(Blog_sidebar_comment, '/blog/sidebar_comment/')
api.add_resource(forums, '/forums/')


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "not found end point"}, 404


if __name__ == '__main__':
    app.run(debug=True)
