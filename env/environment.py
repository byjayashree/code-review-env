import random
from env.tasks import TASKS
from env.grader import grade

class CodeReviewEnv:

    def __init__(self, task_type="easy"):
        self.task_type = task_type
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(TASKS[self.task_type])
        return {"code": self.current_task["code"]}

    def step(self, action):
        score = grade(action, self.current_task)
        done = True
        return {"code": self.current_task["code"]}, score, done, {}

    def state(self):
        return self.current_task