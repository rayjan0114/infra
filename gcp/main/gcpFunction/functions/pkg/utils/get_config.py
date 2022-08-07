from argparse import Namespace
import os
from loguru import logger


def get_config():
    cfg = Namespace()
    cfg.BUCKET_IMAGE_PATH = "pkg-image"
    cfg.BUCKET_URL = "https://storage.googleapis.com"
    cfg.IMAGE_W = 120
    cfg.IMAGE_H = 120
    cfg.BASIC_INFO_DEFAULT = {
        "role": ["UI/UX Designer", "Graphic Designer", "Market Branding", "Front-end Developer", "Back-end Developer", "iOS Developer", "Android Developer"],
        "seniority": ["0-1 year", "1-2 years", "3-5 years", "6-10 years", "11-20 years", "20+ years"],
        "uiUxDesigner": ["Ul", "UX", "Wireframing", "Prototyping", "User Research", "Sketch", "Figma", "Adobe XD"],
        "availability": [
            "1-4 hours / week",
            "4-8 hours / week",
            "8-12 hours / week",
            "12-20 hours / week",
            "20-32 hours / week",
            "32+ hours / week",
        ],
        "links": {
            # What links to put:
            # 1. Get list from 'default' key. Adopted by all type of Role
            # 2. Get list from last word of role.
            #    i.e. Chose "UI/UX Designer" as Role. -> Get the last word which is "designer".
            # In conclusion,
            #    -"UI/UX Designer", "Graphic Designer" should list out links of 'LinkedIn',, 'Behance', 'Dribble'
            #    -"Front-end Developer", "Back-end Developer", and others suffix with "developer" should list out links of 'LinkedIn',, 'Portfolio', 'Resume'
            # .   -"Market Branding" or other that might be added in the future should list out 'LinkedIn'
            "default": [
                "LinkedIn",
                "Resume",
            ],
            "designer": [
                "Behance",
                "Dribble",
            ],
            "developer": [
                "Portfolio",
                "Github",
            ],
        },
        "location": ["台灣北部", "台灣中部", "台灣南部", "台灣東部", "台灣離島", "海外亞洲", "海外歐洲", "海外美洲", "海外非洲", "海外大洋洲"],
    }
    return cfg
