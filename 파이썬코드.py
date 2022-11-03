def addition(item_list, item):
    if item in item_list:
        item_list[item] += 1
    else:
        item_list[item] = 1
    return item_list

def yesorno():
    n = input("추가 구매하시겠습니까? 맞으시면 y 아니시면 아무키나 입력해주세요 : ")
    return n 
def memory_size():
    print("-------------------")
    print("|64G | 128G | 256G |")
    print("-------------------")
def iphone_memory_size():
    print("----------------------")
    print("| 128G | 256G | 512G |")
    print("----------------------")
def mac_memory_size():
    print("-----------------")
    print("| 256G | 512G |")
    print("-----------------")
def ipad_type():
    print("-------------------------------")
    print("미니 | 10세대 | Pro11 | Air5 |")
    print("-------------------------------")
def pad_memory_size12():
    print("---------------")
    print("| 64G | 256G |")
    print("---------------")
def ipad_memory_size():
    print("----------------------")
    print("| 128G | 256G | 512G |")
    print("----------------------")
def iphone_type():
    print("-------------------------------")
    print("| 14 | 14+ | 14Pro | 14ProMax |")
    print("-------------------------------")
def watch_type():
    print("---------------------------")
    print("| 울트라 | 워치8 | 워치SE |")
    print("---------------------------")
def colors():
    print("-------------------------")
    print("|그레이 | 블랙 | 화이트 |")
    print("-------------------------")    
def airpod_gens():
    print("----------------------------")
    print("|2세대 | 3세대 | Pro | Max |")
    print("----------------------------")
def mac_gens():
    print("-------------")
    print("| Air | Pro |")
    print("-------------")

money = 0
num = 0
yes_no = "y"
item_list = {}
print("---------------------------------------------")

print("""              .:'
                   __ :'__
                .'`  `-'  ``.
               :          .-'
               :         :
                :         `-;
            ...  `.__.-.__.'
            
,adPPYYba, 8b,dPPYba,  8b,dPPYba,  88  ,adPPYba,  
""     `Y8 88P'    "8a 88P'    "8a 88 a8P_____88    
,adPPPPP88 88       d8 88       d8 88 8PP"""""""  
88,    ,88 88b,   ,a8" 88b,   ,a8" 88 "8b,   ,aa  
`"8bbdP"Y8 88`YbbdP"'  88`YbbdP"'  88  `"Ybbd8"'  
           88          88                         
           88          88


           """)
print("안녕하세요 애플스토어에 오신 것을 환영합니다 ")
print("---------------------------------------------")
while True:
    print()
    print("---------------- 구매 물품 ------------------")
    print("아이폰")
    print("---- 14 128G 125만원")
    print("---- 14 256G 140만원")
    print("---- 14 512G 170만원")
    print("---- 14+ 128G 135만원")
    print("---- 14+ 256G 150만원")
    print("---- 14+ 512G 180만원")
    print("---- 14Pro 128G 155만원")
    print("---- 14Pro 256G 170만원")
    print("---- 14Pro 512G 200만원")
    print("---- 14ProMax 128G 175만원")
    print("---- 14ProMax 256G 190만원")
    print("---- 14ProMax 512G 220만원")
    print("아이패드")
    print("---- 미니 64G 77만원")
    print("---- 미니 256G 100만원")
    print("---- 10세대 64G 68만원")
    print("---- 10세대 256G 92만원")
    print("---- Air5 64G 93만원")
    print("---- Air5 256G 120만원")
    print("---- Pro11 128G 125만원")
    print("---- Pro11 256G 140만원")
    print("---- Pro11 512G 170만원")
    print("맥북")
    print("---- Air 256G 170만원")
    print("---- Air 512G 200만원")
    print("---- Pro 256G 270만원")
    print("---- Pro 512G 330만원")
    print("애플워치")
    print("---- 울트라 150만원")
    print("---- 워치8 60만원")
    print("---- 워치SE 36만원")
    print("에어팟")
    print("---- 2세대 18만원")
    print("---- 3세대 25만원")
    print("---- Pro 33만원")
    print("---- Max 72만원")
    print("기타용품 (충전기, 이어폰, 케이스등) 각각 2만원 ")
    print("--------------------------------------------- ")
    n = input("입력 : ")
    if n == "아이폰":
        iphone_memory_size()
        memory = input("원하시는 용량을 입력해주세요 : ")
        iphone_type()
        pType = input("원하시는 기종을 입력해주세요 : ")
        colors()
        color = input("원하시는 색상을 입력해주세요 : ")
        num = int(input("몇 개를 구매하시겠습니까? : "))
        for i in range(num):
            item_list = addition(item_list, n)  
        if memory == "128":
            if pType == "14":
                money += (125 * num)
            if pType == "14+":
                money += (135 * num)
            if pType == "14Pro":
                money += (155 * num)
            if pType == "14ProMax":
                money += (175 * num)
        elif memory == "256":
            if pType == "14":
                money += (140 * num)
            if pType == "14+":
                money += (150 * num)
            if pType == "14Pro":
                money += (170 * num)
            if pType == "14ProMax":
                money += (190 * num)
        else:
            if pType == "14":
                money += (170 * num)
            if pType == "14+":
                money += (180 * num)
            if pType == "14Pro":
                money += (200 * num)
            if pType == "14ProMax":
                money += (220 * num)
    elif n =="아이패드":
        ipad_type()
        pType = input("원하시는 기종을 입력해주세요 : ")
        if pType == "미니":
            pad_memory_size12()
            memory = input("원하시는 용량을 입력해주세요 : ")
        elif pType == "10세대":
            pad_memory_size12()
            memory = input("원하시는 용량을 입력해주세요 : ")
        elif pType == "Air5":
            pad_memory_size12()
            memory = input("원하시는 용량을 입력해주세요 : ")
        else:
            ipad_memory_size()
            memory = input("원하시는 용량을 입력해주세요 : ")
        colors()
        color = input("원하시는 색상을 입력해주세요 : ")
        num = int(input("몇 개를 구매하시겠습니까? : "))
        for i in range(num):
            item_list = addition(item_list, n)  
        if memory == "64":
            if pType == "미니":
                money += (77 * num)
            elif pType == "10세대":
                money += (68 * num)
            else:
                money += (93 * num)
        elif memory == "128":
            money += (125 * num)
        elif memory == "256":
            if pType == "미니":
                money += (100 * num)
            elif pType == "10세대":
                money += (92 * num)
            elif pType == "Air5":
                money += (120 * num)
            else:
                money += (140 * num)
        else:
            money += (170 * num)
    elif n=="맥북":
        mac_memory_size()
        memory = input("원하시는 용량을 입력해주세요 : ")
        mac_gens()
        gen = input("원하시는 모델을 입력해주세요 : ")
        colors()
        color = input("원하시는 색상을 입력해주세요 : ")
        num = int(input("몇 개를 구매하시겠습니까? : "))
        for i in range(num):
            item_list = addition(item_list, n)  

        if memory == "256":
            if gen == "Air":
                money += (170 * num)
            elif gen == "Pro":
                money += (270 * num)
        else:
            if gen == "Air":
                money += (200 * num)
            elif gen == "Pro":
                money += (330 * num)
    elif n == "애플워치":
        watch_type()
        wt = input("원하시는 모델을 입력해주세요 : ")
        num = int(input("몇 개를 구매하시겠습니까? : "))
        for i in range(num):
            item_list = addition(item_list, n)
        if wt == "울트라":
            money += (150 * num)
        elif wt == "워치8":
            money += (60 * num)
        elif wt == "워치SE":
            money += (36 * num)
    elif n =="에어팟":
        airpod_gens()
        airpodGen = input("원하시는 모델을 입력해주세요 : ")
        num = int(input("몇 개를 구매하시겠습니까? : "))
        for i in range(num):
            item_list = addition(item_list, n)
        
        if airpodGen == "2세대":
            money += (18 * num)
        elif airpodGen == "3세대":
            money += (25 * num)
        elif airpodGen == "Pro":
            money += (33 * num)
        else:
            money += (72 * num)

    elif n =="기타용품":
        m = input("어떤 기타용품을 구매하시겠습니까? : ")
        if m == "충전기":
            num = int(input("몇 개를 구매하시겠습니까? : "))
            for i in range(num):
                item_list = addition(item_list, n)
                money += 2

        elif m=="이어폰":
            num = int(input("몇 개를 구매하시겠습니까? : "))
            for i in range(num):
                item_list = addition(item_list, n)
                money += 2
                
        elif m=="케이스":
            num = int(input("몇 개를 구매하시겠습니까? : "))
            for i in range(num):
                item_list = addition(item_list, n)
                money += 2
        else:
            print("잘못 입력하셨습니다.")
    else:
        print("잘못 입력하셨습니다.")
    
    yes_no = yesorno()
    if yes_no != 'y':
        for item, count in item_list.items():
            print(item,":",count,"개")
        print(".∧＿∧　  　　　 ∧＿∧   ")
        print("(*･ω･ヾ  ⌒∨⌒ヽ･ω･*) ")
        print("( 　 ⊃( 하　트 )  ⊂) ")
        print("(＿＿⊃  ＼_ _／⊂＿＿) ")

        print("감사합니다 총 구매금액은 %d만원입니다."%money)
        break
            
