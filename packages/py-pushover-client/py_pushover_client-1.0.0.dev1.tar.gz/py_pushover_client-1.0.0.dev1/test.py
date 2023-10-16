from py_pushover_client import PushoverAPIClient

push = PushoverAPIClient(
    api_token="aqej1xh4jvnpmqgvjavi4hh5rv85wz",
    user_key="u78w45hrcc7ragbngzn8ec57quo6ac",
)
push.send("Test", "This is a test message")
