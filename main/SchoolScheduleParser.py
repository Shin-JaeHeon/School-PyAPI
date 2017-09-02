from . import SchoolError, SchoolSchedule


class SchoolScheduleParser:
    def parse(self, raw_data):
        if len(raw_data) < 1:
            raise SchoolError("불러온 데이터가 올바르지 않습니다.")
        monthly_schedule = []
        raw_data = str.replace(raw_data, r'\\s+', '')
        chunk = raw_data.split("text:\">")
        try:
            for item in chunk:
                trimed = item.split("</div>", 1)[0]
                date = trimed.split(">", 1)[1].split("</em>")[0]
                if len(date) < 1:
                    continue
                if trimed.index("<strong>") > 0:
                    monthly_schedule.append(SchoolSchedule(trimed.split("<strong>",1)[1].split("</strong>")[0]))
                else:
                    monthly_schedule.append(SchoolSchedule())
            return monthly_schedule
        except:
            raise SchoolError("학사일정 정보 파싱에 실패했습니다. 최신 버전으로 업데이트 해주세요")
