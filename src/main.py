from datetime import datetime, timezone


def main() -> None:
    print("internet-outage-monitoring-attribution initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
