import os

import giphypop
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("giphy_token")


def rng_gif():
    g = giphypop.Giphy(api_key=API_KEY)
    gif = g.screensaver()
    return gif
