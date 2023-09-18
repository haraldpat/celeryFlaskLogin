from src.apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login",views.login,["POST"],"login url")
]

other_urls = [
    ("/task_status/",views.get_status,["GET"],"GEt the status of the celery"),
    ("/task_result/",views.task_result,["GET"],"See the final result of the task")
]

all_urls = api_urls + other_urls