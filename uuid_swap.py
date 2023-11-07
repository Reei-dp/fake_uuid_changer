from winreg import OpenKey, SetValueEx, CloseKey, REG_SZ, HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS
from uuid import uuid4


def swap():
    key = OpenKey(HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, KEY_ALL_ACCESS)
    SetValueEx(key, 'FAKE_UID', 0, REG_SZ, str(uuid4()))
    CloseKey(key)


if __name__ == "__main__":
    swap()
