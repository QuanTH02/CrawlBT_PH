import os
import time
import pyautogui

def duyet_thu_muc(duong_dan):
    tieptuc = 0
    for thu_muc_goc, thu_muc_con, tap_tin in os.walk(duong_dan):
        # print(thu_muc_goc)
        if tap_tin:
            for ten_tap_tin in tap_tin:
                

                
                duong_dan_tep_tin = os.path.join(thu_muc_goc, ten_tap_tin)

                time.sleep(1)
                os.startfile(duong_dan_tep_tin)

                time.sleep(1)
                pyautogui.keyDown('ctrl')
                pyautogui.press('a')
                pyautogui.keyUp('a')
                pyautogui.keyUp('ctrl')
                
                time.sleep(1)
                pyautogui.keyDown('ctrl')
                pyautogui.press('c')
                pyautogui.keyUp('c')
                pyautogui.keyUp('ctrl')

                time.sleep(1)
                duongdancu = duong_dan_tep_tin
                duong_dan_tep_moi = duongdancu.replace('.html', '.docx')

                with open(duong_dan_tep_moi, 'w'):
                    pass
                
                time.sleep(1)

                os.startfile(duong_dan_tep_moi)
                time.sleep(5)

                pyautogui.keyDown('ctrl')
                pyautogui.press('v')
                pyautogui.keyUp('v')
                pyautogui.keyUp('ctrl')
                time.sleep(12)

                pyautogui.keyDown('ctrl')
                pyautogui.press('s')
                pyautogui.keyUp('s')
                pyautogui.keyUp('ctrl')
                time.sleep(3)

                click_close_button()
                time.sleep(1)
                click_close_button()
                time.sleep(1)
                # time.sleep(2)


def click_close_button():
    screen_width, screen_height = pyautogui.size()
    close_button_position = (screen_width - 10, 10)  # Điều chỉnh tọa độ tùy thuộc vào kích thước của màn hình
    pyautogui.click(close_button_position)


# file_path = "html.html"

# try:
#     os.startfile(file_path)
# except FileNotFoundError:
#     print("Không tìm thấy tệp tin!")
# except Exception as e:
#     print(f"Có lỗi xảy ra: {e}")

# time.sleep(2)  # Chờ trang web được tải

# click_close_button()  # Gọi hàm để nhấn vào nút close ở góc phải màn hình


duong_dan = 'VioEdu/Khối 3'

duyet_thu_muc(duong_dan)