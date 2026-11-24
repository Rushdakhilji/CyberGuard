
import json
from pathlib import Path


def display_report(report_file):

    try:
        with open(report_file, "r", encoding="utf-8") as file:
            report_data = json.load(file)

        print("\n" + "=" * 50)
        print("             CYBERGUARD SECURITY REPORT")
        print("=" * 50)

        print(f"\nProject: {report_data.get('project', 'N/A')}")
        print(f"Report Type: {report_data.get('report_type', 'N/A')}")
        print(f"File: {report_file.name}")

        print("\nTools Used:")
        for tool in report_data.get("tools_used", []):
            print(f"  - {tool}")

        print("\nSecurity Results:")

        results = report_data.get("results", {})

        if not results:
            print("  No results available.")
        else:
            for tool_name, result in results.items():
                print(f"\n  {tool_name.replace('_', ' ').title()}")
                print(json.dumps(result, indent=4))

        print("\n" + "=" * 50)

    except (OSError, json.JSONDecodeError) as error:
        print(f"\nUnable to read security report: {error}")


def get_report_files():

    reports_folder = Path(__file__).resolve().parent.parent / "reports"

    report_files = list(reports_folder.glob("security_report_*.json"))

    return sorted(
        report_files,
        key=lambda file: file.stat().st_mtime,
        reverse=True
    )


def view_latest_report():

    report_files = get_report_files()

    if not report_files:
        print("\nNo security reports found.")
        return

    display_report(report_files[0])


def view_report_history():

    report_files = get_report_files()

    if not report_files:
        print("\nNo security reports found.")
        return

    print("\n" + "=" * 50)
    print("             SECURITY REPORT HISTORY")
    print("=" * 50)

    for index, report in enumerate(report_files, start=1):
        print(f"{index}. {report.name}")

    print("\n0. Back to Main Menu")

    choice = input("\nSelect a report number: ").strip()

    if choice == "0":
        return

    if not choice.isdigit() or not (1 <= int(choice) <= len(report_files)):
        print("\nInvalid selection. Please choose a valid report number.")
        return

    selected_report = report_files[int(choice) - 1]

    display_report(selected_report)
