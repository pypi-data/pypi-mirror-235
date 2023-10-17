from dateutil import parser


def get_tweet_id_from_url(url: str) -> str:
    """
    Extracts the tweet ID from a tweet URL.
    :param url: The tweet URL.
    :return: The tweet ID.
    :raises ValueError: If the tweet URL is not correct.
    :raises TypeError: If the tweet URL is not a string.
    """

    if not url:
        raise ValueError("url cannot be empty.")

    if isinstance(url, str) == False:
        raise TypeError("url must be a string.")

    # Remove anything after ?.
    url = url.split("?")[0]

    # IF URL ends with /, remove it.
    if url[-1] == "/":
        url = url[:-1]

    # Split URL AT each /.
    url = url.split("/")

    # Last item in the list is the Tweet ID.
    id = url[-1]
    if not id.isnumeric():
        raise ValueError("Tweet URL is not correct.")
    return id


def extract_user_data_from_object(user_object: dict) -> dict:
    """
    Extracts user data from a user object.
    :param user_object: The user object.
    :return: The extracted user data.
    :rtype: dict
    """

    user = {}
    user["id"] = user_object["rest_id"]
    user["name"] = user_object["legacy"]["name"]
    user["screen_name"] = user_object["legacy"]["screen_name"]

    user["img"] = user_object["legacy"]["profile_image_url_https"]
    user["banner"] = user_object["legacy"]["profile_banner_url"]
    user["description"] = user_object["legacy"]["description"]
    user["location"] = user_object["legacy"]["location"]

    user["favourites_count"] = user_object["legacy"]["favourites_count"]
    user["followers_count"] = user_object["legacy"]["followers_count"]
    user["friends_count"] = user_object["legacy"]["friends_count"]

    user["tweets_count"] = user_object["legacy"]["statuses_count"]

    user["account_age"] = user_object["legacy"]["created_at"]
    if user["account_age"] is not None:
        user["account_age"] = parser.parse(user["account_age"])

    return user
