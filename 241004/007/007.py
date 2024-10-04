class SecretMeeting:
    def __init__(self, secret_code, meeting_place, time):
        self.secret_code = secret_code
        self.meeting_place = meeting_place
        self.time = time
    def display_info(self):
        print(f"secret code : {self.secret_code}")
        print(f"meeting point : {self.meeting_place}")
        print(f"time : {self.time}")

secret_code, meeting_place, time = input().split()
time = int(time)
meeting = SecretMeeting(secret_code, meeting_place, time)
meeting.display_info()