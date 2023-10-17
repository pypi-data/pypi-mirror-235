import threading
import winreg
import time


# 获取个性化颜色函数
def get_windows_system_color():
    color_key_path = r"Software\Microsoft\Windows\DWM"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, color_key_path)
        value, _ = winreg.QueryValueEx(key, "ColorizationColor")
        alpha = (value >> 24) & 0xFF
        red = (value >> 16) & 0xFF
        green = (value >> 8) & 0xFF
        blue = value & 0xFF
        return red, green, blue, alpha
    except Exception as e:
        return repr(e)


def get_Oldwindows_system_color():
    color_key_path = r"Control Panel\Colors"
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, color_key_path)
        value, _ = winreg.QueryValueEx(key, "ColorizationColor")
        alpha = (value >> 24) & 0xFF
        red = (value >> 16) & 0xFF
        green = (value >> 8) & 0xFF
        blue = value & 0xFF
        return red, green, blue, alpha
    except Exception as e:
        return repr(e)


class On_theme_change():
    def __init__(self):
        self.value = None
        self.hkey = None
        self.current_value = None
        self.on_theme_change = None
        self.theme_change()

    def theme_change(self):
        try:
            self.hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                       r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            self.current_value = winreg.QueryValueEx(self.hkey, "AppsUseLightTheme")[0]
            winreg.CloseKey(self.hkey)

            self.hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                       r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            self.value = winreg.QueryValueEx(self.hkey, "AppsUseLightTheme")[0]
            winreg.CloseKey(self.hkey)
            self.on_theme_change = False

            if self.current_value != self.value:
                self.current_value = self.value
                self.on_theme_change = True
                return self.on_theme_change



        except KeyboardInterrupt:
            pass


class ThemeColorMonitor:
    def __init__(self, callback):
        self.previous_accent_color = None
        self.callback = callback

    def get_current_accent_color(self):
        key_path = r"SOFTWARE\Microsoft\Windows\DWM"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)
        accent_color, _ = winreg.QueryValueEx(key, "AccentColor")
        winreg.CloseKey(key)
        return accent_color

    def check_theme_change(self):
        current_accent_color = self.get_current_accent_color()

        if current_accent_color != self.previous_accent_color:
            self.callback(current_accent_color)

        self.previous_accent_color = current_accent_color

        timer = threading.Timer(1.0, self.check_theme_change)
        timer.start()

# # 示例回调函数
# def theme_color_changed(accent_color):
#     print("主题色已更改:", accent_color)
#
#
# # 创建主题色监控对象并启动监控
# monitor = ThemeColorMonitor(callback=theme_color_changed)
# monitor.check_theme_change()
