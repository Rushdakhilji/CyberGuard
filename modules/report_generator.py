
import json
import os
from datetime import datetime


def generate_report(report_data):

    # Make sure the reports folder exists
    os.makedirs("reports", exist_ok=True)

    # Create a unique filename using the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"reports/security_report_{timestamp}.json"

    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(report_data, file, indent=4)

        return file_name

    except OSError:
        return None
