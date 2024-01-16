broker_url = 'redis://localhost:6379/1'

celery_beat_schedule = {
    'clear_expired_tokens': {
        'task': 'auth_two.tasks.clear_expired_tokens',
        'schedule': 5
    },
}

broker_connection_max_retries = 10

broker_connection_retry_on_startup = True
