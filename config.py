from pyrogram import Client
from Plugin.databesas import *
from Plugin.api import *
import os 

SUDO = 7246248054 # admin or sudo id
CHANNLS_BOT = ['R_O_L_I_X_5'] # bot channls 
API_KEY = '7102991840:AAEAMmGfmRL9uDDBTsdYELCvurOtW3nPpj4'  # API_KEY OR BOT_TOKN 


if not os.path.exists('./.session'):
    os.mkdir('./.session')

if not os.path.exists('./.databesas'):
    os.mkdir('./.databesas')

app = Client(
    '.session/rad',
    bot_token=API_KEY, # API_KEY 
    api_hash='160b2bf653ee7dd974bd6d09a7968cd1', # UserBot api_hahs
    api_id='25829176' # UserBot api_id 
)

datas, apiV = databesas(), TempMailApi()


