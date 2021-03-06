import winsound
from win10toast import ToastNotifier

def timer(reminder,seconds):
    notify=ToastNotifier()
    notify.show_toast("Reminder",f" ""Alarm will go off in (seconds) Seconds""",duration=10)
    notify.show_toast(f"Reminder",reminder,duration=10)

    frequency=2000
    duration=1000
    winsound.MessageBeep(frequency,duration)

if __name__=="__main__":
    words=input("What would you remind of:")
    sec=int(input("Enter Seconds:"))
    timer(words,sec)
