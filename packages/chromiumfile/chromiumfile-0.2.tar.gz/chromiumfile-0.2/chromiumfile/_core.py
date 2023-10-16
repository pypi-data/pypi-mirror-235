from pathlib import Path
from sys import platform


root_path = Path(__file__).parent / 'chromium'

win_chromium_dir = (root_path / 'win').absolute()
win_bootstrap_file = (root_path / 'win/chrome.exe').absolute()

mac_chromium_dir = (root_path / 'mac').absolute()
mac_bootstrap_file = (root_path / 'mac/chrome.exe').absolute()

linux_chromium_dir = (root_path / 'linux').absolute()
linux_bootstrap_file = (root_path / 'linux/chrome.exe').absolute()

platform = platform.lower()

if 'win' in platform:
    chromium_dir = win_chromium_dir
    bootstrap_file = win_bootstrap_file

elif 'mac' in platform:
    chromium_dir = mac_chromium_dir
    bootstrap_file = mac_bootstrap_file

elif 'linux' in platform:
    chromium_dir = linux_chromium_dir
    bootstrap_file = linux_bootstrap_file