from modules.report_viewer import view_latest_report, view_report_history
from modules.ip_lookup import lookup_ip
from modules.url_checker import check_url_format
from modules.file_hash import generate_file_hash
from colorama import Fore, init
from modules.password_checker import check_password_strength
from modules.report_generator import generate_report

init(autoreset=True, convert=True, strip=False)


def display_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "             CYBERGUARD TOOLKIT")
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "Your Personal Cybersecurity Assistant")
    print(Fore.CYAN + "=" * 50)


def main():
    tool_results = {}
    while True:
        display_banner()

        print("1. Password Strength Checker")
        print("2. URL Format Inspector")
        print("3. File Hash Generator")
        print("4. IP Information Lookup")
        print("5. Generate Security Report")
        print("6. View Latest Security Report")
        print("7. View Report History")
        print("8. Exit")

        choice = input(Fore.YELLOW + "\nSelect an option (1-8): ").strip()

        if choice == "1":
            print(Fore.CYAN + "\n--- Password Strength Checker ---")

            password = input("Enter a test password: ")

            strength, feedback = check_password_strength(password)

            tool_results["password_checker"] = {
                "strength": strength,
                "suggestions": feedback
            }

            print(Fore.YELLOW + f"\nPassword Strength: {strength}")

            if feedback:
                print(Fore.RED + "\nSuggestions:")
                for suggestion in feedback:
                    print("- " + suggestion)
            else:
                print(Fore.GREEN + "All basic checks passed!")
        
        elif choice == "2":
            print(Fore.CYAN + "\n--- URL Inspector ---")

            url = input("Enter URL to inspect: ")

            is_valid, message = check_url_format(url)

            tool_results["url_inspector"] = {
                "url": url,
                "valid_format": is_valid,
                "message": message
          }

            if is_valid:
                print(Fore.GREEN + "\n" + message)
            else:
                print(Fore.RED + "\n" + message)

        elif choice == "3":
            print(Fore.CYAN + "\n--- File Hash Generator ---")

            file_path = input("Enter file path: ")

            file_hash = generate_file_hash(file_path)

            tool_results["file_hash_generator"] = {
                 "file_path": file_path,
                 "sha256_hash": file_hash,
                 "success": file_hash is not None
            }

            if file_hash:
                print(Fore.GREEN + "\nSHA-256 Hash:")
                print(Fore.YELLOW + file_hash)
            else:
                print(Fore.RED + "\nError: File not found!")
        
        elif choice == "4":
            print(Fore.CYAN + "\n--- IP Information Lookup ---")
 
            ip_address = input("Enter a public IP address: ")

            result = lookup_ip(ip_address)

            tool_results["ip_lookup"] = {
                "input_ip": ip_address,
                "result": result
            }

            if result:
                print(Fore.GREEN + "\nIP Information:")
                for key, value in result.items():
                    print(Fore.YELLOW + f"{key.capitalize()}: {value}")
            else:
                    print(Fore.RED + "\nUnable to retrieve IP information.")
                
        
        elif choice == "5":
            print(Fore.CYAN + "\n--- Security Report Generator ---")

            report_data = {
                "project": "CyberGuard",
                "report_type": "Security Report",
                "tools_used": [
                    "Password Strength Checker",
                    "URL Format Inspector",
                    "File Hash Generator",
                    "IP Information Lookup"
                ],
                "results": tool_results
            }

            report_path = generate_report(report_data)

            if report_path:
                print(Fore.GREEN + "\nSecurity report generated successfully!")
                print(Fore.YELLOW + f"Report saved at: {report_path}")
            else:
                print(Fore.RED + "\nUnable to generate security report.")

        elif choice == "6":
            print(Fore.CYAN + "\n--- Latest Security Report ---")
            view_latest_report()
                

        elif choice == "7":
            print(Fore.CYAN + "\n--- Security Report History ---")
            view_report_history()
            
        elif choice == "8":
            print(Fore.GREEN + "\nThank you for using CyberGuard!")
            break

        input(Fore.CYAN + "\nPress Enter to continue...")


if __name__ == "__main__":
    main()

