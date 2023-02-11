import os


def get_base_url():

    #env = os.environ.get('ENV', None)
    env = os.environ.get('ENV', 'test')  # telling if none of the environment is set and simply run the test in test environment

    if env.lower() == 'test':
        return 'http://demostore.supersqa.com'
        #return 'http://localhost:10003/shop/'
    elif env.lower() == 'prod':
        return 'http://demostore.prod.supersqa.com'
    elif env.lower() == 'testw':
        return 'http://demostore.supersqa.com'
    else:
        raise Exception(f"Unknown environment: {env}")

