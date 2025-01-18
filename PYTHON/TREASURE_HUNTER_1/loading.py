import time
import random
from termcolor import colored, cprint
import os
import sys

os.system("color")

def play_sound():
    # Chức năng này có thể được sử dụng để phát âm thanh
    # Bạn có thể thay thế bằng cách sử dụng thư viện như winsound trên Windows
    pass


def clear_console():
    print("\033[H\033[J", end="")  # Di chuyển con trỏ về đầu và xóa màn hình.



class Loading():
    def __init__(self) -> None:
        self.percent : int = 0
        self.dot : list[str] = [".", "..", "..."]
        self.load : list[str] = [">_<", "o_o", ">_<"]
        self.src = [
            "load_CONFIG_SETTINGS",
            "get_USER_PERMISSIONS",
            "load_DATABASE_CONNECTION",
            "check_DISK_SPACE",
            "load_LOG_FILE",
            "get_ACTIVE_SESSIONS",
            "load_USER_PROFILE",
            "check_API_STATUS",
            "get_APPLICATION_VERSION",
            "load_SESSION_DATA",
            "check_MEMORY_USAGE",
            "load_ENVIRONMENT_VARIABLES",
            "get_USER_INPUT",
            "load_SECURITY_SETTINGS",
            "check_SERVICE_HEALTH",
            "load_PLUGIN_LIST",
            "get_SYSTEM_LOGS",
            "load_NETWORK_CONFIG",
            "check_FIREWALL_SETTINGS",
            "get_PROCESS_LIST",
            "load_ERROR_HANDLING",
            "check_UPDATE_AVAILABLE",
            "load_CACHE_SETTINGS",
            "get_SYSTEM_MAINTENANCE",
            "load_MODULE_DEPENDENCIES",
            "check_USER_ACTIVITY",
            "get_PERFORMANCE_METRICS",
            "load_ASSET_MANAGEMENT",
            "check_DATABASE_INTEGRITY",
            "get_NOTIFICATION_SETTINGS",
            "load_ACCESS_LOGS",
            "check_SYSTEM_UPDATES",
            "get_CLOUD_STORAGE_INFO",
            "load_EMAIL_SETTINGS",
            "check_VPN_CONNECTION",
            "get_HARDWARE_INFO",
            "load_BACKUP_CONFIG",
            "check_USER_SESSION_TIMEOUT",
            "get_API_KEYS",
            "load_CRON_JOBS",
            "check_SYSTEM_SECURITY",
            "get_APPLICATION_LOGS",
            "load_DEPLOYMENT_INFO",
            "check_MEMORY_LIMITS",
            "get_SERVICE_STATUS",
            "load_BACKEND_SERVICES",
            "check_LOAD_BALANCER",
            "get_SSL_CERTIFICATES",
            "load_USER_ACTIVITY_LOG",
            "check_NETWORK_TRAFFIC",
            "get_THROUGHPUT_METRICS",
            "load_USER_SESSION_DATA",
            "check_DISK_USAGE",
            "get_TROUBLESHOOTING_GUIDE",
            "load_EXPORT_SETTINGS",
            "check_DATA_COMPLIANCE",
            "get_SYSTEM_NOTIFICATIONS",
            "load_PERFORMANCE_LOGS",
            "check_SERVICE_DEPENDENCIES",
            "get_DASHBOARD_DATA",
            "load_SESSION_ACTIVITY",
            "check_CACHE_HIT_RATIO",
            "get_SERVICE_PROVIDER_INFO",
            "load_USER_FEEDBACK",
            "check_SYSTEM_BACKUPS",
            "get_PROCESS_MONITORING",
            "load_DEPENDENCY_GRAPH",
            "check_SYSTEM_RESTART",
            "get_USER_AUTHENTICATION",
            "load_ASSET_TRACKING",
            "check_SCHEDULED_TASKS",
            "get_API_USAGE_STATS",
            "load_FILE_SYSTEM_INFO",
            "check_APPLICATION_LOGGING",
            "get_NETWORK_TOPOLOGY",
            "load_USER_SETTINGS",
            "check_MEMORY_ALLOCATIONS",
            "get_SYSTEM_CONFIG",
            "load_CRASH_REPORTS",
            "check_HEALTH_CHECKS",
            "get_PERFORMANCE_PROFILES",
            "load_DATA_ANALYTICS",
            "check_USER_PRIVILEGES",
            "get_APPLICATION_ENDPOINTS",
            "load_SERVICE_LOGS",
            "check_INTEGRATION_STATUS",
            "get_DEPLOYMENT_STATUS",
            "load_CACHE_MEMORY",
            "check_NETWORK_MONITORING",
            "get_SYSTEM_AUDIT_LOGS",
            "load_CONNECTION_POOL",
            "check_ERROR_LOGS",
            "get_SYSTEM_RESOURCE_USAGE",
            "load_MODULE_CONFIG",
            "check_APPLICATION_PERFORMANCE",
            "get_NETWORK_BANDWIDTH",
            "load_ACCESS_CONTROL_LIST",
            "check_SERVICE_LOGGING",
            "get_SYSTEM_MONITORING",
            "load_APPLICATION_SETTINGS",
            "check_DATABASE_CONNECTIONS",
            "get_API_ENDPOINTS",
            "load_TROUBLESHOOTING_LOGS",
            "check_LOAD_BALANCING",
            "get_USER_NOTIFICATION_SETTINGS",
            "load_SERVICE_MONITORING",
            "check_SYSTEM_SETTINGS",
            "get_APPLICATION_DEPENDENCIES",
            "load_SYSTEM_BACKUP_LOGS",
            "check_DATA_BACKUP",
            "get_SYSTEM_UPTIME",
            "load_SESSION_LOGS",
            "check_USER_ACCESS",
            "get_SERVER_HEALTH_CHECK",
            "load_SECURITY_AUDIT_LOGS",
            "check_APPLICATION_STATUS",
            "get_SCRIPT_EXECUTION_LOGS",
            "load_NETWORK_ACTIVITY_LOGS",
            "check_RESOURCE_ALLOCATION"
        ]
        self.x : int = 0
        self.y : int = 0

    def start(self):
        while self.percent <= 100:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n" * 5)
            print(" " * 65, colored("Welcome to the VN_studio " + self.load[self.x], "white", "on_blue"))
            sys.stdout.write("\n" * 15)
            print(" " * 70, colored("Loading" + self.dot[self.x], "white"))
            play_sound()  # Phát âm thanh khi loading
            self.x = (self.x + 1) % len(self.load)
            self.y = (self.y + 1) % len(self.src)

            self.percent += random.randint(0, 5)
            if self.percent >= 100:
                clear_console()
                print("\n" * 5)
                print(" " * 65, colored("Welcome to the VN_studio >.<", "white", "on_blue"))
                sys.stdout.write("\n" * 15)
                print(" " * 55, colored("Loading success !", "white"))
                print(" " * 50, "[", colored("=" * 50,"green", "on_green"), "] 100%")
                time.sleep(2.5)
                os.system("cls" if os.name == "nt" else "clear")
                break
            
            print(
                " " * 50,
                "[ ",
                colored("=" * (self.percent // 2), "green", "on_green"),
                " " * ((100 - self.percent) // 2),
                "] ",
                self.percent,
                "%",
            )
            
            print("\n", " " * 80,f"{self.src[self.y]}")
            time.sleep(0.5)

        os.system("cls" if os.name == "nt" else "clear")
        print("\n" * 5)
        print(" " * 65, colored("Welcome to the VN_studio >.<", "white", "on_blue"))
        sys.stdout.write("\n" * 15)
        print(" " * 55, colored("Loading success !", "white"))
        print(" " * 50, "[", colored("=" * 50, "green", "on_green"), "] 100%")
        time.sleep(2.5)
        clear_console()

Loading().start()