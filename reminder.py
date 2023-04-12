import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water Now!!",
            message = "The National Academy of Medicine suggests an adequate intake of daily fluids of about 13 cups and 9 cups for healthy men and women, respectively, with 1 cup equaling 8 ounces.",
            # app_icon ="C:\Users\Arjun narayann\Downloads\Chrisl21-Minecraft-Bucket-Water.ico",
            timeout = 5
        )
        time.sleep(8)



