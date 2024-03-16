import os

# This function has a command injection vulnerability
def run_command(command):
    os.system(command)

if __name__ == "__main__":
    user_input = input("Enter a command to run: ")
    run_command(user_input)
