from src.core.configs import settings


broker_url = settings.REDIS_URL
backend_url = settings.REDIS_URL
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Moscow'
enable_utc = True

