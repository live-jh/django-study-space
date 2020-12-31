class YearConverter:
    regex = r"20\d{2}"

    # url 매칭 후 view 함수 호출전 인자 검사
    def to_python(self, value):
        return int(value)

    # url reverse
    def to_url(self, value):
        # return "%04d" % value
        return str(value)


class MonthConverter(YearConverter):
    regex = r"d{1,2}"


class DayConverter(YearConverter):
    regex = r"[0-3]\d"
