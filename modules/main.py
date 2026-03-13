import auth
import ip_gen
import scanner

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

    for i in range(3):
        target_ip = ip_gen.generate_target()

        if i == 0:
            target_ip = "8.8.8.8"

        print(f"\n[*] Target locked: {target_ip}" )
        print(f"[*] Scanning ports")
        for port, service in target_port.items():
            is_open = scanner.check_port(target_ip, port)

            print( ".", end = "", flush = True)
                
            if is_open:
                print(f"\nPort: {port}, service: {service} is Open 🔓")
        print()

if __name__ == "__main__":
    start_shadow_terminal()
