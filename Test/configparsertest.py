import configparser


config = configparser.ConfigParser()
print(config.sections())
config.read("../setting/setting.ini")
print(config.sections())
print(config["SKIN"]["skin_theme"])