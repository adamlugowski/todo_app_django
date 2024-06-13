from faker import Faker
from .models import Task
from random import randint


def create_task(n: int):
    """
    This function creates random and fake tasks
    :param n: Number of fake tasks
    :return: Tasks
    """
    fake = Faker()
    for _ in range(n):
        task = Task.objects.create(
            title=fake.text(randint(5, 50)),
            content=fake.text(randint(5, 100)),
            is_done=fake.boolean(),
            created_at=fake.date_time(),
            modified=fake.date_time()
        )
        task.save()
