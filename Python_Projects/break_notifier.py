from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Take Break.\nGo have some streaching or Coffee",
            message = "Taking break is important for your wellbeing.\nBreaks reduces stress, enhance your mood, improve concentration, recharge your body and increases your productivity.",
            app_icon = "Python_Projects/images.ico",
            timeout = 5)
        time.sleep(10)
    