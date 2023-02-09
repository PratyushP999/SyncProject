from plyer import notification
import time

while True:
    notification.notify(
        title="please take medicine",
        message="timely medicine improves health condition.",
        app_icon="D:\sync intern\pills_pill_bottle_medicine_medical_healthcare_icon_141993.ico",
        timeout=10,
        toast=True

    )
    time.sleep(30)