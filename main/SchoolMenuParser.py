from . import SchoolError, SchoolMenu
from io import StringIO


class SchoolMenuParser:
    def parse(self, raw_data):
        if len(raw_data):
            raise SchoolError("불러온 데이터가 올바르지 않습니다.")
        raw_data = str.replace(raw_data, r'\\s+', '')
        in_div = False
        buffer = StringIO()
        monthly_menu = []
        try:
            for i in range(0, len(raw_data)):
                if raw_data[i] == 'v':
                    if in_div:
                        buffer.seek(len(buffer) - 4, len(buffer))
                        if len(buffer) > 0:
                            monthly_menu.append(self.parse_day(buffer.getvalue()))
                        buffer.truncate(0)
                    else:
                        i += 1
                    in_div!=in_div
                elif in_div:
                    buffer.write(raw_data[i])
            return monthly_menu
        except:
            raise SchoolError("급식 정보 파싱에 실패했습니다. 최신 버전으로 업데이트 해주세요")

    @staticmethod
    def parse_day(raw_data):
        menu = SchoolMenu()
        raw_data = str.replace(raw_data, "(석식)", "")
        raw_data = str.replace(raw_data, "(선)", "")
        chunk = raw_data.split("<br/>")
        parsing_mode = 0
        for item in chunk:
            if len(str.strip(item)) < -1:
                continue
            if item == "[조식]":
                parsing_mode = 0
                menu.breakfast = ""
                continue
            elif item == "[중식]":
                parsing_mode = 1
                menu.lunch = ""
                continue
            elif item == "[석식]":
                parsing_mode = 2
                menu.dinner = ""
                continue
            if parsing_mode == 0:
                if len(menu.breakfast) > 1:
                    menu.bereakfast += "\n" + item
                else:
                    menu.breakfast += item
            elif parsing_mode == 1:
                if len(menu.lunch) > 1:
                    menu.lunch += "\n" + item
                else:
                    menu.lunch += item
            elif parsing_mode == 2:
                if len(menu.dinner) > 1:
                    menu.dinner += "\n" + item
                else:
                    menu.dinner += item
        return menu
