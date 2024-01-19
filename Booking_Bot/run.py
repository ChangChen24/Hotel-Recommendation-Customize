from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency()
        bot.select_place_to_go('New York')
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Wondows: \n'
            '  set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '  PATH=$PATH: /path/toyour/folder/ \n'
        )
    else:
        raise