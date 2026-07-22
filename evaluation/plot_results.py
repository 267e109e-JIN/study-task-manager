from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "benchmark_results.csv"
OUTPUT_FILE = BASE_DIR / "benchmark_results.pdf"

EXPECTED_METHODS = [
    "Manual",
    "Study Task Manager",
]


def load_results() -> pd.DataFrame:
    """Load and validate benchmark results."""
    results = pd.read_csv(DATA_FILE)

    required_columns = {
        "method",
        "trial",
        "time_seconds",
    }

    if not required_columns.issubset(results.columns):
        raise ValueError(
            "The CSV file must contain method, trial, "
            "and time_seconds columns."
        )

    results["time_seconds"] = pd.to_numeric(
        results["time_seconds"],
        errors="coerce",
    )

    if results["time_seconds"].isna().any():
        raise ValueError(
            "Please fill in all time_seconds values "
            "before creating the chart."
        )

    if (results["time_seconds"] <= 0).any():
        raise ValueError(
            "All measured times must be greater than zero."
        )

    methods = set(results["method"])

    if methods != set(EXPECTED_METHODS):
        raise ValueError(
            "The method column must contain only "
            "'Manual' and 'Study Task Manager'."
        )

    return results


def create_chart(results: pd.DataFrame) -> None:
    """Create a vector PDF chart from benchmark results."""
    summary = (
        results.groupby("method")["time_seconds"]
        .agg(["mean", "std"])
        .reindex(EXPECTED_METHODS)
    )

    means = summary["mean"]
    errors = summary["std"].fillna(0)

    figure, axis = plt.subplots(figsize=(6.4, 4.2))

    bars = axis.bar(
        EXPECTED_METHODS,
        means,
        yerr=errors,
        capsize=6,
    )

    for position, method in enumerate(EXPECTED_METHODS):
        trial_values = results.loc[
            results["method"] == method,
            "time_seconds",
        ]

        axis.scatter(
            [position] * len(trial_values),
            trial_values,
            zorder=3,
        )

    for bar, mean_value in zip(bars, means):
        axis.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{mean_value:.1f} s",
            ha="center",
            va="bottom",
        )

    manual_mean = means["Manual"]
    software_mean = means["Study Task Manager"]

    reduction_rate = (
        (manual_mean - software_mean)
        / manual_mean
        * 100
    )

    axis.set_title("Task Management Time Comparison")
    axis.set_ylabel("Average time (seconds)")
    axis.set_xlabel("Method")
    axis.grid(axis="y", linestyle="--", alpha=0.4)

    figure.text(
        0.5,
        0.01,
        f"Time reduction: {reduction_rate:.1f}%",
        ha="center",
    )

    figure.tight_layout(rect=[0, 0.05, 1, 1])
    figure.savefig(
        OUTPUT_FILE,
        format="pdf",
        bbox_inches="tight",
    )

    print("Benchmark summary:")
    print(summary.round(2))
    print()
    print(f"Time reduction: {reduction_rate:.1f}%")
    print(f"Chart saved to: {OUTPUT_FILE}")


def main() -> None:
    """Generate the benchmark chart."""
    results = load_results()
    create_chart(results)


if __name__ == "__main__":
    main()