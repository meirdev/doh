# PoC

# import os
# import os.path


# def get_latest_command() -> str:
#     shell = os.path.basename(os.environ["SHELL"])
#     history_file = os.path.expanduser(f"~/.{shell}_history")

#     with open(history_file) as fp:
#         latest_command = ""

#         while True:
#             try:
#                 line = fp.readline()
#             except UnicodeDecodeError:
#                 continue

#             if not line:
#                 break

#             latest_command = line

#         return latest_command.strip()
