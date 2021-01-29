# -*- coding:UTF-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
import base64
import json
import random
import sys
import re


def daily_report(cookie,reportData,delayReport = False):  #最后个参数是补报用的
    # if(delayReport==False):
    #     reportUrl = "https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?t=" + reportData["Time_1or2"]
    # else:
    #     reportUrl = "https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?day="+ reportData["date"].replace(" ","") + "t=" + reportData["Time_1or2"]
    reportUrl = "https://selfreport.shu.edu.cn/DayReport.aspx"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    }
    response = requests.get(reportUrl, cookies=cookie)
    soup = BeautifulSoup(response.text, 'html.parser')
    view_state = soup.find('input', attrs={'name': '__VIEWSTATE'})
   # print(view_state)
    data = {
        "__EVENTTARGET": "p1$ctl00$btnSubmit",
        "__EVENTARGUMENT": "",
        "__VIEWSTATE": view_state['value'],
        "__VIEWSTATEGENERATOR": "7AD7E509",
        "p1$ChengNuo": "p1_ChengNuo",
        "p1$BaoSRQ": reportData["date"],
        "p1$DangQSTZK": "良好",
        "p1$TiWen": "",
        "p1$JiuYe_ShouJHM": "",
        "p1$JiuYe_Email": "",
        "p1$JiuYe_Wechat": "",
        "p1$QiuZZT":  "",
        "p1$JiuYKN": "",
        "p1$JiuYSJ": "",
        "p1$TiWen": "",
        "p1$ZaiXiao": "不在校",
        "p1$MingTDX":"不到校",
        "p1$BanChe_1$Value": "0",
        "p1$BanChe_1": "不需要乘班车",
        "p1$BanChe_2$Value": "0",
        "p1$BanChe_2": "不需要乘班车",
        "p1$GuoNei": "国内",
        "p1$ddlGuoJia$Value": "-1",
        "p1$ddlGuoJia": "选择国家",
        "p1$ShiFSH": "否",
        "p1$ddlSheng$Value": reportData["sheng"],  #当天所在省
        "p1$ddlSheng":  reportData["sheng"],
        "p1$ddlShi$Value": reportData["shi"],#当天所在市
        "p1$ddlShi": reportData["shi"],
        "p1$ddlXian$Value": reportData["xian"],
        "p1$ddlXian": reportData["xian"],
        "p1$XiangXDZ": reportData["location"],
        # "p1$ddlXian$Value": reportData["county"],#当天所在县
        # "p1$ddlXian": reportData["county"],
       # "p1$XiangXDZ": reportData["location"],
        "p1$FengXDQDL": "否",
        "p1$TongZWDLH": "否",
        "p1$CengFWH": "否",
        "p1$CengFWH_RiQi": "",
        "p1$CengFWH_BeiZhu": "",
        "p1$JieChu": "否",
        "p1$JieChu_RiQi": "",
        "p1$JieChu_BeiZhu": "",
        "p1$TuJWH": "否",
        "p1$TuJWH_RiQi": "",
        "p1$TuJWH_BeiZhu": "",
        "p1$QueZHZJC$Value": "否",
        "p1$QueZHZJC": "否",
        "p1$DangRGL": "否",
        "p1$GeLDZ": "",
        "p1$FanXRQ": "",
        "p1$WeiFHYY": "",
        "p1$ShangHJZD": "",
        "p1$DaoXQLYGJ": "",
        "p1$DaoXQLYCS": "",
        "p1$JiaRen_BeiZhu": "",
        "p1$SuiSM": "绿色",
        "p1$LvMa14Days": "是",
        "p1$Address2": "",
        "F_TARGET": "p1_ctl00_btnSubmit",
        "p1_ContentPanel1_Collapsed": "true",
        "p1_GeLSM_Collapsed": "false",
        "p1_Collapsed": "false",
        'F_STATE': get_FState(reportData),
    }
    header = {
        'X-FineUI-Ajax': 'true',
    }
    if (reportData["sheng"]=="上海"):
        data["p1$ShiFSH"]="是"
        data["p1$ShiFZX"]="否"
    response = requests.post(reportUrl, data=data, cookies=cookie,headers=header)
   #  print(response.text)
    return response.text.find("提交成功")


def get_FState(reportData):
    F_STATE_Former = "eyJwMV9CYW9TUlEiOnsiVGV4dCI6IjIwMjEtMDEtMjQifSwicDFfRGFuZ1FTVFpLIjp7IkZfSXRlbXMiOltbIuiJr+WlvSIsIuiJr+Wlve+8iOS9k+a4qeS4jemrmOS6jjM3LjPvvIkiLDFdLFsi5LiN6YCCIiwi5LiN6YCCIiwxXV0sIlNlbGVjdGVkVmFsdWUiOiLoia/lpb0ifSwicDFfWmhlbmdaaHVhbmciOnsiSGlkZGVuIjp0cnVlLCJGX0l0ZW1zIjpbWyLmhJ/lhpIiLCLmhJ/lhpIiLDFdLFsi5ZKz5Ze9Iiwi5ZKz5Ze9IiwxXSxbIuWPkeeDrSIsIuWPkeeDrSIsMV1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOltdfSwicDFfUWl1WlpUIjp7IkZfSXRlbXMiOltdLCJTZWxlY3RlZFZhbHVlQXJyYXkiOltdfSwicDFfSml1WUtOIjp7IkZfSXRlbXMiOltdLCJTZWxlY3RlZFZhbHVlQXJyYXkiOltdfSwicDFfSml1WVlYIjp7IlJlcXVpcmVkIjpmYWxzZSwiRl9JdGVtcyI6W10sIlNlbGVjdGVkVmFsdWVBcnJheSI6W119LCJwMV9KaXVZWkQiOnsiRl9JdGVtcyI6W10sIlNlbGVjdGVkVmFsdWVBcnJheSI6W119LCJwMV9KaXVZWkwiOnsiRl9JdGVtcyI6W10sIlNlbGVjdGVkVmFsdWVBcnJheSI6W119LCJwMV9aYWlYaWFvIjp7IlNlbGVjdGVkVmFsdWUiOiLkuI3lnKjmoKEiLCJGX0l0ZW1zIjpbWyLkuI3lnKjmoKEiLCLkuI3lnKjmoKEiLDFdLFsi5a6d5bGxIiwi5a6d5bGx5qCh5Yy6IiwxXSxbIuW7tumVvyIsIuW7tumVv+agoeWMuiIsMV0sWyLlmInlrpoiLCLlmInlrprmoKHljLoiLDFdLFsi5paw6Ze46LevIiwi5paw6Ze46Lev5qCh5Yy6IiwxXV19LCJwMV9NaW5nVERYIjp7IlNlbGVjdGVkVmFsdWUiOiLkuI3liLDmoKEiLCJGX0l0ZW1zIjpbWyLkuI3liLDmoKEiLCLkuI3liLDmoKEiLDFdLFsi5a6d5bGxIiwi5a6d5bGx5qCh5Yy6IiwxXSxbIuW7tumVvyIsIuW7tumVv+agoeWMuiIsMV0sWyLlmInlrpoiLCLlmInlrprmoKHljLoiLDFdLFsi5paw6Ze46LevIiwi5paw6Ze46Lev5qCh5Yy6IiwxXV19LCJwMV9NaW5nVEpDIjp7IlJlcXVpcmVkIjpmYWxzZSwiSGlkZGVuIjp0cnVlLCJGX0l0ZW1zIjpbWyLmmK8iLCLmmK8iLDFdLFsi5ZCmIiwi5ZCmIiwxXV0sIlNlbGVjdGVkVmFsdWUiOm51bGx9LCJwMV9CYW5DaGVfMSI6eyJIaWRkZW4iOnRydWUsIkZfSXRlbXMiOltbIjAiLCLkuI3pnIDopoHkuZjnj63ovaYiLDEsIiIsIiJdLFsiMSIsIjHlj7fnur/vvJrlmInlrprmoKHljLrljZfpl6g9PuWuneWxseagoeWMuiIsMSwiIiwiIl0sWyIyIiwiMuWPt+e6v++8muWuneWxseagoeWMuj0+5ZiJ5a6a5qCh5Yy65Y2X6ZeoIiwxLCIiLCIiXSxbIjMiLCIz5Y+357q/77ya5bu26ZW/5qCh5Yy65YyX6ZeoPT7lrp3lsbHmoKHljLoiLDEsIiIsIiJdLFsiNCIsIjTlj7fnur/vvJrlrp3lsbHmoKHljLo9PuW7tumVv+agoeWMuuWMl+mXqCIsMSwiIiwiIl0sWyI1IiwiNeWPt+e6v++8muWYieWumuagoeWMuuWNl+mXqD0+5bu26ZW/5qCh5Yy65YyX6ZeoIiwxLCIiLCIiXSxbIjYiLCI25Y+357q/77ya5bu26ZW/5qCh5Yy65YyX6ZeoPT7lmInlrprmoKHljLrljZfpl6giLDEsIiIsIiJdXSwiU2VsZWN0ZWRWYWx1ZUFycmF5IjpbIjAiXX0sInAxX0JhbkNoZV8yIjp7IkhpZGRlbiI6dHJ1ZSwiRl9JdGVtcyI6W1siMCIsIuS4jemcgOimgeS5mOePrei9piIsMSwiIiwiIl0sWyIxIiwiMeWPt+e6v++8muWYieWumuagoeWMuuWNl+mXqD0+5a6d5bGx5qCh5Yy6IiwxLCIiLCIiXSxbIjIiLCIy5Y+357q/77ya5a6d5bGx5qCh5Yy6PT7lmInlrprmoKHljLrljZfpl6giLDEsIiIsIiJdLFsiMyIsIjPlj7fnur/vvJrlu7bplb/moKHljLrljJfpl6g9PuWuneWxseagoeWMuiIsMSwiIiwiIl0sWyI0IiwiNOWPt+e6v++8muWuneWxseagoeWMuj0+5bu26ZW/5qCh5Yy65YyX6ZeoIiwxLCIiLCIiXSxbIjUiLCI15Y+357q/77ya5ZiJ5a6a5qCh5Yy65Y2X6ZeoPT7lu7bplb/moKHljLrljJfpl6giLDEsIiIsIiJdLFsiNiIsIjblj7fnur/vvJrlu7bplb/moKHljLrljJfpl6g9PuWYieWumuagoeWMuuWNl+mXqCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsiMCJdfSwicDFfR3VvTmVpIjp7IkZfSXRlbXMiOltbIuWbveWGhSIsIuWbveWGhSIsMV0sWyLlm73lpJYiLCLlm73lpJYiLDFdXSwiU2VsZWN0ZWRWYWx1ZSI6IuWbveWGhSJ9LCJwMV9kZGxHdW9KaWEiOnsiRGF0YVRleHRGaWVsZCI6Ilpob25nV2VuIiwiRGF0YVZhbHVlRmllbGQiOiJaaG9uZ1dlbiIsIkZfSXRlbXMiOltbIi0xIiwi6YCJ5oup5Zu95a62IiwxLCIiLCIiXSxbIumYv+WwlOW3tOWwvOS6miIsIumYv+WwlOW3tOWwvOS6miIsMSwiIiwiIl0sWyLpmL/lsJTlj4rliKnkupoiLCLpmL/lsJTlj4rliKnkupoiLDEsIiIsIiJdLFsi6Zi/5a+M5rGXIiwi6Zi/5a+M5rGXIiwxLCIiLCIiXSxbIumYv+agueW7tyIsIumYv+agueW7tyIsMSwiIiwiIl0sWyLpmL/mi4nkvK/ogZTlkIjphYvplb/lm70iLCLpmL/mi4nkvK/ogZTlkIjphYvplb/lm70iLDEsIiIsIiJdLFsi6Zi/6bKB5be0Iiwi6Zi/6bKB5be0IiwxLCIiLCIiXSxbIumYv+abvCIsIumYv+abvCIsMSwiIiwiIl0sWyLpmL/loZ7mi5znloYiLCLpmL/loZ7mi5znloYiLDEsIiIsIiJdLFsi5Z+D5Y+KIiwi5Z+D5Y+KIiwxLCIiLCIiXSxbIuWfg+WhnuS/hOavlOS6miIsIuWfg+WhnuS/hOavlOS6miIsMSwiIiwiIl0sWyLniLHlsJTlhbAiLCLniLHlsJTlhbAiLDEsIiIsIiJdLFsi54ix5rKZ5bC85LqaIiwi54ix5rKZ5bC85LqaIiwxLCIiLCIiXSxbIuWuiemBk+WwlCIsIuWuiemBk+WwlCIsMSwiIiwiIl0sWyLlronlk6Xmi4kiLCLlronlk6Xmi4kiLDEsIiIsIiJdLFsi5a6J5Zyt5ouJIiwi5a6J5Zyt5ouJIiwxLCIiLCIiXSxbIuWuieaPkOeTnOWSjOW3tOW4g+i+viIsIuWuieaPkOeTnOWSjOW3tOW4g+i+viIsMSwiIiwiIl0sWyLlpaXlnLDliKkiLCLlpaXlnLDliKkiLDEsIiIsIiJdLFsi5aWl5YWw576k5bKbIiwi5aWl5YWw576k5bKbIiwxLCIiLCIiXSxbIua+s+Wkp+WIqeS6miIsIua+s+Wkp+WIqeS6miIsMSwiIiwiIl0sWyLlt7Tlt7TlpJrmlq8iLCLlt7Tlt7TlpJrmlq8iLDEsIiIsIiJdLFsi5be05biD5Lqa5paw5Yeg5YaF5LqaIiwi5be05biD5Lqa5paw5Yeg5YaF5LqaIiwxLCIiLCIiXSxbIuW3tOWTiOmprCIsIuW3tOWTiOmprCIsMSwiIiwiIl0sWyLlt7Tln7rmlq/lnaYiLCLlt7Tln7rmlq/lnaYiLDEsIiIsIiJdLFsi5be05YuS5pav5Z2mIiwi5be05YuS5pav5Z2mIiwxLCIiLCIiXSxbIuW3tOaelyIsIuW3tOaelyIsMSwiIiwiIl0sWyLlt7Tmi7/pqawiLCLlt7Tmi7/pqawiLDEsIiIsIiJdLFsi5be06KW/Iiwi5be06KW/IiwxLCIiLCIiXSxbIueZveS/hOe9l+aWryIsIueZveS/hOe9l+aWryIsMSwiIiwiIl0sWyLnmb7mhZXlpKciLCLnmb7mhZXlpKciLDEsIiIsIiJdLFsi5L+d5Yqg5Yip5LqaIiwi5L+d5Yqg5Yip5LqaIiwxLCIiLCIiXSxbIui0neWugSIsIui0neWugSIsMSwiIiwiIl0sWyLmr5TliKnml7YiLCLmr5TliKnml7YiLDEsIiIsIiJdLFsi5Yaw5bKbIiwi5Yaw5bKbIiwxLCIiLCIiXSxbIuazouWkmum7juWQhCIsIuazouWkmum7juWQhCIsMSwiIiwiIl0sWyLms6LlhbAiLCLms6LlhbAiLDEsIiIsIiJdLFsi5rOi5pav5bC85Lqa5ZKM6buR5aGe5ZOl57u06YKjIiwi5rOi5pav5bC85Lqa5ZKM6buR5aGe5ZOl57u06YKjIiwxLCIiLCIiXSxbIueOu+WIqee7tOS6miIsIueOu+WIqee7tOS6miIsMSwiIiwiIl0sWyLkvK/liKnlhbkiLCLkvK/liKnlhbkiLDEsIiIsIiJdLFsi5Y2a6Iyo55Om57qzIiwi5Y2a6Iyo55Om57qzIiwxLCIiLCIiXSxbIuS4jeS4uSIsIuS4jeS4uSIsMSwiIiwiIl0sWyLluIPln7rnurPms5XntKIiLCLluIPln7rnurPms5XntKIiLDEsIiIsIiJdLFsi5biD6ZqG6L+qIiwi5biD6ZqG6L+qIiwxLCIiLCIiXSxbIuW4g+e7tOWymyIsIuW4g+e7tOWymyIsMSwiIiwiIl0sWyLmnJ3pspwiLCLmnJ3pspwiLDEsIiIsIiJdLFsi6LWk6YGT5Yeg5YaF5LqaIiwi6LWk6YGT5Yeg5YaF5LqaIiwxLCIiLCIiXSxbIuS4uem6piIsIuS4uem6piIsMSwiIiwiIl0sWyLlvrflm70iLCLlvrflm70iLDEsIiIsIiJdLFsi5Lic5bid5rG2Iiwi5Lic5bid5rG2IiwxLCIiLCIiXSxbIuS4nOW4neaxtiIsIuS4nOW4neaxtiIsMSwiIiwiIl0sWyLlpJrlk6UiLCLlpJrlk6UiLDEsIiIsIiJdLFsi5aSa57Gz5bC85YqgIiwi5aSa57Gz5bC85YqgIiwxLCIiLCIiXSxbIuS/hOe9l+aWr+iBlOmCpiIsIuS/hOe9l+aWr+iBlOmCpiIsMSwiIiwiIl0sWyLljoTnk5zlpJrlsJQiLCLljoTnk5zlpJrlsJQiLDEsIiIsIiJdLFsi5Y6E56uL54m56YeM5LqaIiwi5Y6E56uL54m56YeM5LqaIiwxLCIiLCIiXSxbIuazleWbvSIsIuazleWbvSIsMSwiIiwiIl0sWyLms5Xlm73lpKfpg73kvJoiLCLms5Xlm73lpKfpg73kvJoiLDEsIiIsIiJdLFsi5rOV572X576k5bKbIiwi5rOV572X576k5bKbIiwxLCIiLCIiXSxbIuazleWxnuazouWIqeWwvOilv+S6miIsIuazleWxnuazouWIqeWwvOilv+S6miIsMSwiIiwiIl0sWyLms5XlsZ7lnK3kuprpgqMiLCLms5XlsZ7lnK3kuprpgqMiLDEsIiIsIiJdLFsi5qK16JKC5YaIIiwi5qK16JKC5YaIIiwxLCIiLCIiXSxbIuiPsuW+i+WuviIsIuiPsuW+i+WuviIsMSwiIiwiIl0sWyLmlpDmtY4iLCLmlpDmtY4iLDEsIiIsIiJdLFsi6Iqs5YWwIiwi6Iqs5YWwIiwxLCIiLCIiXSxbIuS9m+W+l+inkiIsIuS9m+W+l+inkiIsMSwiIiwiIl0sWyLlhojmr5TkupoiLCLlhojmr5TkupoiLDEsIiIsIiJdLFsi5Yia5p6cIiwi5Yia5p6cIiwxLCIiLCIiXSxbIuWImuaenO+8iOmHke+8iSIsIuWImuaenO+8iOmHke+8iSIsMSwiIiwiIl0sWyLlk6XkvKbmr5TkupoiLCLlk6XkvKbmr5TkupoiLDEsIiIsIiJdLFsi5ZOl5pav6L6+6buO5YqgIiwi5ZOl5pav6L6+6buO5YqgIiwxLCIiLCIiXSxbIuagvOael+e6s+i+viIsIuagvOael+e6s+i+viIsMSwiIiwiIl0sWyLmoLzpsoHlkInkupoiLCLmoLzpsoHlkInkupoiLDEsIiIsIiJdLFsi5qC56KW/5bKbIiwi5qC56KW/5bKbIiwxLCIiLCIiXSxbIuWPpOW3tCIsIuWPpOW3tCIsMSwiIiwiIl0sWyLnk5zlvrfnvZfmma7lspsiLCLnk5zlvrfnvZfmma7lspsiLDEsIiIsIiJdLFsi5YWz5bKbIiwi5YWz5bKbIiwxLCIiLCIiXSxbIuWcreS6mumCoyIsIuWcreS6mumCoyIsMSwiIiwiIl0sWyLlk4jokKjlhYvmlq/lnaYiLCLlk4jokKjlhYvmlq/lnaYiLDEsIiIsIiJdLFsi5rW35ZywIiwi5rW35ZywIiwxLCIiLCIiXSxbIumfqeWbvSIsIumfqeWbvSIsMSwiIiwiIl0sWyLojbflhbAiLCLojbflhbAiLDEsIiIsIiJdLFsi6buR5bGxIiwi6buR5bGxIiwxLCIiLCIiXSxbIua0qumDveaLieaWryIsIua0qumDveaLieaWryIsMSwiIiwiIl0sWyLln7rph4zlt7Tmlq8iLCLln7rph4zlt7Tmlq8iLDEsIiIsIiJdLFsi5ZCJ5biD5o+QIiwi5ZCJ5biD5o+QIiwxLCIiLCIiXSxbIuWQieWwlOWQieaWr+aWr+WdpiIsIuWQieWwlOWQieaWr+aWr+WdpiIsMSwiIiwiIl0sWyLlh6DlhoXkupoiLCLlh6DlhoXkupoiLDEsIiIsIiJdLFsi5Yeg5YaF5Lqa5q+U57uNIiwi5Yeg5YaF5Lqa5q+U57uNIiwxLCIiLCIiXSxbIuWKoOaLv+WkpyIsIuWKoOaLv+WkpyIsMSwiIiwiIl0sWyLliqDnurMiLCLliqDnurMiLDEsIiIsIiJdLFsi5Yqg6JOsIiwi5Yqg6JOsIiwxLCIiLCIiXSxbIuafrOWflOWvqCIsIuafrOWflOWvqCIsMSwiIiwiIl0sWyLmjbflhYsiLCLmjbflhYsiLDEsIiIsIiJdLFsi5rSl5be05biD6Z+mIiwi5rSl5be05biD6Z+mIiwxLCIiLCIiXSxbIuWWgOm6pumahiIsIuWWgOm6pumahiIsMSwiIiwiIl0sWyLljaHloZTlsJQiLCLljaHloZTlsJQiLDEsIiIsIiJdLFsi56eR56eR5pav77yI5Z+65p6X77yJ576k5bKbIiwi56eR56eR5pav77yI5Z+65p6X77yJ576k5bKbIiwxLCIiLCIiXSxbIuenkeaRqee9lyIsIuenkeaRqee9lyIsMSwiIiwiIl0sWyLnp5Hnibnov6rnk6YiLCLnp5Hnibnov6rnk6YiLDEsIiIsIiJdLFsi56eR5aiB54m5Iiwi56eR5aiB54m5IiwxLCIiLCIiXSxbIuWFi+e9l+WcsOS6miIsIuWFi+e9l+WcsOS6miIsMSwiIiwiIl0sWyLogq/lsLzkupoiLCLogq/lsLzkupoiLDEsIiIsIiJdLFsi5bqT5YWL576k5bKbIiwi5bqT5YWL576k5bKbIiwxLCIiLCIiXSxbIuaLieiEsee7tOS6miIsIuaLieiEsee7tOS6miIsMSwiIiwiIl0sWyLojrHntKLmiZgiLCLojrHntKLmiZgiLDEsIiIsIiJdLFsi6ICB5oydIiwi6ICB5oydIiwxLCIiLCIiXSxbIum7juW3tOWrqSIsIum7juW3tOWrqSIsMSwiIiwiIl0sWyLnq4vpmbblrpsiLCLnq4vpmbblrpsiLDEsIiIsIiJdLFsi5Yip5q+U6YeM5LqaIiwi5Yip5q+U6YeM5LqaIiwxLCIiLCIiXSxbIuWIqeavlOS6miIsIuWIqeavlOS6miIsMSwiIiwiIl0sWyLliJfmlK/mlablo6vnmbsiLCLliJfmlK/mlablo6vnmbsiLDEsIiIsIiJdLFsi55WZ5bC85rGq5bKbIiwi55WZ5bC85rGq5bKbIiwxLCIiLCIiXSxbIuWNouajruWgoSIsIuWNouajruWgoSIsMSwiIiwiIl0sWyLljaLml7rovr4iLCLljaLml7rovr4iLDEsIiIsIiJdLFsi572X6ams5bC85LqaIiwi572X6ams5bC85LqaIiwxLCIiLCIiXSxbIumprOi+vuWKoOaWr+WKoCIsIumprOi+vuWKoOaWr+WKoCIsMSwiIiwiIl0sWyLpqazmganlspsiLCLpqazmganlspsiLDEsIiIsIiJdLFsi6ams5bCU5Luj5aSrIiwi6ams5bCU5Luj5aSrIiwxLCIiLCIiXSxbIumprOiAs+S7liIsIumprOiAs+S7liIsMSwiIiwiIl0sWyLpqazmi4nnu7QiLCLpqazmi4nnu7QiLDEsIiIsIiJdLFsi6ams5p2l6KW/5LqaIiwi6ams5p2l6KW/5LqaIiwxLCIiLCIiXSxbIumprOmHjCIsIumprOmHjCIsMSwiIiwiIl0sWyLpqazlhbbpob8iLCLpqazlhbbpob8iLDEsIiIsIiJdLFsi6ams57uN5bCU576k5bKbIiwi6ams57uN5bCU576k5bKbIiwxLCIiLCIiXSxbIumprOaPkOWwvOWFi+WymyIsIumprOaPkOWwvOWFi+WymyIsMSwiIiwiIl0sWyLpqaznuqbnibkiLCLpqaznuqbnibkiLDEsIiIsIiJdLFsi5q+b6YeM5rGC5pavIiwi5q+b6YeM5rGC5pavIiwxLCIiLCIiXSxbIuavm+mHjOWhlOWwvOS6miIsIuavm+mHjOWhlOWwvOS6miIsMSwiIiwiIl0sWyLnvo7lm70iLCLnvo7lm70iLDEsIiIsIiJdLFsi576O5bGe6JCo5pGp5LqaIiwi576O5bGe6JCo5pGp5LqaIiwxLCIiLCIiXSxbIuiSmeWPpCIsIuiSmeWPpCIsMSwiIiwiIl0sWyLokpnnibnloZ7mi4nnibkiLCLokpnnibnloZ7mi4nnibkiLDEsIiIsIiJdLFsi5a2f5Yqg5ouJIiwi5a2f5Yqg5ouJIiwxLCIiLCIiXSxbIuenmOmygSIsIuenmOmygSIsMSwiIiwiIl0sWyLlr4blhYvnvZflsLzopb/kupoiLCLlr4blhYvnvZflsLzopb/kupoiLDEsIiIsIiJdLFsi57yF55S4Iiwi57yF55S4IiwxLCIiLCIiXSxbIuaRqeWwlOWkmueTpiIsIuaRqeWwlOWkmueTpiIsMSwiIiwiIl0sWyLmkanmtJvlk6UiLCLmkanmtJvlk6UiLDEsIiIsIiJdLFsi5pGp57qz5ZOlIiwi5pGp57qz5ZOlIiwxLCIiLCIiXSxbIuiOq+ahkeavlOWFiyIsIuiOq+ahkeavlOWFiyIsMSwiIiwiIl0sWyLloqjopb/lk6UiLCLloqjopb/lk6UiLDEsIiIsIiJdLFsi57qz57Gz5q+U5LqaIiwi57qz57Gz5q+U5LqaIiwxLCIiLCIiXSxbIuWNl+mdniIsIuWNl+mdniIsMSwiIiwiIl0sWyLljZfmlq/mi4nlpKsiLCLljZfmlq/mi4nlpKsiLDEsIiIsIiJdLFsi55GZ6bKBIiwi55GZ6bKBIiwxLCIiLCIiXSxbIuWwvOaziuWwlCIsIuWwvOaziuWwlCIsMSwiIiwiIl0sWyLlsLzliqDmi4nnk5wiLCLlsLzliqDmi4nnk5wiLDEsIiIsIiJdLFsi5bC85pel5bCUIiwi5bC85pel5bCUIiwxLCIiLCIiXSxbIuWwvOaXpeWIqeS6miIsIuWwvOaXpeWIqeS6miIsMSwiIiwiIl0sWyLnur3ln4MiLCLnur3ln4MiLDEsIiIsIiJdLFsi5oyq5aiBIiwi5oyq5aiBIiwxLCIiLCIiXSxbIuivuuemj+WFi+WymyIsIuivuuemj+WFi+WymyIsMSwiIiwiIl0sWyLluJXlirMiLCLluJXlirMiLDEsIiIsIiJdLFsi55qu54m55Yev5oGp576k5bKbIiwi55qu54m55Yev5oGp576k5bKbIiwxLCIiLCIiXSxbIuiRoeiQhOeJmSIsIuiRoeiQhOeJmSIsMSwiIiwiIl0sWyLml6XmnKwiLCLml6XmnKwiLDEsIiIsIiJdLFsi55Ge5YW4Iiwi55Ge5YW4IiwxLCIiLCIiXSxbIueRnuWjqyIsIueRnuWjqyIsMSwiIiwiIl0sWyLokKjlsJTnk6blpJoiLCLokKjlsJTnk6blpJoiLDEsIiIsIiJdLFsi6JCo5pGp5LqaIiwi6JCo5pGp5LqaIiwxLCIiLCIiXSxbIuWhnuWwlOe7tOS6miIsIuWhnuWwlOe7tOS6miIsMSwiIiwiIl0sWyLloZ7mi4nliKnmmIIiLCLloZ7mi4nliKnmmIIiLDEsIiIsIiJdLFsi5aGe5YaF5Yqg5bCUIiwi5aGe5YaF5Yqg5bCUIiwxLCIiLCIiXSxbIuWhnua1pui3r+aWryIsIuWhnua1pui3r+aWryIsMSwiIiwiIl0sWyLloZ7oiIzlsJQiLCLloZ7oiIzlsJQiLDEsIiIsIiJdLFsi5rKZ54m56Zi/5ouJ5LyvIiwi5rKZ54m56Zi/5ouJ5LyvIiwxLCIiLCIiXSxbIuWco+ivnuWymyIsIuWco+ivnuWymyIsMSwiIiwiIl0sWyLlnKPlpJrnvo7lkozmma7mnpfopb/mr5QiLCLlnKPlpJrnvo7lkozmma7mnpfopb/mr5QiLDEsIiIsIiJdLFsi5Zyj6LWr5YuS5ou/Iiwi5Zyj6LWr5YuS5ou/IiwxLCIiLCIiXSxbIuWco+WfuuiMqOWSjOWwvOe7tOaWryIsIuWco+WfuuiMqOWSjOWwvOe7tOaWryIsMSwiIiwiIl0sWyLlnKPljaLopb/kupoiLCLlnKPljaLopb/kupoiLDEsIiIsIiJdLFsi5Zyj6ams5Yqb6K+6Iiwi5Zyj6ams5Yqb6K+6IiwxLCIiLCIiXSxbIuWco+aWh+ajrueJueWSjOagvOael+e6s+S4geaWryIsIuWco+aWh+ajrueJueWSjOagvOael+e6s+S4geaWryIsMSwiIiwiIl0sWyLmlq/ph4zlhbDljaEiLCLmlq/ph4zlhbDljaEiLDEsIiIsIiJdLFsi5pav5rSb5LyQ5YWLIiwi5pav5rSb5LyQ5YWLIiwxLCIiLCIiXSxbIuaWr+a0m+aWh+WwvOS6miIsIuaWr+a0m+aWh+WwvOS6miIsMSwiIiwiIl0sWyLmlq/lqIHlo6vlhbAiLCLmlq/lqIHlo6vlhbAiLDEsIiIsIiJdLFsi6IuP5Li5Iiwi6IuP5Li5IiwxLCIiLCIiXSxbIuiLj+mHjOWNlyIsIuiLj+mHjOWNlyIsMSwiIiwiIl0sWyLmiYDnvZfpl6jnvqTlspsiLCLmiYDnvZfpl6jnvqTlspsiLDEsIiIsIiJdLFsi57Si6ams6YeMIiwi57Si6ams6YeMIiwxLCIiLCIiXSxbIuWhlOWQieWFi+aWr+WdpiIsIuWhlOWQieWFi+aWr+WdpiIsMSwiIiwiIl0sWyLms7Dlm70iLCLms7Dlm70iLDEsIiIsIiJdLFsi5Z2m5qGR5bC85LqaIiwi5Z2m5qGR5bC85LqaIiwxLCIiLCIiXSxbIuaxpOWKoCIsIuaxpOWKoCIsMSwiIiwiIl0sWyLnibnnq4vlsLzovr7lkozlpJrlt7Tlk6UiLCLnibnnq4vlsLzovr7lkozlpJrlt7Tlk6UiLDEsIiIsIiJdLFsi56qB5bC85pavIiwi56qB5bC85pavIiwxLCIiLCIiXSxbIuWbvueTpuWNoiIsIuWbvueTpuWNoiIsMSwiIiwiIl0sWyLlnJ/ogLPlhbYiLCLlnJ/ogLPlhbYiLDEsIiIsIiJdLFsi5Zyf5bqT5pu85pav5Z2mIiwi5Zyf5bqT5pu85pav5Z2mIiwxLCIiLCIiXSxbIuaJmOWFi+WKsyIsIuaJmOWFi+WKsyIsMSwiIiwiIl0sWyLnk6bliKnmlq/nvqTlspvlkozlr4zlm77nurPnvqTlspsiLCLnk6bliKnmlq/nvqTlspvlkozlr4zlm77nurPnvqTlspsiLDEsIiIsIiJdLFsi55Om5Yqq6Zi/5Zu+Iiwi55Om5Yqq6Zi/5Zu+IiwxLCIiLCIiXSxbIuWNseWcsOmprOaLiSIsIuWNseWcsOmprOaLiSIsMSwiIiwiIl0sWyLlp5TlhoXnkZ7mi4kiLCLlp5TlhoXnkZ7mi4kiLDEsIiIsIiJdLFsi5paH6I6xIiwi5paH6I6xIiwxLCIiLCIiXSxbIuS5jOW5sui+viIsIuS5jOW5sui+viIsMSwiIiwiIl0sWyLkuYzlhYvlhbAiLCLkuYzlhYvlhbAiLDEsIiIsIiJdLFsi5LmM5ouJ5ZytIiwi5LmM5ouJ5ZytIiwxLCIiLCIiXSxbIuS5jOWFueWIq+WFi+aWr+WdpiIsIuS5jOWFueWIq+WFi+aWr+WdpiIsMSwiIiwiIl0sWyLopb/nj63niZkiLCLopb/nj63niZkiLDEsIiIsIiJdLFsi6KW/5pKS5ZOI5ouJIiwi6KW/5pKS5ZOI5ouJIiwxLCIiLCIiXSxbIuW4jOiFiiIsIuW4jOiFiiIsMSwiIiwiIl0sWyLmlrDliqDlnaEiLCLmlrDliqDlnaEiLDEsIiIsIiJdLFsi5paw5ZaA6YeM5aSa5bC85LqaIiwi5paw5ZaA6YeM5aSa5bC85LqaIiwxLCIiLCIiXSxbIuaWsOilv+WFsCIsIuaWsOilv+WFsCIsMSwiIiwiIl0sWyLljIjniZnliKkiLCLljIjniZnliKkiLDEsIiIsIiJdLFsi5Y+Z5Yip5LqaIiwi5Y+Z5Yip5LqaIiwxLCIiLCIiXSxbIueJmeS5sOWKoCIsIueJmeS5sOWKoCIsMSwiIiwiIl0sWyLkuprnvo7lsLzkupoiLCLkuprnvo7lsLzkupoiLDEsIiIsIiJdLFsi5Lmf6ZeoIiwi5Lmf6ZeoIiwxLCIiLCIiXSxbIuS8iuaLieWFiyIsIuS8iuaLieWFiyIsMSwiIiwiIl0sWyLkvIrmnJciLCLkvIrmnJciLDEsIiIsIiJdLFsi5Lul6Imy5YiXIiwi5Lul6Imy5YiXIiwxLCIiLCIiXSxbIuaEj+Wkp+WIqSIsIuaEj+Wkp+WIqSIsMSwiIiwiIl0sWyLljbDluqYiLCLljbDluqYiLDEsIiIsIiJdLFsi5Y2w5bqm5bC86KW/5LqaIiwi5Y2w5bqm5bC86KW/5LqaIiwxLCIiLCIiXSxbIuiLseWbvSIsIuiLseWbvSIsMSwiIiwiIl0sWyLnuqbml6YiLCLnuqbml6YiLDEsIiIsIiJdLFsi6LaK5Y2XIiwi6LaK5Y2XIiwxLCIiLCIiXSxbIui1nuavlOS6miIsIui1nuavlOS6miIsMSwiIiwiIl0sWyLms73opb/lspsiLCLms73opb/lspsiLDEsIiIsIiJdLFsi5LmN5b6XIiwi5LmN5b6XIiwxLCIiLCIiXSxbIuebtOW4g+e9l+mZgCIsIuebtOW4g+e9l+mZgCIsMSwiIiwiIl0sWyLmmbrliKkiLCLmmbrliKkiLDEsIiIsIiJdLFsi5Lit6Z2eIiwi5Lit6Z2eIiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyItMSJdfSwicDFfU2hpRlNIIjp7IlJlcXVpcmVkIjp0cnVlLCJIaWRkZW4iOmZhbHNlLCJTZWxlY3RlZFZhbHVlIjoi5pivIiwiRl9JdGVtcyI6W1si5pivIiwi5Zyo5LiK5rW3IiwxXSxbIuWQpiIsIuS4jeWcqOS4iua1tyIsMV1dfSwicDFfU2hpRlpYIjp7IlJlcXVpcmVkIjp0cnVlLCJIaWRkZW4iOmZhbHNlLCJTZWxlY3RlZFZhbHVlIjoi5ZCmIiwiRl9JdGVtcyI6W1si5pivIiwi5L2P5qChIiwxXSxbIuWQpiIsIuS4jeS9j+agoSIsMV1dfSwicDFfZGRsU2hlbmciOnsiSGlkZGVuIjpmYWxzZSwiRl9JdGVtcyI6W1siLTEiLCLpgInmi6nnnIHku70iLDEsIiIsIiJdLFsi5YyX5LqsIiwi5YyX5LqsIiwxLCIiLCIiXSxbIuWkqea0pSIsIuWkqea0pSIsMSwiIiwiIl0sWyLkuIrmtbciLCLkuIrmtbciLDEsIiIsIiJdLFsi6YeN5bqGIiwi6YeN5bqGIiwxLCIiLCIiXSxbIuays+WMlyIsIuays+WMlyIsMSwiIiwiIl0sWyLlsbHopb8iLCLlsbHopb8iLDEsIiIsIiJdLFsi6L695a6BIiwi6L695a6BIiwxLCIiLCIiXSxbIuWQieaelyIsIuWQieaelyIsMSwiIiwiIl0sWyLpu5HpvpnmsZ8iLCLpu5HpvpnmsZ8iLDEsIiIsIiJdLFsi5rGf6IuPIiwi5rGf6IuPIiwxLCIiLCIiXSxbIua1meaxnyIsIua1meaxnyIsMSwiIiwiIl0sWyLlronlvr0iLCLlronlvr0iLDEsIiIsIiJdLFsi56aP5bu6Iiwi56aP5bu6IiwxLCIiLCIiXSxbIuaxn+ilvyIsIuaxn+ilvyIsMSwiIiwiIl0sWyLlsbHkuJwiLCLlsbHkuJwiLDEsIiIsIiJdLFsi5rKz5Y2XIiwi5rKz5Y2XIiwxLCIiLCIiXSxbIua5luWMlyIsIua5luWMlyIsMSwiIiwiIl0sWyLmuZbljZciLCLmuZbljZciLDEsIiIsIiJdLFsi5bm/5LicIiwi5bm/5LicIiwxLCIiLCIiXSxbIua1t+WNlyIsIua1t+WNlyIsMSwiIiwiIl0sWyLlm5vlt50iLCLlm5vlt50iLDEsIiIsIiJdLFsi6LS15beeIiwi6LS15beeIiwxLCIiLCIiXSxbIuS6keWNlyIsIuS6keWNlyIsMSwiIiwiIl0sWyLpmZXopb8iLCLpmZXopb8iLDEsIiIsIiJdLFsi55SY6IKDIiwi55SY6IKDIiwxLCIiLCIiXSxbIumdkua1tyIsIumdkua1tyIsMSwiIiwiIl0sWyLlhoXokpnlj6QiLCLlhoXokpnlj6QiLDEsIiIsIiJdLFsi5bm/6KW/Iiwi5bm/6KW/IiwxLCIiLCIiXSxbIuilv+iXjyIsIuilv+iXjyIsMSwiIiwiIl0sWyLlroHlpI8iLCLlroHlpI8iLDEsIiIsIiJdLFsi5paw55aGIiwi5paw55aGIiwxLCIiLCIiXSxbIummmea4ryIsIummmea4ryIsMSwiIiwiIl0sWyLmvrPpl6giLCLmvrPpl6giLDEsIiIsIiJdLFsi5Y+w5rm+Iiwi5Y+w5rm+IiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyLkuIrmtbciXX0sInAxX2RkbFNoaSI6eyJIaWRkZW4iOmZhbHNlLCJFbmFibGVkIjp0cnVlLCJGX0l0ZW1zIjpbWyItMSIsIumAieaLqeW4giIsMSwiIiwiIl0sWyLkuIrmtbfluIIiLCLkuIrmtbfluIIiLDEsIiIsIiJdXSwiU2VsZWN0ZWRWYWx1ZUFycmF5IjpbIuS4iua1t+W4giJdfSwicDFfZGRsWGlhbiI6eyJIaWRkZW4iOmZhbHNlLCJFbmFibGVkIjp0cnVlLCJGX0l0ZW1zIjpbWyItMSIsIumAieaLqeWOv+WMuiIsMSwiIiwiIl0sWyLpu4TmtabljLoiLCLpu4TmtabljLoiLDEsIiIsIiJdLFsi5Y2i5rm+5Yy6Iiwi5Y2i5rm+5Yy6IiwxLCIiLCIiXSxbIuW+kOaxh+WMuiIsIuW+kOaxh+WMuiIsMSwiIiwiIl0sWyLplb/lroHljLoiLCLplb/lroHljLoiLDEsIiIsIiJdLFsi6Z2Z5a6J5Yy6Iiwi6Z2Z5a6J5Yy6IiwxLCIiLCIiXSxbIuaZrumZgOWMuiIsIuaZrumZgOWMuiIsMSwiIiwiIl0sWyLombnlj6PljLoiLCLombnlj6PljLoiLDEsIiIsIiJdLFsi5p2o5rWm5Yy6Iiwi5p2o5rWm5Yy6IiwxLCIiLCIiXSxbIuWuneWxseWMuiIsIuWuneWxseWMuiIsMSwiIiwiIl0sWyLpl7XooYzljLoiLCLpl7XooYzljLoiLDEsIiIsIiJdLFsi5ZiJ5a6a5Yy6Iiwi5ZiJ5a6a5Yy6IiwxLCIiLCIiXSxbIuadvuaxn+WMuiIsIuadvuaxn+WMuiIsMSwiIiwiIl0sWyLph5HlsbHljLoiLCLph5HlsbHljLoiLDEsIiIsIiJdLFsi6Z2S5rWm5Yy6Iiwi6Z2S5rWm5Yy6IiwxLCIiLCIiXSxbIuWliei0pOWMuiIsIuWliei0pOWMuiIsMSwiIiwiIl0sWyLmtabkuJzmlrDljLoiLCLmtabkuJzmlrDljLoiLDEsIiIsIiJdLFsi5bSH5piO5Yy6Iiwi5bSH5piO5Yy6IiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyLlrp3lsbHljLoiXX0sInAxX1hpYW5nWERaIjp7IkhpZGRlbiI6ZmFsc2UsIkxhYmVsIjoi5Zu95YaF6K+m57uG5Zyw5Z2A77yI55yB5biC5Yy65Y6/5peg6ZyA6YeN5aSN5aGr5YaZ77yJIiwiVGV4dCI6IjExIn0sInAxX0NvbnRlbnRQYW5lbDFfWmhvbmdHRlhEUSI6eyJUZXh0IjoiPHNwYW4gc3R5bGU9J2NvbG9yOnJlZDsnPumrmOmjjumZqeWcsOWMuu+8mjxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guiXgeWfjuWMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guaWsOS5kOW4gjxici8+XHJcbuays+WMl+ecgemCouWPsOW4guWNl+Wuq+W4gjxici8+XHJcbum7kem+meaxn+ecgee7peWMluW4guacm+WljuWOvzxici8+XHJcbuWQieael+ecgemAmuWMluW4guS4nOaYjOWMujxici8+XHJcbuWMl+S6rOW4guWkp+WFtOWMuuWkqeWuq+mZouihl+mBk+iejeaxh+ekvuWMujxici8+XHJcbjxici8+XHJcbuS4remjjumZqeWcsOWMuu+8mjxici8+XHJcbuWMl+S6rOW4gumhuuS5ieWMuuWMl+efs+anvemVh+ilv+i1teWQhOW6hOadkTxici8+XHJcbuWMl+S6rOW4gumhuuS5ieWMuuWMl+efs+anvemVh+WMl+efs+anveadkTxici8+XHJcbuWMl+S6rOW4gumhuuS5ieWMuui1teWFqOiQpemVh+iBlOW6hOadkTxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4gumrmOaWsOWMuui1teadkeaWsOWMuuWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4gumrmOaWsOWMuuS4u+ivreWfjuWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guaXoOaegeWOv+S4nOWMl+i/nOadkTxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guaXoOaegeWOv+ilv+mDneW6hOadkTxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guato+WumuWOv+epuua4r+iKseWbreWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guato+WumuWOv+WtlOadkTxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guaWsOWNjuWMuumDveW4gumYs+WFieWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guaWsOWNjuWMuuS4vemDveays+eVlOWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guahpeilv+WMuuW5s+WuieWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guihjOWUkOWOv+a7qOays+Wwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guijleWNjuWMuuWkqea1t+iqieWkqeS4i+Wwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guijleWNjuWMuuaZtuW9qeiLkeWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guijleWNjuWMuuS8l+e+juW7iuahpeWbm+Wto0HljLo8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILoo5XljY7ljLrkuJzmlrnmmI7nj6DlsI/ljLo8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILmoaXopb/ljLrnmb3ph5Hlhazlr5M8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILmoaXopb/ljLrljY7mtqbkuIfosaHln448YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILpub/ms4nljLrop4Lls7DlmInpgrjlsI/ljLo8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILmraPlrprljr/lhq/lrrbluoTmnZE8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILmraPlrprljr/kuJzlubPkuZDmnZE8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILplb/lronljLrljZrpm4Xnm5vkuJblsI/ljLpF5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6ZW/5a6J5Yy65Zu96LWr57qi54+K5rm+5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6auY5paw5Yy65aSq6KGM5ZiJ6IuR5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6KOV5Y2O5Yy65Y2T5Lic5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6KOV5Y2O5Yy65paw5Y2O6IuR5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6bm/5rOJ5Yy66ZO25bGx6Iqx5Zut5paw5Yy65bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC5paw5Y2O5Yy65bCa6YeR6IuR5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6ZW/5a6J5Yy65YmN6L+b5p2RPGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6ZW/5a6J5Yy65pmu5ZKM5bCP5Yy65Y2X6ZmiPGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6ZW/5a6J5Yy65bu65piO5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6ZW/5a6J5Yy6566A562R5a625Zut5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6ZW/5a6J5Yy65L+d5Yip6Iqx5ZutQuWMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4gumVv+WuieWMuuS/neWIqeiKseWbrUTljLo8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILplb/lronljLrog7jnp5HljLvpmaLlhazlr5PljJfljLo8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILpq5jmlrDljLrlkIznpaXln47lsI/ljLpD5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6auY5paw5Yy65ZKM5ZCI576O5a625bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6KOV5Y2O5Yy65rW35aSp6Ziz5YWJ5Zut5bCP5Yy6PGJyLz5cclxu5rKz5YyX55yB55+z5a625bqE5biC6KOV5Y2O5Yy65Y2B5LqM5YyW5bu65bCP5Yy6MTblj7fmpbw8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILoo5XljY7ljLrljYHkuozljJblu7rlsI/ljLoxN+WPt+alvDxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guijleWNjuWMuuays+WMl+WfjuW7uuWtpuagoeWutuWxnumZojxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guagvuWfjuWMuuWNk+i+vuWkqumYs+WfjuW4jOacm+S5i+a0suWwj+WMujxici8+XHJcbuays+WMl+ecgeefs+WutuW6hOW4guW5s+WxseWOv+mYsueWq+ermeWwj+WMujxici8+XHJcbuays+WMl+ecgeW7iuWdiuW4guWbuuWuieWOv+iLseWbveWuqzXmnJ88YnIvPlxyXG7msrPljJfnnIHpgqLlj7DluILpmoblsKfljr/ng5/ojYnlrrblm63vvIjng5/ojYnlhazlj7jlrrblsZ7pmaLvvIk8YnIvPlxyXG7msrPljJfnnIHnn7PlrrbluoTluILotbXljr/ku7vluoTmnZE8YnIvPlxyXG7ovr3lroHnnIHlpKfov57luILph5Hmma7mlrDljLrlhYnkuK3ooZfpgZPog5zliKnopb/npL7ljLo8YnIvPlxyXG7ovr3lroHnnIHlpKfov57luILph5Hmma7mlrDljLrmi6XmlL/ooZfpgZPlj6Tln47nlLLljLo8YnIvPlxyXG7pu5HpvpnmsZ/nnIHlpKfluobluILpvpnlh6TljLrkuJbnuqrllJDkurrkuK3lv4PlsI/ljLoy5qCLMeWNleWFgzxici8+XHJcbum7kem+meaxn+ecgem9kOm9kOWTiOWwlOW4guaYguaYgua6quWMuuWkp+S6lOemj+eOm+adkTxici8+XHJcbum7kem+meaxn+ecgeWTiOWwlOa7qOW4gummmeWdiuWMuummmeWdiuWkp+ihl+ihl+mBk+WKnuS6i+WkhOmmmeS4reekvuWMuuWPpOmmmeihlzEy5Y+3PGJyLz5cclxu6buR6b6Z5rGf55yB5ZOI5bCU5ruo5biC6aaZ5Z2K5Yy65aSn5bqG6Lev6KGX6YGT5Yqe5LqL5aSE55S15aGU5bCP5Yy6MTAx5qCLN+WNleWFgzxici8+XHJcbum7kem+meaxn+ecgeWTiOWwlOa7qOW4gummmeWdiuWMuuWSjOW5s+i3r+ihl+mBk+WKnuS6i+WkhOmjjuWNjuekvuWMuuefs+WMluWwj+WMujnmoIs25Y2V5YWDPGJyLz5cclxu6buR6b6Z5rGf55yB5ZOI5bCU5ruo5biC5ZKM5bmz6Lev6KGX6YGT5Yqe5LqL5aSE5LiK5Lic56S+5Yy65LiH6LGh5LiK5Lic5bCP5Yy6ReagizLljZXlhYM8YnIvPlxyXG7lkInmnpfnnIHplb/mmKXluILlhazkuLvlsq3luILojIPlrrblsa/plYc8YnIvPlxyXG7lkInmnpfnnIHplb/mmKXluILnu7/lm63ljLrok4nmoaXlo7nlj7dD5Yy6PGJyLz5cclxu5ZCJ5p6X55yB6ZW/5pil5biC57u/5Zut5Yy65aSn56a55Y2O6YKmQuWMujxici8+XHJcbuWQieael+ecgemVv+aYpeW4guS6jOmBk+WMuumygei+ieWbvemZheWfjuiNt+WFsOWwj+mVh+Wwj+WMujxici8+XHJcbuWQieael+ecgemAmuWMluW4guWMu+iNr+mrmOaWsOWMuuWllei+vuWwj+WMujxici8+XHJcbuWQieael+ecgeadvuWOn+W4gue7j+a1juaKgOacr+W8gOWPkeWMuuaWsOWGnOWwj+WMujflj7fmpbw8YnIvPlxyXG7kuIrmtbfluILpu4TmtabljLrmmK3pgJrot6/lsYXmsJHljLrvvIjnpo/lt57ot6/ku6XljZfljLrln5/vvIk8L3NwYW4+In0sInAxX0NvbnRlbnRQYW5lbDEiOnsiSUZyYW1lQXR0cmlidXRlcyI6e319LCJwMV9GZW5nWERRREwiOnsiTGFiZWwiOiIwMeaciDEw5pel6IezMDHmnIgyNOaXpeaYr+WQpuWcqDxzcGFuIHN0eWxlPSdjb2xvcjpyZWQ7Jz7kuK3pq5jpo47pmanlnLDljLo8L3NwYW4+6YCX55WZIiwiU2VsZWN0ZWRWYWx1ZSI6IuWQpiIsIkZfSXRlbXMiOltbIuaYryIsIuaYryIsMV0sWyLlkKYiLCLlkKYiLDFdXX0sInAxX1RvbmdaV0RMSCI6eyJSZXF1aXJlZCI6dHJ1ZSwiTGFiZWwiOiLkuIrmtbflkIzkvY/kurrlkZjmmK/lkKbmnIkwMeaciDEw5pel6IezMDHmnIgyNOaXpeadpeiHqjxzcGFuIHN0eWxlPSdjb2xvcjpyZWQ7Jz7kuK3pq5jpo47pmanlnLDljLo8L3NwYW4+55qE5Lq6IiwiU2VsZWN0ZWRWYWx1ZSI6IuWQpiIsIkZfSXRlbXMiOltbIuaYryIsIuaYryIsMV0sWyLlkKYiLCLlkKYiLDFdXX0sInAxX0NlbmdGV0giOnsiTGFiZWwiOiIwMeaciDEw5pel6IezMDHmnIgyNOaXpeaYr+WQpuWcqDxzcGFuIHN0eWxlPSdjb2xvcjpyZWQ7Jz7kuK3pq5jpo47pmanlnLDljLo8L3NwYW4+6YCX55WZ6L+HIiwiRl9JdGVtcyI6W1si5pivIiwi5pivIiwxXSxbIuWQpiIsIuWQpiIsMV1dLCJTZWxlY3RlZFZhbHVlIjoi5ZCmIn0sInAxX0NlbmdGV0hfUmlRaSI6eyJIaWRkZW4iOnRydWV9LCJwMV9DZW5nRldIX0JlaVpodSI6eyJIaWRkZW4iOnRydWV9LCJwMV9KaWVDaHUiOnsiTGFiZWwiOiIwMeaciDEw5pel6IezMDHmnIgyNOaXpeaYr+WQpuS4juadpeiHqjxzcGFuIHN0eWxlPSdjb2xvcjpyZWQ7Jz7kuK3pq5jpo47pmanlnLDljLo8L3NwYW4+5Y+R54Ot5Lq65ZGY5a+G5YiH5o6l6KemIiwiU2VsZWN0ZWRWYWx1ZSI6IuWQpiIsIkZfSXRlbXMiOltbIuaYryIsIuaYryIsMV0sWyLlkKYiLCLlkKYiLDFdXX0sInAxX0ppZUNodV9SaVFpIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX0ppZUNodV9CZWlaaHUiOnsiSGlkZGVuIjp0cnVlfSwicDFfVHVKV0giOnsiTGFiZWwiOiIwMeaciDEw5pel6IezMDHmnIgyNOaXpeaYr+WQpuS5mOWdkOWFrOWFseS6pOmAmumAlOW+hDxzcGFuIHN0eWxlPSdjb2xvcjpyZWQ7Jz7kuK3pq5jpo47pmanlnLDljLo8L3NwYW4+IiwiU2VsZWN0ZWRWYWx1ZSI6IuWQpiIsIkZfSXRlbXMiOltbIuaYryIsIuaYryIsMV0sWyLlkKYiLCLlkKYiLDFdXX0sInAxX1R1SldIX1JpUWkiOnsiSGlkZGVuIjp0cnVlfSwicDFfVHVKV0hfQmVpWmh1Ijp7IkhpZGRlbiI6dHJ1ZX0sInAxX1F1ZVpIWkpDIjp7IkZfSXRlbXMiOltbIuaYryIsIuaYryIsMSwiIiwiIl0sWyLlkKYiLCLlkKYiLDEsIiIsIiJdXSwiU2VsZWN0ZWRWYWx1ZUFycmF5IjpbIuWQpiJdfSwicDFfRGFuZ1JHTCI6eyJTZWxlY3RlZFZhbHVlIjoi5ZCmIiwiRl9JdGVtcyI6W1si5pivIiwi5pivIiwxXSxbIuWQpiIsIuWQpiIsMV1dfSwicDFfR2VMU00iOnsiSGlkZGVuIjp0cnVlLCJJRnJhbWVBdHRyaWJ1dGVzIjp7fX0sInAxX0dlTEZTIjp7IlJlcXVpcmVkIjpmYWxzZSwiSGlkZGVuIjp0cnVlLCJGX0l0ZW1zIjpbWyLlsYXlrrbpmpTnprsiLCLlsYXlrrbpmpTnprsiLDFdLFsi6ZuG5Lit6ZqU56a7Iiwi6ZuG5Lit6ZqU56a7IiwxXV0sIlNlbGVjdGVkVmFsdWUiOm51bGx9LCJwMV9HZUxEWiI6eyJIaWRkZW4iOnRydWV9LCJwMV9GYW5YUlEiOnsiSGlkZGVuIjp0cnVlfSwicDFfV2VpRkhZWSI6eyJIaWRkZW4iOnRydWV9LCJwMV9TaGFuZ0hKWkQiOnsiSGlkZGVuIjp0cnVlfSwicDFfSmlhUmVuIjp7IkxhYmVsIjoiMDHmnIgxMOaXpeiHszAx5pyIMjTml6XlrrbkurrmmK/lkKbmnInlj5Hng63nrYnnl4fnirYifSwicDFfSmlhUmVuX0JlaVpodSI6eyJIaWRkZW4iOnRydWV9LCJwMV9TdWlTTSI6eyJSZXF1aXJlZCI6dHJ1ZSwiU2VsZWN0ZWRWYWx1ZSI6Iue7v+iJsiIsIkZfSXRlbXMiOltbIue6ouiJsiIsIue6ouiJsiIsMV0sWyLpu4ToibIiLCLpu4ToibIiLDFdLFsi57u/6ImyIiwi57u/6ImyIiwxXV19LCJwMV9Mdk1hMTREYXlzIjp7IlJlcXVpcmVkIjp0cnVlLCJTZWxlY3RlZFZhbHVlIjoi5pivIiwiRl9JdGVtcyI6W1si5pivIiwi5pivIiwxXSxbIuWQpiIsIuWQpiIsMV1dfSwicDFfY3RsMDBfYnRuUmV0dXJuIjp7Ik9uQ2xpZW50Q2xpY2siOiJkb2N1bWVudC5sb2NhdGlvbi5ocmVmPScvRGVmYXVsdC5hc3B4JztyZXR1cm47In0sInAxIjp7IklGcmFtZUF0dHJpYnV0ZXMiOnt9fX0="
    p1_BaoSRQ = reportData["date"].replace(" ","")   #这报送网站的变量名属实有点秀
    p1_ddlSheng = reportData['sheng']
    p1_ddlShi = reportData['shi']
    p1_f_state_shi = reportData['F_State_Shi']
    p1_ddlXian =  reportData['xian']
    p1_f_state_xian = reportData['F_State_Xian']
    p1_XiangXDZ = reportData["location"]
    F_State_Former_str = str(base64.b64decode(F_STATE_Former), encoding='utf-8')
    F_STATE_Former_dict = json.loads(F_State_Former_str)
    F_STATE_Former_dict['p1_BaoSRQ'].update({'Text': p1_BaoSRQ})
    F_STATE_Former_dict['p1_ddlSheng'].update({'SelectedValueArray':[p1_ddlSheng]})
    F_STATE_Former_dict['p1_ddlShi'].update({'SelectedValueArray':[p1_ddlShi ],'F_Items':p1_f_state_shi })
    F_STATE_Former_dict['p1_ddlXian'].update({'SelectedValueArray':[p1_ddlXian] ,'F_Items':p1_f_state_xian })
    F_STATE_Former_dict['p1_XiangXDZ'].update({'Text':p1_XiangXDZ})
    F_State_New_str = json.dumps(F_STATE_Former_dict, ensure_ascii=False, separators=(',', ':'))
    F_State_New=base64.b64encode(F_State_New_str.encode("utf-8")).decode()
   # print(  F_State_New)
    return F_State_New


def main(cookie,location): #location没啥用
    timeUTC = datetime.datetime.utcnow()
    timeLocal = timeUTC + datetime.timedelta(hours=8)
    date = timeLocal.strftime('%Y - %m - %d')
    reportUrl = "https://selfreport.shu.edu.cn/DayReport.aspx"
    response = requests.get(reportUrl, cookies=cookie)
    #print(response.text)
    LastInformation= re.findall("\"SelectedValueArray\":\[\"(.*?)\"", response.text)     #获取上次报送信息
   # print(LastInformation)
    Sheng = LastInformation[1]          #省
    Shi = LastInformation[2]            #市
    Xian = LastInformation[3]           #县
    #detailedLocation = re.findall("\"国内详细地址（省市区县无需重复填写）\",\"Text\":\"(.*?)\"", response.text)[0]
    detailedLocation = re.findall("\"Text\":\"(.*?)\"", response.text)[1]
    # for a in re.findall("\"F_Items\":(.*?),\"SelectedValueArray\"", response.text):
    #     print(a)
    # print(re.findall("\"F_Items\":(.*?),\"SelectedValueArray\"", response.text)[8])
    F_State_List =  re.findall("\"F_Items\":(.*?),\"SelectedValueArray\"", response.text)
    F_State_Shi = json.loads( re.findall("\"F_Items\":(.*?),\"SelectedValueArray\"", response.text)[8])
    F_State_Xian = json.loads(re.findall("\"F_Items\":(.*?),\"SelectedValueArray\"", response.text)[9])
    #print(Sheng, Shi, Xian, detailedLocation, F_State_Shi, F_State_Xian)
    reportData = {"date": date,
                "campusLocation": "宝山", "location": detailedLocation, "sheng": Sheng, "shi": Shi,
                "xian": Xian, "F_State_Shi": F_State_Shi, "F_State_Xian": F_State_Xian}
    reportSuccess = daily_report(cookie, reportData)
    if (reportSuccess) == -1:
        print("报送失败")
    else:
        print("提交成功")


