from src.core.configs import settings


broker_url = settings.REDIS_URL
# broker_url = 'redis://redis:6379/0'
# broker_url = 'redis://localhost:6379/0'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Moscow'
enable_utc = True

