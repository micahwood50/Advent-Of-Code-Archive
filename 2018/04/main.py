from enum import Enum, auto
from collections import defaultdict, Counter
import re


FILENAME = "input.txt"
GUARD_ID_PLACEHOLD = -1


class ActivityType(Enum):
    BEGIN_SHIFT = auto()
    SLEEP = auto()
    WAKE = auto()


class Record:
    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        guard_id: int,
        activity_type: ActivityType,
    ):
        self.guard_id = guard_id
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.activity_type = activity_type

    def __str__(self) -> str:
        return f"[{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}]; ID = {self.guard_id}, activity = {self.activity_type}"

    def __repr__(self) -> str:
        return f"Record({self.year}, {self.month}, {self.day}, {self.hour}, {self.minute}, {self.guard_id}, {self.activity_type})"

    def __eq__(self, other) -> bool:
        return (
            self.year == other.year
            and self.month == other.month
            and self.day == other.day
            and self.hour == other.hour
            and self.minute == other.minute
            and self.activity_type == other.activity_type,
        )

    def __lt__(self, other) -> bool:
        return (
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.activity_type.value,
        ) < (
            other.year,
            other.month,
            other.day,
            other.hour,
            other.minute,
            other.activity_type.value,
        )


def get_input() -> list[Record]:
    record_list: list[Record] = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            result = re.search(r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] \S+ #?(\d+)?", line)

            group_captures = result.groups(default=GUARD_ID_PLACEHOLD)
            group_captures = tuple(map(int, group_captures))

            activity_ch = line[19]  # first character after timestamp

            if activity_ch == "w":
                this_activity = ActivityType.WAKE

            elif activity_ch == "f":
                this_activity = ActivityType.SLEEP

            else:
                this_activity = ActivityType.BEGIN_SHIFT

            record_list.append(Record(*group_captures, this_activity))

    record_list.sort()

    current_guard_id = GUARD_ID_PLACEHOLD

    for record in record_list:
        if record.guard_id != GUARD_ID_PLACEHOLD:
            current_guard_id = record.guard_id
        else:
            record.guard_id = current_guard_id

    return record_list


def part_1():
    records = get_input()
    sleep_dict = defaultdict(int)
    sleep_freq_dict = defaultdict(list)
    current_guard_id = GUARD_ID_PLACEHOLD
    sleep_minute = 0

    for record in records:
        if record.activity_type == ActivityType.BEGIN_SHIFT:
            current_guard_id = record.guard_id
            sleep_minute = 0

        elif record.activity_type == ActivityType.SLEEP:
            sleep_minute = record.minute

        else:
            sleep_dict[current_guard_id] += record.minute - sleep_minute + 1
            sleep_freq_dict[current_guard_id].extend(
                list(range(sleep_minute, record.minute + 1))
            )

    target_guard_id = GUARD_ID_PLACEHOLD
    sleep_max_value = 0

    for k, v in sleep_dict.items():
        if v > sleep_max_value:
            sleep_max_value = v
            target_guard_id = k

    result = (
        target_guard_id * Counter(sleep_freq_dict[target_guard_id]).most_common(1)[0][0]
    )

    print(f"Answer is {result}")


def part_2():
    records = get_input()
    sleep_freq_dict = defaultdict(list)
    current_guard_id = GUARD_ID_PLACEHOLD
    sleep_minute = 0

    for record in records:
        if record.activity_type == ActivityType.BEGIN_SHIFT:
            current_guard_id = record.guard_id
            sleep_minute = 0

        elif record.activity_type == ActivityType.SLEEP:
            sleep_minute = record.minute

        else:
            sleep_freq_dict[current_guard_id].extend(
                list(range(sleep_minute, record.minute + 1))
            )

    max_freq = 0
    target_guard_id = GUARD_ID_PLACEHOLD

    for guard_id, sleep_minute_list in sleep_freq_dict.items():
        sleep_highest_freq = Counter(sleep_minute_list).most_common(1)[0][1]
        if sleep_highest_freq > max_freq:
            max_freq = sleep_highest_freq
            target_guard_id = guard_id

    result = (
        target_guard_id * Counter(sleep_freq_dict[target_guard_id]).most_common(1)[0][0]
    )

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
