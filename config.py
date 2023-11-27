import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","25488022"))
API_HASH = getenv("API_HASH","0c999a454fddd79251213be7944811e8")

BOT_TOKEN = getenv("BOT_TOKEN","6657655543:AAH5QN6VhyH63WM1F3JJAIaylw4DZeR186c")

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://vivek123:vivek@cluster0.chvk1tw.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1002042572827"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "vivek's Music")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6815918609").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mrtosumemon/DoReAmOn_MuSiC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/bseb9th")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/bseb9th")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION","BQCCR8PhwK6noxZn6S6izVvSnZsw3Nr52EVrkFwoNvbV9-1dEgWvBB9U3Wo9_-uRxo5MTjsM3oUhWgB49qqs3Q7d0EOaosYbJ2GI8fU907yUwa0OmKs2qr6xuifctwyJ1FgfRFGuU8gSYA6ZNSL_0DbeEbPNuHsHTrENSZh9JdOxhTlL_R0Wp73VqMZ2Qqnh01Pl7GIlyxCGfd8hedqRhImmbdkuIfNWqHLl4s_eBpxL2UYYqFCbgm1ugrVZU1kAIj8ir2LOktQuAtEC_ZhEcS51V7HXnDmexhNPcUuYgucgbmTkW3Mzo_ONNqzX6HHSckm02Uz1xD3IbH-_r-Od5DAAAAAZZCqhEA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/929a2ae1bba42e733aae6.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/e12595049bd2a9fe5cfbb.jpg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

GLOBAL_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

STATS_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

TELEGRAM_VIDEO_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

STREAM_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

SOUNCLOUD_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

YOUTUBE_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://graph.org/file/e12595049bd2a9fe5cfbb.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/929a2ae1bba42e733aae6.jpg"
