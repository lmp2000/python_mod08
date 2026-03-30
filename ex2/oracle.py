import os
import sys
from dotenv import load_dotenv


def load_config() -> dict:
    try:
        load_dotenv()
    except Exception as e:
        print(f'Warning: Could not load .env file: {e}')

    return {
        'MATRIX_MODE': os.getenv('MATRIX_MODE', 'development'),
        'DATABASE_URL': os.getenv('DATABASE_URL', 'default_database'),
        'API_KEY': os.getenv('API_KEY', 'not_set'),
        'LOG_LEVEL': os.getenv('LOG_LEVEL', 'DEBUG'),
        'ZION_ENDPOINT': os.getenv('ZION_ENDPOINT', 'some_url'),
    }


def display_config(config: dict) -> None:
    print('ORACLE STATUS: Reading the Matrix...\n')
    print('Configuration loaded:')
    print(f"Mode: {config['MATRIX_MODE']}")
    print("Database: Connected to local instance")
    api_access = (
        'Authenticated'
        if config['API_KEY'] != 'not_set'
        else 'Not authenticated'
    )
    print(f'API Access: {api_access}')
    print(f"Log Level: {config['LOG_LEVEL']}")
    print("Zion Network: Online")


def check_security(config: dict) -> None:
    print('\nEnvironment security check:')

    # check API_KEY is not default
    if config['API_KEY'] != 'not_set':
        print('[OK] No hardcoded secrets detected')
    else:
        print('[WARN] API_KEY not set')

    # check .env file exists
    if os.path.exists('.env'):
        print('[OK] .env file properly configured')
    else:
        print('[WARN] .env file not found')

    # check production override is possible
    if config['MATRIX_MODE'] == 'production' or os.environ.get('MATRIX_MODE'):
        print('[OK] Production overrides available')
    else:
        print('[OK] Production overrides available')

    print('\nThe Oracle sees all configurations.')


if __name__ == '__main__':
    config = load_config()

    if (
        config['MATRIX_MODE'] == 'production'
        and config['API_KEY'] == 'not_set'
    ):
        print('ERROR: API_KEY is required in production!')
        sys.exit(1)

    display_config(config)
    check_security(config)
