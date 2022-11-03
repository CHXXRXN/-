import requests
import os
import platform

pf = platform.platform()
url = 'https://oapi.saramin.co.kr/job-search?access-key=LAQUkCNCxMUvixl7nROFIO3NLClxI8OH2zJ4kRSIwN0PvsnedZm'

keyword = ""
lo = ""
business = ""
sBusiness = ""
workType = ""
eduType = ""


def startMyJob(k, sR1, sR2, sR3, b, sB, b2, sB2, wT1, wT2, edu):
    global keyword, lo, business, sBusiness, workType, eduType

    if sR1 == "서울 전체":
        sR1 = 101000

    elif sR1 == '경기 전체':
        sR1 = 102000

    elif sR1 == '인천 전체':
        sR1 = 108000

    elif sR1 == '부산 전체':

        sR1 = 106000

    elif sR1 == '대구 전체':
        sR1 = 104000

    elif sR1 == '대전 전체':
        sR1 = 105000

    elif sR1 == '울산 전체':
        sR1 = 107000

    elif sR1 == '세종 전체':
        sR1 = 118000

    elif sR1 == '강원 전체':
        sR1 = 109000

    elif sR1 == '경남 전체':
        sR1 = 110000

    elif sR1 == '경북 전체':
        sR1 = 111000

    elif sR1 == '전남 전체':
        sR1 = 112000

    elif sR1 == '전북 전체':
        sR1 = 113000

    elif sR1 == '충남 전체':
        sR1 = 115000

    elif sR1 == '충북 전체':
        sR1 = 114000

    elif sR1 == '제주 전체':
        sR1 = 116000

    elif sR1 == '강남구':
        sR1 = 101010

    elif sR1 == '강동구':
        sR1 = 101020

    elif sR1 == '강북구':
        sR1 = 101030

    elif sR1 == '강서구':
        sR1 = 101040

    elif sR1 == '관안구':
        sR1 = 101050

    elif sR1 == '광진구':
        sR1 = 101060

    elif sR1 == '구로구':
        sR1 = 101070

    elif sR1 == '금천구':
        sR1 = 101080

    elif sR1 == '노원구':
        sR1 = 101090

    elif sR1 == '도봉구':
        sR1 = 101100

    elif sR1 == '동대문구':
        sR1 = 101110

    elif sR1 == '동작구':
        sR1 = 101120

    elif sR1 == '마포구':
        sR1 = 101130

    elif sR1 == '서대문구':
        sR1 = 101140

    elif sR1 == '서초구':
        sR1 = 101150

    elif sR1 == '성동구':
        sR1 = 101160

    elif sR1 == '성북구':
        sR1 = 101170

    elif sR1 == '송파구':
        sR1 = 101180

    elif sR1 == '양천구':
        sR1 = 101190

    elif sR1 == '영등포구':
        sR1 = 101200

    elif sR1 == '용산구':
        sR1 = 101210

    elif sR1 == '은평구':
        sR1 = 101220

    elif sR1 == '종로구':
        sR1 = 101230

    elif sR1 == '중구':
        sR1 = 101240

    elif sR1 == '중랑구':
        sR1 = 101250

    elif sR1 == '가평군':
        sR1 = 102010

    elif sR1 == '고양시':
        sR1 = 102020

    elif sR1 == '고양시 덕양구':
        sR1 = 102030

    elif sR1 == '고양시 일산동구':
        sR1 = 102040

    elif sR1 == '고양시 일산서구':
        sR1 = 102050

    elif sR1 == '과천시':
        sR1 = 102060

    elif sR1 == '광명시':
        sR1 = 102070

    elif sR1 == '광주시':
        sR1 = 102080

    elif sR1 == '구리시':
        sR1 = 102090

    elif sR1 == '군포사':
        sR1 = 102100

    elif sR1 == '김포시':
        sR1 = 102110

    elif sR1 == '남양주시':
        sR1 = 102120

    elif sR1 == '동두천시':
        sR1 = 102130

    elif sR1 == '부천시':
        sR1 = 102140

    elif sR1 == '부천시 소사구':
        sR1 = 102150

    elif sR1 == '부천시 오정구':
        sR1 = 102160

    elif sR1 == '부천시 원미구':
        sR1 = 102170

    elif sR1 == '성남시':
        sR1 = 102180

    elif sR1 == '성남시 분당구':
        sR1 = 102190

    elif sR1 == '성남시 수정구':
        sR1 = 102200

    elif sR1 == '성남시 중원구':
        sR1 = 102210

    elif sR1 == '수원시':
        sR1 = 102220

    elif sR1 == '수원시 권선구':
        sR1 = 102230

    elif sR1 == '수원시 영통구':
        sR1 = 102240

    elif sR1 == '수원시 장안구':
        sR1 = 102250

    elif sR1 == '수원시 팔달구':
        sR1 = 102260

    elif sR1 == '시흥시':
        sR1 = 102270

    elif sR1 == '안산시':
        sR1 = 102280

    elif sR1 == '안산시 단원구':
        sR1 = 102290

    elif sR1 == '안산시 상록구':
        sR1 = 102300

    elif sR1 == '안성시':
        sR1 = 102310

    elif sR1 == '안양시':
        sR1 = 102320

    elif sR1 == '안양시 동안구':
        sR1 = 102330

    elif sR1 == '안양시 만안구':
        sR1 = 102340

    elif sR1 == '양주시':
        sR1 = 102350

    elif sR1 == '양평군':
        sR1 = 102360

    elif sR1 == '여주시':
        sR1 = 102370

    elif sR1 == '연천군':
        sR1 = 102380

    elif sR1 == '오산시':
        sR1 = 102390

    elif sR1 == '용인시':
        sR1 = 102400

    elif sR1 == '용인시 기흥구':
        sR1 = 102410

    elif sR1 == '용인시 수지구':
        sR1 = 102420

    elif sR1 == '용인시 처인구':
        sR1 = 102430

    elif sR1 == '의왕시':
        sR1 = 102440

    elif sR1 == '의정부시':
        sR1 = 102450

    elif sR1 == '이천시':
        sR1 = 102460

    elif sR1 == '파주시':
        sR1 = 102470

    elif sR1 == '평택시':
        sR1 = 102480

    elif sR1 == '포천시':
        sR1 = 102490

    elif sR1 == '하남시':
        sR1 = 102500

    elif sR1 == '화성시':
        sR1 = 102510

    elif sR1 == '광산구':
        sR1 = 103010

    elif sR1 == '남구':
        sR1 = 103020

    elif sR1 == '동구':
        sR1 = 103030

    elif sR1 == '북구':
        sR1 = 103040

    elif sR1 == '서구':
        sR1 = 103050

    elif sR1 == '남구':
        sR1 = 104010

    elif sR1 == '달서구':
        sR1 = 104020

    elif sR1 == '달성군':
        sR1 = 104030

    elif sR1 == '동구':
        sR1 = 104040

    elif sR1 == '북구':
        sR1 = 104050

    elif sR1 == '서구':
        sR1 = 104060

    elif sR1 == '수성구':
        sR1 = 104070

    elif sR1 == '중구':
        sR1 = 104080

    elif sR1 == '대덕구':
        sR1 = 105010

    elif sR1 == '동구':
        sR1 = 105020

    elif sR1 == '서구':
        sR1 = 105030

    elif sR1 == '유성구':
        sR1 = 105040

    elif sR1 == '중구':
        sR1 = 105050

    elif sR1 == '강서구':
        sR1 = 106010

    elif sR1 == '금정구':
        sR1 = 106020

    elif sR1 == '기장군':
        sR1 = 106030

    elif sR1 == '남구':
        sR1 = 106040

    elif sR1 == '동구':
        sR1 = 106050

    elif sR1 == '동래구':
        sR1 = 106060

    elif sR1 == '부산진구':
        sR1 = 106070

    elif sR1 == '북구':
        sR1 = 106080

    elif sR1 == '사상구':
        sR1 = 106090

    elif sR1 == '사하구':
        sR1 = 106100

    elif sR1 == '서구':
        sR1 = 106110

    elif sR1 == '수영구':
        sR1 = 106120

    elif sR1 == '연제구':
        sR1 = 106130

    elif sR1 == '영도구':
        sR1 = 106140

    elif sR1 == '중구':
        sR1 = 106150

    elif sR1 == '해운대구':
        sR1 = 106160

    elif sR1 == '남구':
        sR1 = 107010

    elif sR1 == '동구':
        sR1 = 107020

    elif sR1 == '북구':
        sR1 = 107030

    elif sR1 == '울주군':
        sR1 = 107040

    elif sR1 == '중구':
        sR1 = 107050

    elif sR1 == '강화군':
        sR1 = 108010

    elif sR1 == '계양구':
        sR1 = 108020

    elif sR1 == '미추홀구':
        sR1 = 108030

    elif sR1 == '남동구':
        sR1 = 108040

    elif sR1 == '동구':
        sR1 = 108050

    elif sR1 == '부평구':
        sR1 = 108060

    elif sR1 == '서구':
        sR1 = 108070

    elif sR1 == '연수구':
        sR1 = 108080

    elif sR1 == '웅진군':
        sR1 = 108090

    elif sR1 == '중구':
        sR1 = 108100

    elif sR1 == '강릉시':
        sR1 = 109010

    elif sR1 == '고성군':
        sR1 = 109020

    elif sR1 == '동해시':
        sR1 = 109030

    elif sR1 == '삼척시':
        sR1 = 109040

    elif sR1 == '속초시':
        sR1 = 109050

    elif sR1 == '양구군':
        sR1 = 109060

    elif sR1 == '양양군':
        sR1 = 109070

    elif sR1 == '영월군':
        sR1 = 109080

    elif sR1 == '원주시':
        sR1 = 109090

    elif sR1 == '인제군':
        sR1 = 109100

    elif sR1 == '정선군':
        sR1 = 109110

    elif sR1 == '철원군':
        sR1 = 109120

    elif sR1 == '춘천시':
        sR1 = 109130

    elif sR1 == '태백시':
        sR1 = 109140

    elif sR1 == '평창군':
        sR1 = 109150

    elif sR1 == '홍천군':
        sR1 = 109160

    elif sR1 == '화천군':
        sR1 = 109170

    elif sR1 == '횡선군':
        sR1 = 109180

    elif sR1 == '거제시':
        sR1 = 110010

    elif sR1 == '거창군':
        sR1 = 110020

    elif sR1 == '고성군':
        sR1 = 110030

    elif sR1 == '김해시':
        sR1 = 110040

    elif sR1 == '남해군':
        sR1 = 110050

    elif sR1 == '창원시 마산회원구':
        sR1 = 110053

    elif sR1 == '창원시 마산합포구':
        sR1 = 110055

    elif sR1 == '창원시 성산구':
        sR1 = 110057

    elif sR1 == '창원시 의창구':
        sR1 = 110059

    elif sR1 == '밀양시':
        sR1 = 110070

    elif sR1 == '사천시':
        sR1 = 110080

    elif sR1 == '산청군':
        sR1 = 110090

    elif sR1 == '양산시':
        sR1 = 110100

    elif sR1 == '의령군':
        sR1 = 110110

    elif sR1 == '진주시':
        sR1 = 110120

    elif sR1 == '창원시 진해구':
        sR1 = 110130

    elif sR1 == '창녕군':
        sR1 = 110140

    elif sR1 == '창원시':
        sR1 = 110150

    elif sR1 == '통영시':
        sR1 = 110160

    elif sR1 == '하동군':
        sR1 = 110170

    elif sR1 == '함안군':
        sR1 = 110180

    elif sR1 == '함양군':
        sR1 = 110190

    elif sR1 == '합천군':
        sR1 = 110200

    elif sR1 == '경산시':
        sR1 = 111010

    elif sR1 == '경주시':
        sR1 = 111020

    elif sR1 == '고령군':
        sR1 = 111030

    elif sR1 == '구미시':
        sR1 = 111040

    elif sR1 == '군위군':
        sR1 = 111050

    elif sR1 == '김천시':
        sR1 = 111060

    elif sR1 == '문경시':
        sR1 = 111070

    elif sR1 == '봉화군':
        sR1 = 111080

    elif sR1 == '상주시':
        sR1 = 111090

    elif sR1 == '성주군':
        sR1 = 111100

    elif sR1 == '안동시':
        sR1 = 111110

    elif sR1 == '영덕군':
        sR1 = 111120

    elif sR1 == '영양군':
        sR1 = 111130

    elif sR1 == '영주시':
        sR1 = 111140

    elif sR1 == '영천시':
        sR1 = 111150

    elif sR1 == '예천군':
        sR1 = 111160

    elif sR1 == '울릉군':
        sR1 = 111170

    elif sR1 == '울진군':
        sR1 = 111180

    elif sR1 == '의성군':
        sR1 = 111190

    elif sR1 == '청도군':
        sR1 = 111200

    elif sR1 == '청송군':
        sR1 = 111210

    elif sR1 == '칠곡군':
        sR1 = 111220

    elif sR1 == '포항시':
        sR1 = 111230

    elif sR1 == '포항시 남구':
        sR1 = 111240

    elif sR1 == '포항시 북구':
        sR1 = 111250

    elif sR1 == '강진군':
        sR1 = 112010

    elif sR1 == '고흥군':
        sR1 = 112020

    elif sR1 == '곡성군':
        sR1 = 112030

    elif sR1 == '광양시':
        sR1 = 112040

    elif sR1 == '구례군':
        sR1 = 112050

    elif sR1 == '나주시':
        sR1 = 112060

    elif sR1 == '담양군':
        sR1 = 112070

    elif sR1 == '목포시':
        sR1 = 112080

    elif sR1 == '무안군':
        sR1 = 112090

    elif sR1 == '보성군':
        sR1 = 112100

    elif sR1 == '순천시':
        sR1 = 112110

    elif sR1 == '신안군':
        sR1 = 112120

    elif sR1 == '여수시':
        sR1 = 112130

    elif sR1 == '영광군':
        sR1 = 112140

    elif sR1 == '영암군':
        sR1 = 112150

    elif sR1 == '완도군':
        sR1 = 112160

    elif sR1 == '장성군':
        sR1 = 112170

    elif sR1 == '장흥군':
        sR1 = 112180

    elif sR1 == '진도군':
        sR1 = 112190

    elif sR1 == '함평군':
        sR1 = 1122000

    elif sR1 == '해남군':
        sR1 = 112210

    elif sR1 == '화순군':
        sR1 = 112220

    elif sR1 == '고창군':
        sR1 = 113010

    elif sR1 == '군산시':
        sR1 = 113020

    elif sR1 == '김제시':
        sR1 = 113030

    elif sR1 == '남원시':
        sR1 = 113040

    elif sR1 == '무주군':
        sR1 = 113050

    elif sR1 == '부안군':
        sR1 = 113060

    elif sR1 == '순창군':
        sR1 = 113070

    elif sR1 == '완주군':
        sR1 = 113080

    elif sR1 == '익산시':
        sR1 = 113090

    elif sR1 == '임실군':
        sR1 = 113100

    elif sR1 == '장수군':
        sR1 = 113110

    elif sR1 == '전주시':
        sR1 = 113120

    elif sR1 == '전주시 덕진구':
        sR1 = 113130

    elif sR1 == '전주시 완산구':
        sR1 = 113140

    elif sR1 == '정읍시':
        sR1 = 113150

    elif sR1 == '진안군':
        sR1 = 113160

    elif sR1 == '괴산군':
        sR1 = 114010

    elif sR1 == '단양군':
        sR1 = 114020

    elif sR1 == '보은군':
        sR1 = 114030

    elif sR1 == '영동군':
        sR1 = 114040

    elif sR1 == '옥천군':
        sR1 = 114050

    elif sR1 == '음성군':
        sR1 = 114060

    elif sR1 == '제천시':
        sR1 = 114070

    elif sR1 == '증편군':
        sR1 = 114080

    elif sR1 == '진천군':
        sR1 = 114090

    elif sR1 == '청원군':
        sR1 = 114100

    elif sR1 == '청주시':
        sR1 = 114110

    elif sR1 == '청주시 상당구':
        sR1 = 114120

    elif sR1 == '청주시 흥덕구':
        sR1 = 114130

    elif sR1 == '충주시':
        sR1 = 114140

    elif sR1 == '청주시 청원구':
        sR1 = 114150

    elif sR1 == '청주시 서원구':
        sR1 = 114160

    elif sR1 == '계룡시':
        sR1 = 115010

    elif sR1 == '공주시':
        sR1 = 115020

    elif sR1 == '금산군':
        sR1 = 115030

    elif sR1 == '논산시':
        sR1 = 115040

    elif sR1 == '당진시':
        sR1 = 115050

    elif sR1 == '보령시':
        sR1 = 115060

    elif sR1 == '부여군':
        sR1 = 115070

    elif sR1 == '서산시':
        sR1 = 115080

    elif sR1 == '서천군':
        sR1 = 105090

    elif sR1 == '아산시':
        sR1 = 115100

    elif sR1 == '연기군':
        sR1 = 115110

    elif sR1 == '예산군':
        sR1 = 115120

    elif sR1 == '천안시':
        sR1 = 115130

    elif sR1 == '천안시 동남구':
        sR1 = 115133

    elif sR1 == '천안시 서북구':
        sR1 = 115135

    elif sR1 == '청양군':
        sR1 = 115140

    elif sR1 == '태안군':
        sR1 = 115150

    elif sR1 == '홍성군':
        sR1 = 115160

    elif sR1 == '서귀포시':
        sR1 = 116030

    elif sR1 == '제주시':
        sR1 = 116040

    if sR2 == "서울 전체":
        sR2 = 101000

    elif sR2 == '경기 전체':
        sR2 = 102000

    elif sR2 == '인천 전체':
        sR2 = 108000

    elif sR2 == '부산 전체':

        sR2 = 106000

    elif sR2 == '대구 전체':
        sR2 = 104000

    elif sR2 == '대전 전체':
        sR2 = 105000

    elif sR2 == '울산 전체':
        sR2 = 107000

    elif sR2 == '세종 전체':
        sR2 = 118000

    elif sR2 == '강원 전체':
        sR2 = 109000

    elif sR2 == '경남 전체':
        sR2 = 110000

    elif sR2 == '경북 전체':
        sR2 = 111000

    elif sR2 == '전남 전체':
        sR2 = 112000

    elif sR2 == '전북 전체':
        sR2 = 113000

    elif sR2 == '충남 전체':
        sR2 = 115000

    elif sR2 == '충북 전체':
        sR2 = 114000

    elif sR2 == '제주 전체':
        sR2 = 116000

    if sR2 == '강남구':
        sR2 = 101010

    elif sR2 == '강동구':
        sR2 = 101020

    elif sR2 == '강북구':
        sR2 = 101030

    elif sR2 == '강서구':
        sR2 = 101040

    elif sR2 == '관안구':
        sR2 = 101050

    elif sR2 == '광진구':
        sR2 = 101060

    elif sR2 == '구로구':
        sR2 = 101070

    elif sR2 == '금천구':
        sR2 = 101080

    elif sR2 == '노원구':
        sR2 = 101090

    elif sR2 == '도봉구':
        sR2 = 101100

    elif sR2 == '동대문구':
        sR2 = 101110

    elif sR2 == '동작구':
        sR2 = 101120

    elif sR2 == '마포구':
        sR2 = 101130

    elif sR2 == '서대문구':
        sR2 = 101140

    elif sR2 == '서초구':
        sR2 = 101150

    elif sR2 == '성동구':
        sR2 = 101160

    elif sR2 == '성북구':
        sR2 = 101170

    elif sR2 == '송파구':
        sR2 = 101180

    elif sR2 == '양천구':
        sR2 = 101190

    elif sR2 == '영등포구':
        sR2 = 101200

    elif sR2 == '용산구':
        sR2 = 101210

    elif sR2 == '은평구':
        sR2 = 101220

    elif sR2 == '종로구':
        sR2 = 101230

    elif sR2 == '중구':
        sR2 = 101240

    elif sR2 == '중랑구':
        sR2 = 101250

    elif sR2 == '가평군':
        sR2 = 102010

    elif sR2 == '고양시':
        sR2 = 102020

    elif sR2 == '고양시 덕양구':
        sR2 = 102030

    elif sR2 == '고양시 일산동구':
        sR2 = 102040

    elif sR2 == '고양시 일산서구':
        sR2 = 102050

    elif sR2 == '과천시':
        sR2 = 102060

    elif sR2 == '광명시':
        sR2 = 102070

    elif sR2 == '광주시':
        sR2 = 102080

    elif sR2 == '구리시':
        sR2 = 102090

    elif sR2 == '군포사':
        sR2 = 102100

    elif sR2 == '김포시':
        sR2 = 102110

    elif sR2 == '남양주시':
        sR2 = 102120

    elif sR2 == '동두천시':
        sR2 = 102130

    elif sR2 == '부천시':
        sR2 = 102140

    elif sR2 == '부천시 소사구':
        sR2 = 102150

    elif sR2 == '부천시 오정구':
        sR2 = 102160

    elif sR2 == '부천시 원미구':
        sR2 = 102170

    elif sR2 == '성남시':
        sR2 = 102180

    elif sR2 == '성남시 분당구':
        sR2 = 102190

    elif sR2 == '성남시 수정구':
        sR2 = 102200

    elif sR2 == '성남시 중원구':
        sR2 = 102210

    elif sR2 == '수원시':
        sR2 = 102220

    elif sR2 == '수원시 권선구':
        sR2 = 102230

    elif sR2 == '수원시 영통구':
        sR2 = 102240

    elif sR2 == '수원시 장안구':
        sR2 = 102250

    elif sR2 == '수원시 팔달구':
        sR2 = 102260

    elif sR2 == '시흥시':
        sR2 = 102270

    elif sR2 == '안산시':
        sR2 = 102280

    elif sR2 == '안산시 단원구':
        sR2 = 102290

    elif sR2 == '안산시 상록구':
        sR2 = 102300

    elif sR2 == '안성시':
        sR2 = 102310

    elif sR2 == '안양시':
        sR2 = 102320

    elif sR2 == '안양시 동안구':
        sR2 = 102330

    elif sR2 == '안양시 만안구':
        sR2 = 102340

    elif sR2 == '양주시':
        sR2 = 102350

    elif sR2 == '양평군':
        sR2 = 102360

    elif sR2 == '여주시':
        sR2 = 102370

    elif sR2 == '연천군':
        sR2 = 102380

    elif sR2 == '오산시':
        sR2 = 102390

    elif sR2 == '용인시':
        sR2 = 102400

    elif sR2 == '용인시 기흥구':
        sR2 = 102410

    elif sR2 == '용인시 수지구':
        sR2 = 102420

    elif sR2 == '용인시 처인구':
        sR2 = 102430

    elif sR2 == '의왕시':
        sR2 = 102440

    elif sR2 == '의정부시':
        sR2 = 102450

    elif sR2 == '이천시':
        sR2 = 102460

    elif sR2 == '파주시':
        sR2 = 102470

    elif sR2 == '평택시':
        sR2 = 102480

    elif sR2 == '포천시':
        sR2 = 102490

    elif sR2 == '하남시':
        sR2 = 102500

    elif sR2 == '화성시':
        sR2 = 102510

    elif sR2 == '광산구':
        sR2 = 103010

    elif sR2 == '남구':
        sR2 = 103020

    elif sR2 == '동구':
        sR2 = 103030

    elif sR2 == '북구':
        sR2 = 103040

    elif sR2 == '서구':
        sR2 = 103050

    elif sR2 == '남구':
        sR2 = 104010

    elif sR2 == '달서구':
        sR2 = 104020

    elif sR2 == '달성군':
        sR2 = 104030

    elif sR2 == '동구':
        sR2 = 104040

    elif sR2 == '북구':
        sR2 = 104050

    elif sR2 == '서구':
        sR2 = 104060

    elif sR2 == '수성구':
        sR2 = 104070

    elif sR2 == '중구':
        sR2 = 104080

    elif sR2 == '대덕구':
        sR2 = 105010

    elif sR2 == '동구':
        sR2 = 105020

    elif sR2 == '서구':
        sR2 = 105030

    elif sR2 == '유성구':
        sR2 = 105040

    elif sR2 == '중구':
        sR2 = 105050

    elif sR2 == '강서구':
        sR2 = 106010

    elif sR2 == '금정구':
        sR2 = 106020

    elif sR2 == '기장군':
        sR2 = 106030

    elif sR2 == '남구':
        sR2 = 106040

    elif sR2 == '동구':
        sR2 = 106050

    elif sR2 == '동래구':
        sR2 = 106060

    elif sR2 == '부산진구':
        sR2 = 106070

    elif sR2 == '북구':
        sR2 = 106080

    elif sR2 == '사상구':
        sR2 = 106090

    elif sR2 == '사하구':
        sR2 = 106100

    elif sR2 == '서구':
        sR2 = 106110

    elif sR2 == '수영구':
        sR2 = 106120

    elif sR2 == '연제구':
        sR2 = 106130

    elif sR2 == '영도구':
        sR2 = 106140

    elif sR2 == '중구':
        sR2 = 106150

    elif sR2 == '해운대구':
        sR2 = 106160

    elif sR2 == '남구':
        sR2 = 107010

    elif sR2 == '동구':
        sR2 = 107020

    elif sR2 == '북구':
        sR2 = 107030

    elif sR2 == '울주군':
        sR2 = 107040

    elif sR2 == '중구':
        sR2 = 107050

    elif sR2 == '강화군':
        sR2 = 108010

    elif sR2 == '계양구':
        sR2 = 108020

    elif sR2 == '미추홀구':
        sR2 = 108030

    elif sR2 == '남동구':
        sR2 = 108040

    elif sR2 == '동구':
        sR2 = 108050

    elif sR2 == '부평구':
        sR2 = 108060

    elif sR2 == '서구':
        sR2 = 108070

    elif sR2 == '연수구':
        sR2 = 108080

    elif sR2 == '웅진군':
        sR2 = 108090

    elif sR2 == '중구':
        sR2 = 108100

    elif sR2 == '강릉시':
        sR2 = 109010

    elif sR2 == '고성군':
        sR2 = 109020

    elif sR2 == '동해시':
        sR2 = 109030

    elif sR2 == '삼척시':
        sR2 = 109040

    elif sR2 == '속초시':
        sR2 = 109050

    elif sR2 == '양구군':
        sR2 = 109060

    elif sR2 == '양양군':
        sR2 = 109070

    elif sR2 == '영월군':
        sR2 = 109080

    elif sR2 == '원주시':
        sR2 = 109090

    elif sR2 == '인제군':
        sR2 = 109100

    elif sR2 == '정선군':
        sR2 = 109110

    elif sR2 == '철원군':
        sR2 = 109120

    elif sR2 == '춘천시':
        sR2 = 109130

    elif sR2 == '태백시':
        sR2 = 109140

    elif sR2 == '평창군':
        sR2 = 109150

    elif sR2 == '홍천군':
        sR2 = 109160

    elif sR2 == '화천군':
        sR2 = 109170

    elif sR2 == '횡선군':
        sR2 = 109180

    elif sR2 == '거제시':
        sR2 = 110010

    elif sR2 == '거창군':
        sR2 = 110020

    elif sR2 == '고성군':
        sR2 = 110030

    elif sR2 == '김해시':
        sR2 = 110040

    elif sR2 == '남해군':
        sR2 = 110050

    elif sR2 == '창원시 마산회원구':
        sR2 = 110053

    elif sR2 == '창원시 마산합포구':
        sR2 = 110055

    elif sR2 == '창원시 성산구':
        sR2 = 110057

    elif sR2 == '창원시 의창구':
        sR2 = 110059

    elif sR2 == '밀양시':
        sR2 = 110070

    elif sR2 == '사천시':
        sR2 = 110080

    elif sR2 == '산청군':
        sR2 = 110090

    elif sR2 == '양산시':
        sR2 = 110100

    elif sR2 == '의령군':
        sR2 = 110110

    elif sR2 == '진주시':
        sR2 = 110120

    elif sR2 == '창원시 진해구':
        sR2 = 110130

    elif sR2 == '창녕군':
        sR2 = 110140

    elif sR2 == '창원시':
        sR2 = 110150

    elif sR2 == '통영시':
        sR2 = 110160

    elif sR2 == '하동군':
        sR2 = 110170

    elif sR2 == '함안군':
        sR2 = 110180

    elif sR2 == '함양군':
        sR2 = 110190

    elif sR2 == '합천군':
        sR2 = 110200

    elif sR2 == '경산시':
        sR2 = 111010

    elif sR2 == '경주시':
        sR2 = 111020

    elif sR2 == '고령군':
        sR2 = 111030

    elif sR2 == '구미시':
        sR2 = 111040

    elif sR2 == '군위군':
        sR2 = 111050

    elif sR2 == '김천시':
        sR2 = 111060

    elif sR2 == '문경시':
        sR2 = 111070

    elif sR2 == '봉화군':
        sR2 = 111080

    elif sR2 == '상주시':
        sR2 = 111090

    elif sR2 == '성주군':
        sR2 = 111100

    elif sR2 == '안동시':
        sR2 = 111110

    elif sR2 == '영덕군':
        sR2 = 111120

    elif sR2 == '영양군':
        sR2 = 111130

    elif sR2 == '영주시':
        sR2 = 111140

    elif sR2 == '영천시':
        sR2 = 111150

    elif sR2 == '예천군':
        sR2 = 111160

    elif sR2 == '울릉군':
        sR2 = 111170

    elif sR2 == '울진군':
        sR2 = 111180

    elif sR2 == '의성군':
        sR2 = 111190

    elif sR2 == '청도군':
        sR2 = 111200

    elif sR2 == '청송군':
        sR2 = 111210

    elif sR2 == '칠곡군':
        sR2 = 111220

    elif sR2 == '포항시':
        sR2 = 111230

    elif sR2 == '포항시 남구':
        sR2 = 111240

    elif sR2 == '포항시 북구':
        sR2 = 111250

    elif sR2 == '강진군':
        sR2 = 112010

    elif sR2 == '고흥군':
        sR2 = 112020

    elif sR2 == '곡성군':
        sR2 = 112030

    elif sR2 == '광양시':
        sR2 = 112040

    elif sR2 == '구례군':
        sR2 = 112050

    elif sR2 == '나주시':
        sR2 = 112060

    elif sR2 == '담양군':
        sR2 = 112070

    elif sR2 == '목포시':
        sR2 = 112080

    elif sR2 == '무안군':
        sR2 = 112090

    elif sR2 == '보성군':
        sR2 = 112100

    elif sR2 == '순천시':
        sR2 = 112110

    elif sR2 == '신안군':
        sR2 = 112120

    elif sR2 == '여수시':
        sR2 = 112130

    elif sR2 == '영광군':
        sR2 = 112140

    elif sR2 == '영암군':
        sR2 = 112150

    elif sR2 == '완도군':
        sR2 = 112160

    elif sR2 == '장성군':
        sR2 = 112170

    elif sR2 == '장흥군':
        sR2 = 112180

    elif sR2 == '진도군':
        sR2 = 112190

    elif sR2 == '함평군':
        sR2 = 1122000

    elif sR2 == '해남군':
        sR2 = 112210

    elif sR2 == '화순군':
        sR2 = 112220

    elif sR2 == '고창군':
        sR2 = 113010

    elif sR2 == '군산시':
        sR2 = 113020

    elif sR2 == '김제시':
        sR2 = 113030

    elif sR2 == '남원시':
        sR2 = 113040

    elif sR2 == '무주군':
        sR2 = 113050

    elif sR2 == '부안군':
        sR2 = 113060

    elif sR2 == '순창군':
        sR2 = 113070

    elif sR2 == '완주군':
        sR2 = 113080

    elif sR2 == '익산시':
        sR2 = 113090

    elif sR2 == '임실군':
        sR2 = 113100

    elif sR2 == '장수군':
        sR2 = 113110

    elif sR2 == '전주시':
        sR2 = 113120

    elif sR2 == '전주시 덕진구':
        sR2 = 113130

    elif sR2 == '전주시 완산구':
        sR2 = 113140

    elif sR2 == '정읍시':
        sR2 = 113150

    elif sR2 == '진안군':
        sR2 = 113160

    elif sR2 == '괴산군':
        sR2 = 114010

    elif sR2 == '단양군':
        sR2 = 114020

    elif sR2 == '보은군':
        sR2 = 114030

    elif sR2 == '영동군':
        sR2 = 114040

    elif sR2 == '옥천군':
        sR2 = 114050

    elif sR2 == '음성군':
        sR2 = 114060

    elif sR2 == '제천시':
        sR2 = 114070

    elif sR2 == '증편군':
        sR2 = 114080

    elif sR2 == '진천군':
        sR2 = 114090

    elif sR2 == '청원군':
        sR2 = 114100

    elif sR2 == '청주시':
        sR2 = 114110

    elif sR2 == '청주시 상당구':
        sR2 = 114120

    elif sR2 == '청주시 흥덕구':
        sR2 = 114130

    elif sR2 == '충주시':
        sR2 = 114140

    elif sR2 == '청주시 청원구':
        sR2 = 114150

    elif sR2 == '청주시 서원구':
        sR2 = 114160

    elif sR2 == '계룡시':
        sR2 = 115010

    elif sR2 == '공주시':
        sR2 = 115020

    elif sR2 == '금산군':
        sR2 = 115030

    elif sR2 == '논산시':
        sR2 = 115040

    elif sR2 == '당진시':
        sR2 = 115050

    elif sR2 == '보령시':
        sR2 = 115060

    elif sR2 == '부여군':
        sR2 = 115070

    elif sR2 == '서산시':
        sR2 = 115080

    elif sR2 == '서천군':
        sR2 = 105090

    elif sR2 == '아산시':
        sR2 = 115100

    elif sR2 == '연기군':
        sR2 = 115110

    elif sR2 == '예산군':
        sR2 = 115120

    elif sR2 == '천안시':
        sR2 = 115130

    elif sR2 == '천안시 동남구':
        sR2 = 115133

    elif sR2 == '천안시 서북구':
        sR2 = 115135

    elif sR2 == '청양군':
        sR2 = 115140

    elif sR2 == '태안군':
        sR2 = 115150

    elif sR2 == '홍성군':
        sR2 = 115160

    elif sR2 == '서귀포시':
        sR2 = 116030

    elif sR2 == '제주시':
        sR2 = 116040

    if sR3 == "서울 전체":
        sR3 = 101000

    elif sR3 == '경기 전체':
        sR3 = 102000

    elif sR3 == '인천 전체':
        sR3 = 108000

    elif sR3 == '부산 전체':

        sR3 = 106000

    elif sR3 == '대구 전체':
        sR3 = 104000

    elif sR3 == '대전 전체':
        sR3 = 105000

    elif sR3 == '울산 전체':
        sR3 = 107000

    elif sR3 == '세종 전체':
        sR3 = 118000

    elif sR3 == '강원 전체':
        sR3 = 109000

    elif sR3 == '경남 전체':
        sR3 = 110000

    elif sR3 == '경북 전체':
        sR3 = 111000

    elif sR3 == '전남 전체':
        sR3 = 112000

    elif sR3 == '전북 전체':
        sR3 = 113000

    elif sR3 == '충남 전체':
        sR3 = 115000

    elif sR3 == '충북 전체':
        sR3 = 114000

    elif sR3 == '제주 전체':
        sR3 = 116000

    if sR3 == '강남구':
        sR3 = 101010

    elif sR3 == '강동구':
        sR3 = 101020

    elif sR3 == '강북구':
        sR3 = 101030

    elif sR3 == '강서구':
        sR3 = 101040

    elif sR3 == '관안구':
        sR3 = 101050

    elif sR3 == '광진구':
        sR3 = 101060

    elif sR3 == '구로구':
        sR3 = 101070

    elif sR3 == '금천구':
        sR3 = 101080

    elif sR3 == '노원구':
        sR3 = 101090

    elif sR3 == '도봉구':
        sR3 = 101100

    elif sR3 == '동대문구':
        sR3 = 101110

    elif sR3 == '동작구':
        sR3 = 101120

    elif sR3 == '마포구':
        sR3 = 101130

    elif sR3 == '서대문구':
        sR3 = 101140

    elif sR3 == '서초구':
        sR3 = 101150

    elif sR3 == '성동구':
        sR3 = 101160

    elif sR3 == '성북구':
        sR3 = 101170

    elif sR3 == '송파구':
        sR3 = 101180

    elif sR3 == '양천구':
        sR3 = 101190

    elif sR3 == '영등포구':
        sR3 = 101200

    elif sR3 == '용산구':
        sR3 = 101210

    elif sR3 == '은평구':
        sR3 = 101220

    elif sR3 == '종로구':
        sR3 = 101230

    elif sR3 == '중구':
        sR3 = 101240

    elif sR3 == '중랑구':
        sR3 = 101250

    elif sR3 == '가평군':
        sR3 = 102010

    elif sR3 == '고양시':
        sR3 = 102020

    elif sR3 == '고양시 덕양구':
        sR3 = 102030

    elif sR3 == '고양시 일산동구':
        sR3 = 102040

    elif sR3 == '고양시 일산서구':
        sR3 = 102050

    elif sR3 == '과천시':
        sR3 = 102060

    elif sR3 == '광명시':
        sR3 = 102070

    elif sR3 == '광주시':
        sR3 = 102080

    elif sR3 == '구리시':
        sR3 = 102090

    elif sR3 == '군포사':
        sR3 = 102100

    elif sR3 == '김포시':
        sR3 = 102110

    elif sR3 == '남양주시':
        sR3 = 102120

    elif sR3 == '동두천시':
        sR3 = 102130

    elif sR3 == '부천시':
        sR3 = 102140

    elif sR3 == '부천시 소사구':
        sR3 = 102150

    elif sR3 == '부천시 오정구':
        sR3 = 102160

    elif sR3 == '부천시 원미구':
        sR3 = 102170

    elif sR3 == '성남시':
        sR3 = 102180

    elif sR3 == '성남시 분당구':
        sR3 = 102190

    elif sR3 == '성남시 수정구':
        sR3 = 102200

    elif sR3 == '성남시 중원구':
        sR3 = 102210

    elif sR3 == '수원시':
        sR3 = 102220

    elif sR3 == '수원시 권선구':
        sR3 = 102230

    elif sR3 == '수원시 영통구':
        sR3 = 102240

    elif sR3 == '수원시 장안구':
        sR3 = 102250

    elif sR3 == '수원시 팔달구':
        sR3 = 102260

    elif sR3 == '시흥시':
        sR3 = 102270

    elif sR3 == '안산시':
        sR3 = 102280

    elif sR3 == '안산시 단원구':
        sR3 = 102290

    elif sR3 == '안산시 상록구':
        sR3 = 102300

    elif sR3 == '안성시':
        sR3 = 102310

    elif sR3 == '안양시':
        sR3 = 102320

    elif sR3 == '안양시 동안구':
        sR3 = 102330

    elif sR3 == '안양시 만안구':
        sR3 = 102340

    elif sR3 == '양주시':
        sR3 = 102350

    elif sR3 == '양평군':
        sR3 = 102360

    elif sR3 == '여주시':
        sR3 = 102370

    elif sR3 == '연천군':
        sR3 = 102380

    elif sR3 == '오산시':
        sR3 = 102390

    elif sR3 == '용인시':
        sR3 = 102400

    elif sR3 == '용인시 기흥구':
        sR3 = 102410

    elif sR3 == '용인시 수지구':
        sR3 = 102420

    elif sR3 == '용인시 처인구':
        sR3 = 102430

    elif sR3 == '의왕시':
        sR3 = 102440

    elif sR3 == '의정부시':
        sR3 = 102450

    elif sR3 == '이천시':
        sR3 = 102460

    elif sR3 == '파주시':
        sR3 = 102470

    elif sR3 == '평택시':
        sR3 = 102480

    elif sR3 == '포천시':
        sR3 = 102490

    elif sR3 == '하남시':
        sR3 = 102500

    elif sR3 == '화성시':
        sR3 = 102510

    elif sR3 == '광산구':
        sR3 = 103010

    elif sR3 == '남구':
        sR3 = 103020

    elif sR3 == '동구':
        sR3 = 103030

    elif sR3 == '북구':
        sR3 = 103040

    elif sR3 == '서구':
        sR3 = 103050

    elif sR3 == '남구':
        sR3 = 104010

    elif sR3 == '달서구':
        sR3 = 104020

    elif sR3 == '달성군':
        sR3 = 104030

    elif sR3 == '동구':
        sR3 = 104040

    elif sR3 == '북구':
        sR3 = 104050

    elif sR3 == '서구':
        sR3 = 104060

    elif sR3 == '수성구':
        sR3 = 104070

    elif sR3 == '중구':
        sR3 = 104080

    elif sR3 == '대덕구':
        sR3 = 105010

    elif sR3 == '동구':
        sR3 = 105020

    elif sR3 == '서구':
        sR3 = 105030

    elif sR3 == '유성구':
        sR3 = 105040

    elif sR3 == '중구':
        sR3 = 105050

    elif sR3 == '강서구':
        sR3 = 106010

    elif sR3 == '금정구':
        sR3 = 106020

    elif sR3 == '기장군':
        sR3 = 106030

    elif sR3 == '남구':
        sR3 = 106040

    elif sR3 == '동구':
        sR3 = 106050

    elif sR3 == '동래구':
        sR3 = 106060

    elif sR3 == '부산진구':
        sR3 = 106070

    elif sR3 == '북구':
        sR3 = 106080

    elif sR3 == '사상구':
        sR3 = 106090

    elif sR3 == '사하구':
        sR3 = 106100

    elif sR3 == '서구':
        sR3 = 106110

    elif sR3 == '수영구':
        sR3 = 106120

    elif sR3 == '연제구':
        sR3 = 106130

    elif sR3 == '영도구':
        sR3 = 106140

    elif sR3 == '중구':
        sR3 = 106150

    elif sR3 == '해운대구':
        sR3 = 106160

    elif sR3 == '남구':
        sR3 = 107010

    elif sR3 == '동구':
        sR3 = 107020

    elif sR3 == '북구':
        sR3 = 107030

    elif sR3 == '울주군':
        sR3 = 107040

    elif sR3 == '중구':
        sR3 = 107050

    elif sR3 == '강화군':
        sR3 = 108010

    elif sR3 == '계양구':
        sR3 = 108020

    elif sR3 == '미추홀구':
        sR3 = 108030

    elif sR3 == '남동구':
        sR3 = 108040

    elif sR3 == '동구':
        sR3 = 108050

    elif sR3 == '부평구':
        sR3 = 108060

    elif sR3 == '서구':
        sR3 = 108070

    elif sR3 == '연수구':
        sR3 = 108080

    elif sR3 == '웅진군':
        sR3 = 108090

    elif sR3 == '중구':
        sR3 = 108100

    elif sR3 == '강릉시':
        sR3 = 109010

    elif sR3 == '고성군':
        sR3 = 109020

    elif sR3 == '동해시':
        sR3 = 109030

    elif sR3 == '삼척시':
        sR3 = 109040

    elif sR3 == '속초시':
        sR3 = 109050

    elif sR3 == '양구군':
        sR3 = 109060

    elif sR3 == '양양군':
        sR3 = 109070

    elif sR3 == '영월군':
        sR3 = 109080

    elif sR3 == '원주시':
        sR3 = 109090

    elif sR3 == '인제군':
        sR3 = 109100

    elif sR3 == '정선군':
        sR3 = 109110

    elif sR3 == '철원군':
        sR3 = 109120

    elif sR3 == '춘천시':
        sR3 = 109130

    elif sR3 == '태백시':
        sR3 = 109140

    elif sR3 == '평창군':
        sR3 = 109150

    elif sR3 == '홍천군':
        sR3 = 109160

    elif sR3 == '화천군':
        sR3 = 109170

    elif sR3 == '횡선군':
        sR3 = 109180

    elif sR3 == '거제시':
        sR3 = 110010

    elif sR3 == '거창군':
        sR3 = 110020

    elif sR3 == '고성군':
        sR3 = 110030

    elif sR3 == '김해시':
        sR3 = 110040

    elif sR3 == '남해군':
        sR3 = 110050

    elif sR3 == '창원시 마산회원구':
        sR3 = 110053

    elif sR3 == '창원시 마산합포구':
        sR3 = 110055

    elif sR3 == '창원시 성산구':
        sR3 = 110057

    elif sR3 == '창원시 의창구':
        sR3 = 110059

    elif sR3 == '밀양시':
        sR3 = 110070

    elif sR3 == '사천시':
        sR3 = 110080

    elif sR3 == '산청군':
        sR3 = 110090

    elif sR3 == '양산시':
        sR3 = 110100

    elif sR3 == '의령군':
        sR3 = 110110

    elif sR3 == '진주시':
        sR3 = 110120

    elif sR3 == '창원시 진해구':
        sR3 = 110130

    elif sR3 == '창녕군':
        sR3 = 110140

    elif sR3 == '창원시':
        sR3 = 110150

    elif sR3 == '통영시':
        sR3 = 110160

    elif sR3 == '하동군':
        sR3 = 110170

    elif sR3 == '함안군':
        sR3 = 110180

    elif sR3 == '함양군':
        sR3 = 110190

    elif sR3 == '합천군':
        sR3 = 110200

    elif sR3 == '경산시':
        sR3 = 111010

    elif sR3 == '경주시':
        sR3 = 111020

    elif sR3 == '고령군':
        sR3 = 111030

    elif sR3 == '구미시':
        sR3 = 111040

    elif sR3 == '군위군':
        sR3 = 111050

    elif sR3 == '김천시':
        sR3 = 111060

    elif sR3 == '문경시':
        sR3 = 111070

    elif sR3 == '봉화군':
        sR3 = 111080

    elif sR3 == '상주시':
        sR3 = 111090

    elif sR3 == '성주군':
        sR3 = 111100

    elif sR3 == '안동시':
        sR3 = 111110

    elif sR3 == '영덕군':
        sR3 = 111120

    elif sR3 == '영양군':
        sR3 = 111130

    elif sR3 == '영주시':
        sR3 = 111140

    elif sR3 == '영천시':
        sR3 = 111150

    elif sR3 == '예천군':
        sR3 = 111160

    elif sR3 == '울릉군':
        sR3 = 111170

    elif sR3 == '울진군':
        sR3 = 111180

    elif sR3 == '의성군':
        sR3 = 111190

    elif sR3 == '청도군':
        sR3 = 111200

    elif sR3 == '청송군':
        sR3 = 111210

    elif sR3 == '칠곡군':
        sR3 = 111220

    elif sR3 == '포항시':
        sR3 = 111230

    elif sR3 == '포항시 남구':
        sR3 = 111240

    elif sR3 == '포항시 북구':
        sR3 = 111250

    elif sR3 == '강진군':
        sR3 = 112010

    elif sR3 == '고흥군':
        sR3 = 112020

    elif sR3 == '곡성군':
        sR3 = 112030

    elif sR3 == '광양시':
        sR3 = 112040

    elif sR3 == '구례군':
        sR3 = 112050

    elif sR3 == '나주시':
        sR3 = 112060

    elif sR3 == '담양군':
        sR3 = 112070

    elif sR3 == '목포시':
        sR3 = 112080

    elif sR3 == '무안군':
        sR3 = 112090

    elif sR3 == '보성군':
        sR3 = 112100

    elif sR3 == '순천시':
        sR3 = 112110

    elif sR3 == '신안군':
        sR3 = 112120

    elif sR3 == '여수시':
        sR3 = 112130

    elif sR3 == '영광군':
        sR3 = 112140

    elif sR3 == '영암군':
        sR3 = 112150

    elif sR3 == '완도군':
        sR3 = 112160

    elif sR3 == '장성군':
        sR3 = 112170

    elif sR3 == '장흥군':
        sR3 = 112180

    elif sR3 == '진도군':
        sR3 = 112190

    elif sR3 == '함평군':
        sR3 = 1122000

    elif sR3 == '해남군':
        sR3 = 112210

    elif sR3 == '화순군':
        sR3 = 112220

    elif sR3 == '고창군':
        sR3 = 113010

    elif sR3 == '군산시':
        sR3 = 113020

    elif sR3 == '김제시':
        sR3 = 113030

    elif sR3 == '남원시':
        sR3 = 113040

    elif sR3 == '무주군':
        sR3 = 113050

    elif sR3 == '부안군':
        sR3 = 113060

    elif sR3 == '순창군':
        sR3 = 113070

    elif sR3 == '완주군':
        sR3 = 113080

    elif sR3 == '익산시':
        sR3 = 113090

    elif sR3 == '임실군':
        sR3 = 113100

    elif sR3 == '장수군':
        sR3 = 113110

    elif sR3 == '전주시':
        sR3 = 113120

    elif sR3 == '전주시 덕진구':
        sR3 = 113130

    elif sR3 == '전주시 완산구':
        sR3 = 113140

    elif sR3 == '정읍시':
        sR3 = 113150

    elif sR3 == '진안군':
        sR3 = 113160

    elif sR3 == '괴산군':
        sR3 = 114010

    elif sR3 == '단양군':
        sR3 = 114020

    elif sR3 == '보은군':
        sR3 = 114030

    elif sR3 == '영동군':
        sR3 = 114040

    elif sR3 == '옥천군':
        sR3 = 114050

    elif sR3 == '음성군':
        sR3 = 114060

    elif sR3 == '제천시':
        sR3 = 114070

    elif sR3 == '증편군':
        sR3 = 114080

    elif sR3 == '진천군':
        sR3 = 114090

    elif sR3 == '청원군':
        sR3 = 114100

    elif sR3 == '청주시':
        sR3 = 114110

    elif sR3 == '청주시 상당구':
        sR3 = 114120

    elif sR3 == '청주시 흥덕구':
        sR3 = 114130

    elif sR3 == '충주시':
        sR3 = 114140

    elif sR3 == '청주시 청원구':
        sR3 = 114150

    elif sR3 == '청주시 서원구':
        sR3 = 114160

    elif sR3 == '계룡시':
        sR3 = 115010

    elif sR3 == '공주시':
        sR3 = 115020

    elif sR3 == '금산군':
        sR3 = 115030

    elif sR3 == '논산시':
        sR3 = 115040

    elif sR3 == '당진시':
        sR3 = 115050

    elif sR3 == '보령시':
        sR3 = 115060

    elif sR3 == '부여군':
        sR3 = 115070

    elif sR3 == '서산시':
        sR3 = 115080

    elif sR3 == '서천군':
        sR3 = 105090

    elif sR3 == '아산시':
        sR3 = 115100

    elif sR3 == '연기군':
        sR3 = 115110

    elif sR3 == '예산군':
        sR3 = 115120

    elif sR3 == '천안시':
        sR3 = 115130

    elif sR3 == '천안시 동남구':
        sR3 = 115133

    elif sR3 == '천안시 서북구':
        sR3 = 115135

    elif sR3 == '청양군':
        sR3 = 115140

    elif sR3 == '태안군':
        sR3 = 115150

    elif sR3 == '홍성군':
        sR3 = 115160

    elif sR3 == '서귀포시':
        sR3 = 116030

    elif sR3 == '제주시':
        sR3 = 116040

    if b == '서비스업':
        b = 1

    elif b == '제조·화학':
        b = 2

    elif b == 'IT·웹·통신':
        b = 3

    elif b == '은행·금융업':
        b = 4

    elif b == '미디어·디자인':
        b = 5

    elif b == '교육업':
        b = 6

    elif b == '의료·제약·복지':
        b = 7

    elif b == '판매·유통':
        b = 8

    elif b == '건설업':
        b = 9

    elif b == '기관·협회':
        b = 10

    if b2 == '서비스업':
        b2 = 1

    elif b2 == '제조·화학':
        b2 = 2

    elif b2 == 'IT·웹·통신':
        b2 = 3

    elif b2 == '은행·금융업':
        b2 = 4

    elif b2 == '미디어·디자인':
        b2 = 5

    elif b2 == '교육업':
        b2 = 6

    elif b2 == '의료·제약·복지':
        b2 = 7

    elif b2 == '판매·유통':
        b2 = 8

    elif b2 == '건설업':
        b2 = 9

    elif b2 == '기관·협회':
        b2 = 10

    if sB == '호텔·여행·항공':
        sB = 108

    elif sB == '외식업·식음료':
        sB = 109

    elif sB == '시설관리·경비·용역':
        sB = 111

    elif sB == '레저·스포츠·여가':
        sB = 115

    elif sB == 'AS·카센터·주유':
        sB = 118

    elif sB == '렌탈·임대':
        sB = 119

    elif sB == '웨딩·장례·이벤트':
        sB = 120

    elif sB == '기타서비스업':
        sB = 121

    elif sB == '뷰티·미용':
        sB = 122

    elif sB == '전기·전자·제어':
        sB = 201

    elif sB == '기계·설비·자동차':
        sB = 202

    elif sB == '석유·화학·에너지':
        sB = 204

    elif sB == '섬유·의류·패션':
        sB = 205

    elif sB == '화장품·뷰티':
        sB = 207

    elif sB == '생활용품·소비재·사무':
        sB = 208

    elif sB == '가구·목재·제지':
        sB = 209

    elif sB == '농업·어업·광업·임업':
        sB = 210

    elif sB == '금속·재료·철강·요업':
        sB = 211

    elif sB == '조선·항공·우주':
        sB = 212

    elif sB == '기타제조업':
        sB = 213

    elif sB == '식품가공·개발':
        sB = 214

    elif sB == '반도체·광학·LCD':
        sB = 215

    elif sB == '환경':
        sB = 216

    elif sB == '솔루션·SI·ERP·CRM':
        sB = 301

    elif sB == '웹에이젼시':
        sB = 302

    elif sB == '쇼핑몰·오픈마켓':
        sB = 304

    elif sB == '포털·인터넷·컨텐츠':
        sB = 305

    elif sB == '네트워크·통신·모바일':
        sB = 306

    elif sB == '하드웨어·장비':
        sB = 307

    elif sB == '정보보안·백신':
        sB = 308

    elif sB == 'IT컨설팅':
        sB = 313

    elif sB == '게임':
        sB = 314

    elif sB == '은행·금융·저축':
        sB = 401

    elif sB == '대출·캐피탈·여신':
        sB = 402

    elif sB == '기타금융':
        sB = 405

    elif sB == '증권·보험·카드':
        sB = 406

    elif sB == '신문·잡지·언론사':
        sB = 501

    elif sB == '방송사·케이블':
        sB = 502

    elif sB == '연예·엔터테인먼트':
        sB = 503

    elif sB == '광고·홍보·전시':
        sB = 504

    elif sB == '영화·배급·음악':
        sB = 505

    elif sB == '공연·예술·문화':
        sB = 506

    elif sB == '출판·인쇄·사진':
        sB = 509

    elif sB == '캐릭터·애니메이션':
        sB = 510

    elif sB == '디자인·설계':
        sB = 511

    elif sB == '초중고·대학':
        sB = 601

    elif sB == '학원·어학원':
        sB = 602

    elif sB == '유아·유치원':
        sB = 603

    elif sB == '교재·학습지':
        sB = 604

    elif sB == '전문·기능학원':
        sB = 605

    elif sB == '의료(진료과목별)':
        sB = 701

    elif sB == '의료(병원종류별)':
        sB = 702

    elif sB == '제약·보건·바이오':
        sB = 703

    elif sB == '사회복지':
        sB = 704

    elif sB == '판매(매장종류별)':
        sB = 801

    elif sB == '판매(상품품목별)':
        sB = 802

    elif sB == '유통·무역·상사':
        sB = 803

    elif sB == '운송·운수·물류':
        sB = 804

    elif sB == '건설·건축·토목·시공':
        sB = 901

    elif sB == '실내·인테리어·조경':
        sB = 902

    elif sB == '환경·설비':
        sB = 903

    elif sB == '부동산·임대·중개':
        sB = 904

    elif sB == '정부·공공기관·공기업':
        sB = 1001

    elif sB == '협회·단체':
        sB = 1002

    elif sB == '법률·법무·특허':
        sB = 1003

    elif sB == '세무·회계':
        sB = 1004

    elif sB == '연구소·컨설팅·조사':
        sB = 1005

    if sB2 == '호텔·여행·항공':
        sB2 = 108

    elif sB2 == '외식업·식음료':
        sB2 = 109

    elif sB2 == '시설관리·경비·용역':
        sB2 = 111

    elif sB2 == '레저·스포츠·여가':
        sB2 = 115

    elif sB2 == 'AS·카센터·주유':
        sB2 = 118

    elif sB2 == '렌탈·임대':
        sB2 = 119

    elif sB2 == '웨딩·장례·이벤트':
        sB2 = 120

    elif sB2 == '기타서비스업':
        sB2 = 121

    elif sB2 == '뷰티·미용':
        sB2 = 122

    elif sB2 == '전기·전자·제어':
        sB2 = 201

    elif sB2 == '기계·설비·자동차':
        sB2 = 202

    elif sB2 == '석유·화학·에너지':
        sB2 = 204

    elif sB2 == '섬유·의류·패션':
        sB2 = 205

    elif sB2 == '화장품·뷰티':
        sB2 = 207

    elif sB2 == '생활용품·소비재·사무':
        sB2 = 208

    elif sB2 == '가구·목재·제지':
        sB2 = 209

    elif sB2 == '농업·어업·광업·임업':
        sB2 = 210

    elif sB2 == '금속·재료·철강·요업':
        sB2 = 211

    elif sB2 == '조선·항공·우주':
        sB2 = 212

    elif sB2 == '기타제조업':
        sB2 = 213

    elif sB2 == '식품가공·개발':
        sB2 = 214

    elif sB2 == '반도체·광학·LCD':
        sB2 = 215

    elif sB2 == '환경':
        sB2 = 216

    elif sB2 == '솔루션·SI·ERP·CRM':
        sB2 = 301

    elif sB2 == '웹에이젼시':
        sB2 = 302

    elif sB2 == '쇼핑몰·오픈마켓':
        sB2 = 304

    elif sB2 == '포털·인터넷·컨텐츠':
        sB2 = 305

    elif sB2 == '네트워크·통신·모바일':
        sB2 = 306

    elif sB2 == '하드웨어·장비':
        sB2 = 307

    elif sB2 == '정보보안·백신':
        sB2 = 308

    elif sB2 == 'IT컨설팅':
        sB2 = 313

    elif sB2 == '게임':
        sB2 = 314

    elif sB2 == '은행·금융·저축':
        sB2 = 401

    elif sB2 == '대출·캐피탈·여신':
        sB2 = 402

    elif sB2 == '기타금융':
        sB2 = 405

    elif sB2 == '증권·보험·카드':
        sB2 = 406

    elif sB2 == '신문·잡지·언론사':
        sB2 = 501

    elif sB2 == '방송사·케이블':
        sB2 = 502

    elif sB2 == '연예·엔터테인먼트':
        sB2 = 503

    elif sB2 == '광고·홍보·전시':
        sB2 = 504

    elif sB2 == '영화·배급·음악':
        sB2 = 505

    elif sB2 == '공연·예술·문화':
        sB2 = 506

    elif sB2 == '출판·인쇄·사진':
        sB2 = 509

    elif sB2 == '캐릭터·애니메이션':
        sB2 = 510

    elif sB2 == '디자인·설계':
        sB2 = 511

    elif sB2 == '초중고·대학':
        sB2 = 601

    elif sB2 == '학원·어학원':
        sB2 = 602

    elif sB2 == '유아·유치원':
        sB2 = 603

    elif sB2 == '교재·학습지':
        sB2 = 604

    elif sB2 == '전문·기능학원':
        sB2 = 605

    elif sB2 == '의료(진료과목별)':
        sB2 = 701

    elif sB2 == '의료(병원종류별)':
        sB2 = 702

    elif sB2 == '제약·보건·바이오':
        sB2 = 703

    elif sB2 == '사회복지':
        sB2 = 704

    elif sB2 == '판매(매장종류별)':
        sB2 = 801

    elif sB2 == '판매(상품품목별)':
        sB2 = 802

    elif sB2 == '유통·무역·상사':
        sB2 = 803

    elif sB2 == '운송·운수·물류':
        sB2 = 804

    elif sB2 == '건설·건축·토목·시공':
        sB2 = 901

    elif sB2 == '실내·인테리어·조경':
        sB2 = 902

    elif sB2 == '환경·설비':
        sB2 = 903

    elif sB2 == '부동산·임대·중개':
        sB2 = 904

    elif sB2 == '정부·공공기관·공기업':
        sB2 = 1001

    elif sB2 == '협회·단체':
        sB2 = 1002

    elif sB2 == '법률·법무·특허':
        sB2 = 1003

    elif sB2 == '세무·회계':
        sB2 = 1004

    elif sB2 == '연구소·컨설팅·조사':
        sB2 = 1005

    if wT1 == "정규직":
        wT1 = 1

    elif wT1 == "계약직":
        wT1 = 2

    elif wT1 == "병역특례":
        wT1 = 3

    elif wT1 == "인턴직":
        wT1 = 4

    elif wT1 == "아르바이트":
        wT1 = 5

    elif wT1 == "파견직":
        wT1 = 6

    elif wT1 == "해외취업":
        wT1 = 7

    elif wT1 == "위촉직":
        wT1 = 8

    elif wT1 == "프리랜서":
        wT1 = 9

    elif wT1 == "교육생":
        wT1 = 12

    elif wT1 == "별정직":
        wT1 = 13

    elif wT1 == "파트":
        wT1 = 14

    elif wT1 == "전임":
        wT1 = 15

    elif wT1 == "기간제":
        wT1 = 16

    elif wT1 == "무기계약직":
        wT1 = 17

    elif wT1 == "전문계약직":
        wT1 = 18

    elif wT1 == "전문연구요원":
        wT1 = 19

    elif wT1 == "산업기능요원":
        wT1 = 20

    elif wT1 == "현역":
        wT1 = 21

    elif wT1 == "보충역":
        wT1 = 22

    if wT2 == "정규직":
        wT2 = 1

    elif wT2 == "계약직":
        wT2 = 2

    elif wT2 == "병역특례":
        wT2 = 3

    elif wT2 == "인턴직":
        wT2 = 4

    elif wT2 == "아르바이트":
        wT2 = 5

    elif wT2 == "파견직":
        wT2 = 6

    elif wT2 == "해외취업":
        wT2 = 7

    elif wT2 == "위촉직":
        wT2 = 8

    elif wT2 == "프리랜서":
        wT2 = 9

    elif wT2 == "교육생":
        wT2 = 12

    elif wT2 == "별정직":
        wT2 = 13

    elif wT2 == "파트":
        wT2 = 14

    elif wT2 == "전임":
        wT2 = 15

    elif wT2 == "기간제":
        wT2 = 16

    elif wT2 == "무기계약직":
        wT2 = 17

    elif wT2 == "전문계약직":
        wT2 = 18

    elif wT2 == "전문연구요원":
        wT2 = 19

    elif wT2 == "산업기능요원":
        wT2 = 20

    elif wT2 == "현역":
        wT2 = 21

    elif wT2 == "보충역":
        wT2 = 22

    if edu == "학력무관":
        edu = 0

    elif edu == "고등학교졸업":
        edu = 1

    elif edu == "대학졸업(2,3년)":
        edu = 2

    elif edu == "대학교졸업(4년)":
        edu = 3

    elif edu == "석사졸업":
        edu = 4

    elif edu == "박사졸업":
        edu = 5

    elif edu == "고등학교졸업이상":
        edu = 6

    elif edu == "대학졸업(2,3년)이상":
        edu = 7

    elif edu == "대학교졸업(4년)이상":
        edu = 8

    elif edu == "석사졸업이상":
        edu = 9

    keyword = k

    screenclear()

    loL = []
    if (str(sR1) != ""):
        loL.append(str(sR1))
    if (str(sR2) != ""):
        loL.append(str(sR2))
    if (str(sR3) != ""):
        loL.append(str(sR3))
    lo = ', '.join(loL)

    bL = []
    bL.append(str(b))
    if (str(sB) != ""):
        loL.append(str(sB))
    if (str(b2) != ""):
        loL.append(str(b2))
    if (str(sB2) != ""):
        loL.append(str(sB2))
    business = ', '.join(bL)

    workTypeL = []
    if (str(wT1) != ""):
        workTypeL.append(str(wT1))
    if (str(wT2) != ""):
        workTypeL.append(str(wT2))
    workType = ', '.join(workTypeL)

    eduType = str(edu)

    count = checking()

    param = {"keywords": keyword, "loc_cd": lo, "count": 10, "ind_cd": business, "job_type": workType,
             "edu_lv": eduType}
    response = requests.get(url, params=param)
    job_dic = response.json()


    print(keyword)
    print(lo)
    print(business)
    print(workType)
    print(eduType)
    print("압력하신 조건에 해당하는 공고 검색을 시작합니다..")
    print()
    print("총", job_dic['jobs']['total'], "개의 공고가 검색되었습니다!")

    for s in range(0, count):
        display(s)
        print("-------", count, "페이지 중 ", s + 1, "페이지 표시 완료 -------")
        print()
        if (s + 1 == count):
            break
            print("MyJob 프로그램을 종료합니다.")
        else:
            wantExit = input("다음 페이지로 이어서 열람하시겠습니까? (Y/N): ")
            if (wantExit == "Y" or wantExit == "y"):
                continue
            else:
                break
                print("MyJob 프로그램을 종료합니다.")


def screenclear():
    if (pf.startswith('mac') | pf.startswith('darwin') == True):
        os.system('clear')
    else:
        os.system('cls')


def checking():
    # 체크용
    param = {"keywords": keyword, "loc_cd": lo, "count": 10, "ind_cd": business, "job_type": workType,
             "edu_lv": eduType}
    response = requests.get(url, params=param)
    job_dic = response.json()
    count = int(job_dic['jobs']['total'])
    if (count % 10 == 0):
        count = int(count / 10)
    else:
        count = int(count / 10) + 1

    return count
    # 체크용 끝


def display(s):
    i = 0
    param = {"keywords": keyword, "loc_cd": lo, "count": 10, "ind_cd": business, "job_type": workType,
             "edu_lv": eduType}
    response = requests.get(url, params=param)
    job_dic = response.json()
    jobList = job_dic['jobs']['job']
    while (True):
        try:
            check = jobList[i]  # 표시할 공고가 더 있는지 확인
            print()
            print(i + 1, "번째 공고입니다.")
            print("사명: ", jobList[i]['company']['detail']['name']) # 사명
            print("공고명: ", jobList[i]['position']['title'])  # 공고명
            print("지역: ", str(jobList[i]['position']['location']['name']).replace("&gt;",""))  # 지역
            print("산업/업종: ", jobList[i]['position']['job-mid-code']['name'])  # 산업/업종
            print("세부 산업/업종: ", jobList[i]['position']['job-code']['name'])  # 세부 산업/업종
            print()
            i = i + 1
        except IndexError:
            break
