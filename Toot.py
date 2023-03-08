import os
from mastodon import Mastodon
from dotenv import load_dotenv
import asyncio

load_dotenv()

masto = Mastodon(
    access_token = os.getenv("TOKEN"),
    api_base_url = "https://masto.es"
)

async def post_video(mje,media):
    with open(f'{media}', 'rb') as video_file:
        video_bytes = video_file.read()
    media_dict = masto.media_post(media_file=video_bytes, mime_type='video/mp4')
    media_id = media_dict['id']
    await asyncio.sleep(5) # espera 10 segundos antes de publicar
    await masto.status_post(status=f'{mje}', media_ids=[media_id], sensitive=False, visibility='public')

asyncio.run(post_video())