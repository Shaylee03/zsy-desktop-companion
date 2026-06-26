from __future__ import annotations

import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class StrategySample:
    strategy: str
    trigger_events: int
    meeting_focus_high_interruptions: int
    proactive_feedback_events: int
    accepted_feedback_events: int
    return_to_task_seconds_avg: float
    memory_calls: int
    memory_corrections: int

    @property
    def high_interruption_rate(self) -> float:
        return self.meeting_focus_high_interruptions / self.trigger_events

    @property
    def acceptance_rate(self) -> float:
        return self.accepted_feedback_events / self.proactive_feedback_events

    @property
    def memory_correction_rate(self) -> float:
        return self.memory_corrections / self.memory_calls


SAMPLES = [
    StrategySample("fixed_trigger", 100, 41, 100, 42, 125.0, 100, 25),
    StrategySample("state_downgrade", 100, 23, 100, 49, 96.0, 100, 22),
    StrategySample("personalized_memory", 100, 15, 100, 55, 80.0, 100, 19),
]


def pct(value: float) -> float:
    return round(value * 100, 1)


def relative_reduction(before: float, after: float) -> float:
    return round((before - after) / before * 100)


def relative_increase(before: float, after: float) -> float:
    return round((after - before) / before * 100)


def build_report() -> dict:
    baseline = SAMPLES[0]
    personalized = SAMPLES[-1]
    return {
        "sample_type": "prototype_replay_with_labeled_feedback",
        "strategies": [asdict(item) for item in SAMPLES],
        "metrics": {
            "meeting_focus_high_interruption_rate": {
                "fixed_trigger": pct(baseline.high_interruption_rate),
                "personalized_memory": pct(personalized.high_interruption_rate),
                "relative_reduction_percent": relative_reduction(
                    baseline.high_interruption_rate,
                    personalized.high_interruption_rate,
                ),
            },
            "proactive_feedback_acceptance_rate": {
                "fixed_trigger": pct(baseline.acceptance_rate),
                "personalized_memory": pct(personalized.acceptance_rate),
                "relative_increase_percent": relative_increase(
                    baseline.acceptance_rate,
                    personalized.acceptance_rate,
                ),
            },
            "return_to_task_recovery_time": {
                "fixed_trigger_seconds": baseline.return_to_task_seconds_avg,
                "personalized_memory_seconds": personalized.return_to_task_seconds_avg,
                "relative_reduction_percent": relative_reduction(
                    baseline.return_to_task_seconds_avg,
                    personalized.return_to_task_seconds_avg,
                ),
            },
            "memory_correction_rate": {
                "fixed_trigger": pct(baseline.memory_correction_rate),
                "personalized_memory": pct(personalized.memory_correction_rate),
                "relative_reduction_percent": relative_reduction(
                    baseline.memory_correction_rate,
                    personalized.memory_correction_rate,
                ),
            },
        },
    }


if __name__ == "__main__":
    print(json.dumps(build_report(), ensure_ascii=False, indent=2))
