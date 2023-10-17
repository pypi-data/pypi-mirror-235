from graspit.services.DBService.models.dynamic_base import TaskBase
from graspit.services.SchedularService.modifySuites import patchTestSuite
from graspit.services.SchedularService.constants import JobType
from graspit.services.SchedularService.completeTestRun import patchTestRun
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger
from tortoise.expressions import Q
from datetime import datetime


def add_lookup_task(_scheduler: AsyncIOScheduler):
    _scheduler.add_job(
        lookup_for_tasks, id=JobType.LOOKUP_JOB,
        name="clearing up the pending tasks if present", args=(_scheduler,),
        next_run_time=datetime.now(), max_instances=2
    )


async def lookup_for_tasks(_scheduler: AsyncIOScheduler):
    logger.info("Looking up for the tasks")
    task = await TaskBase.filter(
        Q(picked=False) & (Q(type=JobType.MODIFY_SUITE) | Q(type=JobType.MODIFY_TEST_RUN))
    ).order_by("dropped").first()  # ascending

    if not task:
        return logger.warning("No Task found in this iteration")

    await task.update_from_dict(dict(picked=True))
    await task.save()

    match task.type:
        case JobType.MODIFY_SUITE:
            await patchTestSuite(task.ticketID, task.test_id)

        case JobType.MODIFY_TEST_RUN:
            await patchTestRun(task.ticketID, task.test_id)
        case _:
            print("Not Implemented yet..")

    logger.info("Rescheduling for lookup task")
    add_lookup_task(_scheduler)
