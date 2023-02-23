import json
import steam.webapi as steam_api
import pprint

with open(r"apikey.json") as f:
    api_userid = json.load(f)

api_key = api_userid["steam_api_key"]
user_id = api_userid["user_id"]

api = steam_api.WebAPI(key=api_key)


def get_library(api, user_id: str) -> list:
    """
    Query's steams web api and returns a list of all games tied to a user id as a list of dictionaries.
    :param api: steamapi object
    :param user_id: user id from s://steamcommunity.com/profiles/{USER_ID}/
    :type: str
    :return: list of all game dictionaries
    :type: list
    """
    response = api.IPlayerService.GetOwnedGames(steamid=user_id,
                                                include_appinfo=True,
                                                include_played_free_games=True,
                                                appids_filter=False,
                                                include_free_sub=True,
                                                language='english',
                                                include_extended_appinfo=False)

    # pprint.pprint(response)
    user_library = response["response"]["games"]
    return user_library


user_library = get_library(api, user_id)

pprint.pprint(user_library)
print("done")
