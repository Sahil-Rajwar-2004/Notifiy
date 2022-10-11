from winotify import Notification,audio

notify = Notification(
    app_id = "Info",
    title = "Hello",
    msg = "Shut the f**k up",
    duration = "short"
)

notify.set_audio(audio.Default,loop = False)
notify.add_actions(label = "Click Me!",launch = "https://www.google.com/")
notify.show()

