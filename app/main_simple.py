from app.config_simple import WELCOME_MSG


def print_welcome_message():
    print(WELCOME_MSG)


def print_incoming_message(msg: str):
    print("Incoming message:", msg)


if __name__ == "__main__":
    print_welcome_message()
    print_incoming_message("Foobar!")
