import requests


class PushoverAPIClient:
    """This is a simple API client for Pushover.

    It allows you to send messages to your devices."""

    URL = "https://api.pushover.net/1/messages.json"
    SOUNDS = [
        "pushover",
        "bike",
        "bugle",
        "cashregister",
        "classical",
        "cosmic",
        "falling",
        "gamelan",
        "incoming",
        "intermission",
        "magic",
        "mechanical",
        "pianobar",
        "siren",
        "spacealarm",
        "tugboat",
        "alien",
        "climb",
        "persistent",
        "echo",
        "updown",
        "vibrate",
        "none",
    ]

    sound = "pushover"

    def __init__(self, api_token: str, user_key: str) -> None:
        self.token = api_token
        self.user_key = user_key

    def set_sound(self, sound: str):
        """Set the sound for the message.
        The sound must be from the list of sounds found at
        https://pushover.net/api#sounds"""

        if sound in self.SOUNDS:
            self.sound = sound

    def send(self, title: str, message: str):
        """Send a message to the user's device/s."""
        requests.post(
            self.URL,
            data={
                "token": self.token,
                "user": self.user_key,
                "title": title,
                "message": message,
                "sound": self.sound,
            },
        )
