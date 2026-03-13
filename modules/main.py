import auth
import ip_gen
import scanner
import ip_check

def scan_results(target_ip, target_port):
    print(f"\n[*] Target locked: {target_ip}" )
    print(f"[*] Scanning ports")
    for port, service in target_port.items():
        is_open = scanner.check_port(target_ip, port)

        print( ".", end = "", flush = True)
            
        if is_open:
            print(f"\nPort: {port}, service: {service} is Open 🔓")
    print()

def start_shadow_terminal():

    USER = "admin"
    PASSWD = "secret"

    target_port = {
        21:"FTP",
        22:"SSH",
        80:"HTTP",
        443:"HTTPS",
        53:"DNS"
    }

    print("--- System online ---")

    auth.login(USER, PASSWD)

    print(f"\n--- Targeting system online ---")
    print(f"Protocol loaded: {list(target_port.values())}")

    choice = input("\nChoose your variance for scanning: \n1. Random targets \n2. Specific targets \n> ")
    
    match choice:
        case "1":
             scan_random_targets(target_port)
        case "2":
            print("Wright specific target(s)...")
            while True:
                target_ip = input("Enter target IP (or 'done' to finish): ")
                if target_ip.lower() == "done":
                    return 0
                if ip_check.is_valid_ip(target_ip):
                    scan_results(target_ip, target_port)
                else:
                    print("Invalid IP address. Please try again.")
        case _:
            print("Invalid choice. Exiting.")

    for i in range(3):
        target_ip = ip_gen.generate_target()

        scan_results(target_ip, target_port)

if __name__ == "__main__":
    start_shadow_terminal()