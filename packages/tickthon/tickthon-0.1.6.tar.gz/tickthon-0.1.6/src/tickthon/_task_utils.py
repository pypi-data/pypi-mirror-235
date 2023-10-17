import re
from datetime import datetime
from typing import List, Optional
from dateutil import parser, tz

from . import ExpenseLog
from .data.ticktick_task_parameters import TicktickTaskParameters as ttp
from .task_model import Task


def _clean_habit_checkins(checkins: List[dict]) -> List[str]:
    """Returns a list of formatted dates from successful habit checkins.

        Args:
            checkins (List[dict]): A list of checkin dictionaries with "checkinStamp" and "status".

        Returns:
            List[str]: A list of strings representing dates of successful checkins ('YYYY-MM-DD').
                       Returns an empty list if no successful checkins are found.

        Example:
            >>> _clean_habit_checkins([{"checkinStamp": "20230925", "status": 2}])
            ['2023-09-25']
    """
    if not checkins:
        return []

    def parse_date(date: str) -> str:
        return datetime.strptime(str(date), '%Y%m%d').strftime('%Y-%m-%d')

    return [parse_date(checkin["checkinStamp"]) for checkin in checkins if checkin["status"] == 2]


def _is_task_a_weight_measurement(task: Task, weight_measurement_id: Optional[str]) -> bool:
    """Checks if a task is a weight measurement."""
    if weight_measurement_id is None:
        return False
    return task.project_id == weight_measurement_id


def _is_task_an_idea(task: Task) -> bool:
    """Checks if a task is an idea."""
    return task.title.startswith("Idea:")


def _is_task_an_expense_log(task: Task) -> bool:
    """Checks if a task is an expense log."""
    return task.title.startswith("$")


def _is_task_active(task: Task) -> bool:
    """Checks if a task is active."""
    return task.status == 0 and task.deleted == 0


def _is_task_completed(task: Task) -> bool:
    """Checks if a task is completed."""
    return task.status == 2


def _is_task_abandoned(task: Task) -> bool:
    """Checks if a task is abandoned."""
    return task.status == -1


def _is_task_deleted(task: Task) -> bool:
    """Checks if a task is deleted."""
    return task.deleted == 1


def dict_to_task(raw_task: dict) -> Task:
    """Converts a raw task to a Task object.

    Args:
        raw_task: The raw task as dictionary.

    Returns:
        A Task object.
    """
    return Task(ticktick_id=raw_task[ttp.ID.value],
                ticktick_etag=raw_task[ttp.ETAG.value],
                created_date=_get_task_date(raw_task[ttp.TIMEZONE.value], raw_task.get(ttp.CREATED_TIME.value, None)),
                status=raw_task[ttp.STATUS.value],
                title=raw_task[ttp.TITLE.value].strip(),
                focus_time=_get_focus_time(raw_task),
                deleted=raw_task.get(ttp.DELETED.value, 0),
                tags=tuple(raw_task.get(ttp.TAGS.value, ())),
                project_id=raw_task[ttp.PROJECT_ID.value],
                timezone=raw_task[ttp.TIMEZONE.value],
                due_date=_get_task_date(raw_task[ttp.TIMEZONE.value], raw_task.get(ttp.START_DATE.value, None)),
                )


def _get_focus_time(raw_task: dict) -> float:
    """Returns the focus time of a task.

    Args:
        raw_task: The raw task from Ticktick.

    Returns:
        The focus time of the task.
    """
    focus_time = 0.0
    if ttp.FOCUS_SUMMARIES.value in raw_task:
        raw_focus_time = map(lambda summary: summary[ttp.POMO_DURATION.value] + summary[ttp.STOPWATCH_DURATION.value],
                             raw_task[ttp.FOCUS_SUMMARIES.value])
        focus_time = round(sum(raw_focus_time) / 3600, 2)
    elif ttp.FOCUS_TIME.value in raw_task:
        focus_time = float(raw_task[ttp.FOCUS_TIME.value])

    return focus_time


def _get_task_date(raw_task_timezone: str, task_start_date: str) -> str:
    """Returns the date of a task taking into account the timezone.

    Args:
        raw_task_timezone: The timezone of the task.
        task_start_date: The start date of the task.

    Returns:
        Task's date in the format YYYY-MM-DD, if the task has no start date, returns an empty string.
    """
    if not task_start_date:
        return ""

    task_timezone = tz.gettz(raw_task_timezone)
    task_raw_date = parser.parse(task_start_date)

    localized_task_date = task_raw_date.astimezone(task_timezone)
    task_date = localized_task_date.strftime("%Y-%m-%d")

    return task_date


def _parse_expense_log(raw_expense_logs: Task) -> Optional[ExpenseLog]:
    """Parses raw expense logs from Ticktick into ExpenseLog objects.

    Args:
        raw_expense_logs: Raw expense logs from Ticktick.

    Returns:
        Parsed expense logs.
    """
    expense_parse = re.search(r"\$([\d\.]+)\s+(.+)", raw_expense_logs.title)
    if not expense_parse:
        return None

    date = raw_expense_logs.due_date
    if not date:
        date = datetime.now(tz.gettz(raw_expense_logs.timezone)).strftime("%Y-%m-%d")

    return ExpenseLog(date=date,
                      expense=float(expense_parse.group(1)),
                      product=expense_parse.group(2))
