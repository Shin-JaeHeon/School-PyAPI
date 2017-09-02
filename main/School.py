from enum import Enum
import urllib.request
from . import SchoolError
from io import StringIO


class Type(Enum):
    def __int__(self, id):
        self.id = id

    # 병설유치원
    KINDERGARTEN = 1,
    # 초등학교
    ELEMENTARY = 2,
    # 중학교
    MIDDLE = 3,
    # 고등학교
    HIGH = 4


class Region(Enum):
    def __init__(self, url):
        self.url = url

    # 서울
    seoul = "stu.sen.go.kr"
    # 인천
    incheon = "stu.ice.go.kr"
    # 부산
    busan = "stu.pen.go.kr"
    # 광주
    gwangju = "stu.gen.go.kr"
    # 대전
    daejeon = "stu.dje.go.kr"
    # 대구
    daegu = "stu.dge.go.kr"
    # 세종
    sejong = "stu.sje.go.kr"
    # 울산
    ulsan = "stu.use.go.kr"
    # 경기
    gyeonggi = "stu.goe.go.kr"
    # 강원
    kangwon = "stu.kwe.go.kr"
    # 충북
    chungbuk = "stu.cbe.go.kr"
    # 충남
    chungnam = "stu.cne.go.kr"
    # 경북
    gyeongbuk = "stu.gbe.go.kr"
    # 경남
    gyeongnam = "stu.gne.go.kr"
    # 전북
    jeonbuk = "stu.jbe.go.kr"
    # 전남
    jeonnam = "stu.jne.go.kr"
    # 제주
    jeju = "stu.jje.go.kr"


def get_content_from_url(url, after, before):
    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req).red()
        return res.split(after)[1].split("before")[0]
    except urllib.request.HTTPError:
        return SchoolError("HTTP 통신 에러 ")
    except urllib.request.URLError:
        return SchoolError("URL을 확인하세요.")


class School:
    Monthly_Menu_Url = "sts_sci_md00_001.do"
    Schedule_Url = "sts_sci_sf01_001.do"

    def __init__(self, schoolType, schoolRegion, schoolCode):
        self.schoolType = schoolType
        self.schoolRegion = schoolRegion
        self.schoolCode = schoolCode

    def get_monthly_menu(self, year, month):
        url = StringIO()
        url.write("http://" + self.schoolRegion.url + "/" + School.Monthly_Menu_Url + "?")
        url.write("schulCode=" + self.schoolCode + "&")
        url.write("schulCrseScCode=" + self.schoolType.id + "&"+"schulKndScCode=" + self.schoolType.id + "&")
        url.write("ay=" + year + "&"+"mm=" + month.format("%02d"))
        content = get_content_from_url("<tbody>", "</tbdoy>")
        return content
