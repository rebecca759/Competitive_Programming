class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        res = []
        day,mon,year = date.split(" ")
        month = str(months[mon])
        day = day[:len(day)-2]
        dd = day if len(day) == 2 else "0"+day
        mm = month if len(month) == 2 else "0"+month

        return year+"-"+mm+"-"+dd