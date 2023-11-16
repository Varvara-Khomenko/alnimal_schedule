import configparser


config = configparser.ConfigParser()
config.add_section("Settings")
config.set("Settings", "font", "Courier")