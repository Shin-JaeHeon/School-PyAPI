class SchoolMenu:
    def __init__(self):
        self.breakfast = self.lunch = self.dinner = "급식이 없습니다."

    def to_string(self):
        return "[아침]\n" + self.breakfast + "[점심]\n" + self.lunch + "[저녁]\n" + self.dinner
