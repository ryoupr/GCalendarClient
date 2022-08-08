import PySimpleGUI as sg
config = sg.UserSettings(
    './settings.ini', use_config_file=True, convert_bools_and_none=True)

config['TEST MENUE']['test11'] = 'mat'
print(config['TEST MENUE']['test1'])
