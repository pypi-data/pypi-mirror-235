"""A module to control setting OpenBB Hub PAT"""

from openbb_terminal.core.session.sdk_session import login


def openbb_login(PAT: str):
    login(token=PAT, keep_session=True)
