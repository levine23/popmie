from pyrogram import Client
from pytgcalls import PyTgCalls

from config import SESSION_NAME, API_ID, API_HASH
from . import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(client)

stream_status = {}  # Dictionary untuk melacak status aliran

async def play_stream(chat_id, file_path):
    try:
        stream_status[chat_id] = True  # Tandai aliran sebagai sedang diputar
        await pytgcalls.play(chat_id, file_path)
    except Exception as e:
        print(f"Error playing stream: {e}")
        stream_status[chat_id] = False  # Tandai aliran sebagai selesai
        handle_stream_end(chat_id)  # Tangani akhir aliran

async def handle_stream_end(chat_id):
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        next_file = queues.get(chat_id)["file"]
        await play_stream(chat_id, next_file) # play stream selanjutnya.

# Contoh pemanggilan fungsi play_stream
# await play_stream(chat_id, file_path)

run = pytgcalls.run
