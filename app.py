# -*- coding: utf-8 -*-

def sleepover(yyyy_mm_dd, hakbun, birth, de_code, locgbn="KW", reason='null'):
    import requests
    import json
    import time

    '''
    @Cookie 생성: 메인페이지에 접속하여 SCOUTER, JSESSIONID를 얻어온다.
    '''
    url = "https://kw.happydorm.or.kr/00/0000.kmc"
    response = requests.get(url)

    cookiejar = response.cookies
    cookie_jsessionid = cookiejar.get_dict()['JSESSIONID']
    cookie_scouter = cookiejar.get_dict()['SCOUTER']

    cookies = {
        'SCOUTER': cookie_scouter,
        'JSESSIONID': cookie_jsessionid,
    }


    '''
    @로그인: 로그인 페이지에 접속하여 로그인을 한다.
    '''

    url = f"https://kw.happydorm.or.kr/00/login_list_sel.kmc?hakbun={hakbun}&birth={birth}&de_code={de_code}&locgbn={locgbn}"
    response = requests.get(url, cookies=cookies)

    '''
    @계정정보 확인: 올바르게 로그인 되었는지 확인한다.
    '''

    url = "https://kw.happydorm.or.kr/student/getIPSaHwakIn.kmc"
    data = {'locgbn': locgbn}

    response = requests.post(url, cookies=cookies, data=data)
    info_response = response.content.decode('utf-8')

    if "세션이 종료되었습니다.다시 로그인해 주세요." in info_response:
        return {"RESULT": False, "MESSAGE": "세션 오류"}
    else:
        infoJson = json.loads(info_response)
        print(infoJson["root"][0]["IPSaHwakIn"][0]["ps_kor_name"])  # 이름


    '''
    @외박신청: 외박신청 페이지에 접속하여 외박신청을 한다.
    '''

    headers = {
        'Host': 'kw.happydorm.or.kr',
        # 'Content-Length': '1317',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '""',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://kw.happydorm.or.kr',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynDWLwZIUPHFHOBkJ',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://kw.happydorm.or.kr/stayout/getStayoutWriteView.kmc?seq=&stayout_locgbn=KW&list_type=mypage&sl_gubun=NORMAL',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'close',
    }

    #yyyy_mm_dd = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    #yyyy_mm_dd = '2023-09-29'
    data = f'------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="list_type"\r\n\r\nmypage\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="seq"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="stayout_locgbn"\r\n\r\nKW\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_hakbun"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_univ"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_gubun"\r\n\r\nNORMAL\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_sdate1"\r\n\r\n{yyyy_mm_dd}\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_sdate2"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_sdate3"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_sdate4"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_sdate5"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_sdate6"\r\n\r\n\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ\r\nContent-Disposition: form-data; name="sl_content"\r\n\r\n{reason}\r\n------WebKitFormBoundarynDWLwZIUPHFHOBkJ--\r\n'

    response = requests.post(
        'https://kw.happydorm.or.kr/stayout/setStayout.kmc',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    setStayOutRspn = response.content.decode('utf-8')

    if f"{yyyy_mm_dd} : 중복 신청된 외박일자 입니다." in setStayOutRspn:
        return {"RESULT": False, "MESSAGE": "이미 신청한 외박일자입니다."}

    '''
    @외박신청 결과 확인: 외박신청 결과를 확인한다.
    '''
    url = "https://kw.happydorm.or.kr/stayout/getStayoutList.kmc"
    # cPage=1&rows=10&list_type=mypage&month=2023-08-29
    # 오늘 날짜를 today 변수에 yyyy-mm-dd 형식으로 저장
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    data = {'stayout_locgbn': 'KW', 'cPage': '1', 'rows': '10', 'list_type': 'mypage', 'month': today}

    response = requests.post(url, cookies=cookies, data=data)
    info_response = response.content.decode('utf-8')
    resultJson = json.loads(info_response)
    resultJsonList = resultJson["root"][0]["list"]

    resultCode = 0
    for item in resultJsonList:
        if item["sl_sdate"] == yyyy_mm_dd:
            resultCode = 1

    '''
    @로그아웃: 로그아웃을 한다.
    '''

    url = "https://kw.happydorm.or.kr/00/0000_logout.kmc"
    response = requests.get(url, cookies=cookies)
    ################# LOGOUT END

    if resultCode == 1:
        print("외박신청 성공!\n", resultJson)
        return {"RESULT": True, "MESSAGE": "외박신청에 성공했습니다.", "RSPN_JSON": resultJson}
    else:
        print("외박신청 실패!\n", resultJson)
        return {"RESULT": False, "MESSAGE": "외박신청에 실패했습니다.", "RSPN_JSON": resultJson}
