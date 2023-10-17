from setuptools import setup, find_packages

setup(
    name='lhackerkarim',
    version='9.0',
    packages=find_packages(),
    install_requires=[
        'telebot',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'lhackerkarim = lhackerkarim:main',
        ],
    },
    author='Karimos',
    author_email='Shellcloud18@gmail.com',
    description='Secure Hacking Telegram Bot',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    # Example usage of the script
    example_usage='''
    # Import the LhackerKarim class
    from lhackerkarim import LhackerKarim

    def main():
        # Telegram bot token (replace with your own)
        telegram_token = 'YOUR_TELEGRAM_TOKEN'

        # Telegram chat ID (replace with your own)
        chat_id = 'YOUR_CHAT_ID'

        # Program name (replace with your own)
        program_name = 'securechat'

        # Create an instance of the SecureChat class
        bot = LhackerKarim(telegram_token, chat_id, program_name)

        # Start the bot
        bot.start_bot()
    '''
)

