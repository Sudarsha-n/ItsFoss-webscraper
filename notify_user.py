from plyer import notification

def notify_user(count):
    notification.notify(
        title= "Itsfoss Bot",
        message = f"We checked the website and found {count} new articles for you to read"
    )
