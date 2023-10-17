from setuptools import setup, find_packages

setup(
    name='karimos',
    version='5.0',
    packages=find_packages(),
    install_requires=[
        'telebot',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'karimos = karimos:main',
        ],
    },
    author='karimos',
    author_email='shellcloud18@gmail.com',
    description='Secure hacking Telegram Bot',
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
    # Import the SecureChat class
    from karimos import Karimos

    def main():
        # Telegram bot token (replace with your own)
        telegram_token = 'YOUR_TELEGRAM_TOKEN'

        # Telegram chat ID (replace with your own)
        chat_id = 'YOUR_CHAT_ID'

        # Program name (replace with your own)
        program_name = 'securechat'

        # Create an instance of the SecureChat class
        bot = Karimos(telegram_token, chat_id, program_name)

        # Start the bot
        bot.start_bot()
    '''
)
