import os


def get_database_uri(database_type: str) -> str:
    env = os.getenv("ENV")
    database_uri = os.getenv(env + "_" + database_type + "_URI")
    return database_uri
