
"""BR: Backup and Retrieve
"""

from platform import system
# import subprocess
import crocodile.toolbox as tb
from machineconfig.utils.utils import LIBRARY_ROOT, DEFAULTS_PATH, print_programming_script, choose_cloud_interactively, display_options
from typing import Any, Literal


OPTIONS = Literal["BACKUP", "RETRIEVE"]


def main(direction: OPTIONS):
    try:
        cloud: str = tb.Read.ini(DEFAULTS_PATH)['general']['rclone_config_name']
        print(f"\n{'--' *  50}\n⚠️ Using default cloud: `{cloud}` ⚠️\n{'--' *  50}\n")
    except (FileNotFoundError, KeyError, IndexError): cloud = choose_cloud_interactively()

    bu_file: dict[str, Any] = LIBRARY_ROOT.joinpath("profile/backup.toml").readit()
    if system() == "Linux": bu_file = {key: val for key, val in bu_file.items() if "windows" not in key}
    elif system() == "Windows": bu_file = {key: val for key, val in bu_file.items() if "linux" not in key}

    choice_key = display_options(msg=f"WHICH FILE of the following do you want to {direction}?", options=['all'] + list(bu_file.keys()))
    assert isinstance(choice_key, str)
    if choice_key == "all": items = bu_file
    else: items = {choice_key: bu_file[choice_key]}

    program = f"""$cloud = "{cloud}:" \n """ if system() == "Windows" else f"""cloud="{cloud}:" \n """
    for item_name, item in items.items():
        flags = ''
        flags += 'z' if item['zip'] == 'True' else ''
        flags += 'e' if item['encrypt'] == 'True' else ''
        flags += 'r' if item['rel2home'] == 'True' else ''
        flags += 'o' if system().lower() in item_name else ''
        if flags: flags = "-" + flags
        if direction == "BACKUP": program += f"""\ncloud_copy "{tb.P(item['path']).as_posix()}" $cloud {flags}\n"""
        elif direction == "RETRIEVE": program += f"""\ncloud_copy $cloud "{tb.P(item['path']).as_posix()}" {flags}\n"""
        else: raise RuntimeError(f"Unknown direction: {direction}")
        if item_name == "dotfiles" and system() == "Linux": program += f"""\nchmod 700 ~/.ssh/*\n"""
    # program += f"""\ncd ~/dotfiles; cloud_repo_sync --cloud {cloud}\n"""
    print_programming_script(program, lexer="shell", desc=f"{direction} script")
    # print(program)
    return program


if __name__ == "__main__":
    pass
