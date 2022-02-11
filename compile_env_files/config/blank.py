config = """
{
  "consumers": {
    "django": "env/django.env",
    "postgres": "env/postgres.env",
    "vite": [
      "env/vite.env",
      "frontend/vite-project/.env",
    ]
  },
  "variables": {
    "db-name": {
      "value": "my_project_db,
      "consumers": {
        "django": "DB_NAME",
        "postgres": "POSTGRES_DB"
      }
    },
    "username-maxlength": {
      "value": 180,
      "consumers": {
        "django": "USER_MODEL_NAME_MAXLENGTH",
        "vite": "USER_AUTH_FORM_NAME_MAXLENGTH"
      }
    },
    "redis-task-queue-url": {
      "value": "redis://redis:6789/0",
      "consumers": {
        "django": [
          "CELERY_BROKER",
          "CELERY_BACKEND",
          "CACHE_URL"
        ]
      }
    }
  }
}
"""