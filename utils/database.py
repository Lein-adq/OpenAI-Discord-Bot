from pymongo import MongoClient

client = None
db = None


def initialize_database(mongo_connection_string):
    global client
    global db
    client = MongoClient(mongo_connection_string)
    db = client["DiscordBot"]


async def change_channel_model(channel_id, model):
    db.channels.update_one(
        {"channel_id": channel_id},
        {"$set": {"settings.openai_api_model": model}},
        upsert=True,
    )


async def get_tokens_used(user_id):
    user_doc = db.users.find_one({"user_id": user_id})
    return user_doc["settings"]["tokens"] if user_doc else 0


async def update_tokens_used(user_id, tokens):
    db.users.update_one(
        {"user_id": user_id}, {"$inc": {"settings.tokens": tokens}}, upsert=True
    )


async def get_model_for_channel(channel_id):
    channel_doc = db.channels.find_one({"channel_id": channel_id})
    return (
        channel_doc["settings"]["openai_api_model"]
        if channel_doc
        else "text-davinci-002"
    )
