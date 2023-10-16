# py-pushover-client
Python package to send notifications to devices using the Pushover Message API.

## Pre-Requisites
Sign up to https://pushover.net and generate a User Key and an API Token.

## Usage
1. Install the package from PyPi:

    ```shell
    pip install py-pushover-client
    ```

2. Add it to your scripts using your own API Token and User Key:

    *The following code snippet is instructional only! You should not hardcode your API Token and User Key as string literals, instead you should consider more secure options such as environment variables.*

    ```python
    from py_pushover_client import PushoverAPIClient

    pushover = PushoverAPIClient(
        api_token="api_token",
        user_key="user_key",
    )

    pushover.send(title="Test", message="This is a test message")
    ```

3. Optionally, you can change the notification sound. This must be done before calling the `PushoverAPIClient.send()` method in order for the sound to be processed.

    A list of acceptable sound options can be found at https://pushover.net/api#sounds

    ```python
    pushover.set_sound(sound="bugle")

    pushover.send(title="Bugle Baby!", message="Stuff happened.")
    ```
