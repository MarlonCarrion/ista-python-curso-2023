from dotenv import load_dotenv, dotenv_values

env = 'development'


def get_config():
    configuration = {}
    if env == 'development':
        configuration = dotenv_values('.env.development')
    if env == 'production':
        configuration = dotenv_values('.env.production')
    return configuration
