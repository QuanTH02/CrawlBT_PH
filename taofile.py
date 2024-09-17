import time
from bs4 import BeautifulSoup
import docx
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from docx import Document
from docx.shared import Inches
import requests
from io import BytesIO
import urllib3
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def clean_folder_name(folder_name):
    invalid_chars = ['?', '*', ':', '"', '<', '>', '|', '/']
    for char in invalid_chars:
        folder_name = folder_name.replace(char, '')
    return folder_name

def html_to_docx(html_string, output_path):
    soup = BeautifulSoup(html_string, 'html.parser')

    # Tìm tất cả các phần tử chứa chuỗi "ĐÁP ÁN ĐÚNG: "
    correct_answer_elements = soup.find_all(string=lambda text: 'ĐÁP ÁN ĐÚNG: ' in text)
    # print("Số đáp án đúng: " + str(len(correct_answer_elements)))
    placeholder_element = soup.find_all(string=lambda text: '{}' in text)
    # print("Số dấu ngoặc nhọn: " + str(len(placeholder_element)))
    j = 0
    # Danh sách để lưu trữ các kết quả
    results = []

    # Lặp qua từng phần tử tìm được
    for correct_answer_element in correct_answer_elements:    
        correct_answer = correct_answer_element.parent.get_text(strip=True)
        # print(correct_answer)

        result_correct = correct_answer.split('ĐÁP ÁN ĐÚNG:')[1].strip()
        if "," in result_correct:
            result_values = result_correct.split(',')
            for result_value in result_values:
                # print("j = " + str(j))
                # placeholder_element[j].replace_with(placeholder_element[j].replace("{}", "[[" + result_value.strip() + "]]"))
                results.append(result_value.strip())            
                j+=1
        else:
            # placeholder_element[j].replace_with(placeholder_element[j].replace("{}", "[[" + result_correct.strip() + "]]"))
            results.append(result_correct.strip())    
            j+=1

        correct_answer_element.parent.extract()
        
    # print(len(results))
    # Thay đổi {}
    index = 0
    # Duyệt qua tất cả các phần tử trong danh sách `soup.find_all()`
    for tag in soup.find_all(string=lambda text: '{}' in text):
        if tag.count("{}") > 1:
            # Thực hiện thay thế toàn bộ placeholder cùng một lúc
            new_string = tag.format(*["[[" + value + "]]" for value in results[index:index+tag.count("{}")]])
            tag.replace_with(new_string)
            index += tag.count("{}")
        else:
            # Thay thế nội dung của tag trực tiếp
            new_string = tag.replace("{}", "[[" + results[index] + "]]")
            tag.replace_with(new_string)
            index += 1

    # CÂU TRẢ LỜI
    panel_body_divs = soup.find_all('div', class_='panel-body')

    # Duyệt qua từng thẻ <div>
    for div in panel_body_divs:
        # Tìm tất cả các thẻ <li> trong thẻ <div> này
        li_elements = div.find_all('li', class_='answerChoice')
        # In ra nội dung của các thẻ <li> tìm được
        k = 1
        for li in li_elements:
            if k == 1:
                if 'correctAnswer' in li['class']:
                    # Nếu là câu trả lời đúng
                    text_content = li.text.strip()
                    div_tag = soup.new_tag("div")  # Tạo thẻ <div>
                    u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                    u_tag.string = "A."  # Đặt nội dung của thẻ <u>
                    div_tag.append(u_tag)  # Thêm thẻ <u> vào trong thẻ <div>
                    div_tag.append(text_content)  # Thêm nội dung còn lại vào trong thẻ <div>
                    li.replace_with(div_tag)
                else:
                    text_content = "A. " + li.text.strip()
                    li.replace_with(text_content)
            elif k == 2:
                if 'correctAnswer' in li['class']:
                    # Nếu là câu trả lời đúng
                    text_content = li.text.strip()
                    div_tag = soup.new_tag("div")  # Tạo thẻ <div>
                    u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                    u_tag.string = "B."  # Đặt nội dung của thẻ <u>
                    div_tag.append(u_tag)  # Thêm thẻ <u> vào trong thẻ <div>
                    div_tag.append(text_content)  # Thêm nội dung còn lại vào trong thẻ <div>
                    li.replace_with(div_tag)
                else:
                    text_content = "B. " + li.text.strip()
                    li.replace_with(text_content)
            elif k == 3:
                if 'correctAnswer' in li['class']:
                    # Nếu là câu trả lời đúng
                    text_content = li.text.strip()
                    div_tag = soup.new_tag("div")  # Tạo thẻ <div>
                    u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                    u_tag.string = "C."  # Đặt nội dung của thẻ <u>
                    div_tag.append(u_tag)  # Thêm thẻ <u> vào trong thẻ <div>
                    div_tag.append(text_content)  # Thêm nội dung còn lại vào trong thẻ <div>
                    li.replace_with(div_tag)
                else:
                    text_content = "C. " + li.text.strip()
                    li.replace_with(text_content)
            elif k == 4:
                if 'correctAnswer' in li['class']:
                    # Nếu là câu trả lời đúng
                    text_content = li.text.strip()
                    div_tag = soup.new_tag("div")  # Tạo thẻ <div>
                    u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                    u_tag.string = "D."  # Đặt nội dung của thẻ <u>
                    div_tag.append(u_tag)  # Thêm thẻ <u> vào trong thẻ <div>
                    div_tag.append(text_content)  # Thêm nội dung còn lại vào trong thẻ <div>
                    li.replace_with(div_tag)
                else:
                    text_content = "D. " + li.text.strip()
                    li.replace_with(text_content)
            k += 1


    # Thay thế giải thích và xem lời giải
    xemgiaithich_elements = soup.find_all(string=lambda text: 'Xem giải thích' in text)
    loigiai_elements = soup.find_all(string=lambda text: 'Lời giải:' in text)

    for loigiai_element in loigiai_elements:
        loigiai_element.replace_with("")

    for xemgiaithich_element in xemgiaithich_elements:
        xemgiaithich_element.replace_with("Lời giải:")

    # Thay thế câu hỏi
    cauhoi_elements = soup.find_all(string=lambda text: 'Câu hỏi ' in text)
    for cauhoi_element in cauhoi_elements:
        cauhoi_element.replace_with("Câu ")

    # Thay thế Nhận biết, nâng cao, ...
    trinhdo_elements = soup.find_all(string=lambda text: 'NHẬN BIẾT' in text)
    for trinhdo_element in trinhdo_elements:
        trinhdo_element.replace_with(": [NB]")

    trinhdo_elements = soup.find_all(string=lambda text: 'THÔNG HIỂU' in text)
    for trinhdo_element in trinhdo_elements:
        trinhdo_element.replace_with(": [TH]")

    trinhdo_elements = soup.find_all(string=lambda text: 'VẬN DỤNG' in text)
    for trinhdo_element in trinhdo_elements:
        trinhdo_element.replace_with(": [VD]")

    trinhdo_elements = soup.find_all(string=lambda text: 'VẬN DỤNG CAO' in text)
    for trinhdo_element in trinhdo_elements:
        trinhdo_element.replace_with(": [VDC]")

    # Xóa "Chọn câu hỏi"
    choncauhoi_elements = soup.find_all(string=lambda text: 'Chọn câu hỏi' in text)
    for choncauhoi_element in choncauhoi_elements:
        choncauhoi_element.replace_with("")

    # Ghi cấu trúc HTML đã thay đổi vào file html.txt
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(soup.prettify())



driver = webdriver.Chrome()
driver.maximize_window()
page_main_url = "https://vio.edu.vn/login"
driver.get(page_main_url)
doc = Document()
# Chờ 2 giây để trang web tải hoàn chỉnh
time.sleep(1)

# Lấy các phần tử input
username_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div/form/div[1]/div/div/div/input')
password_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div/form/div[2]/div/div/div/div[1]/input')

# Điền thông tin vào các input
username_input.send_keys("anhquankaka113@gmail.com")
password_input.send_keys("anhquankaka113")
time.sleep(1)
# Lấy nút đăng nhập
login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div/div/div/div/form/div[4]/button')

# Click vào nút đăng nhập
login_button.click()
time.sleep(2)
# Đợi 2 giây để kiểm tra dữ liệu đã được điền vào form


driver.get("https://vio.edu.vn/create-homework")
time.sleep(1)
tenbaivenha_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[1]/div/div/input')
tenbaivenha_input.send_keys("Test123")
time.sleep(1)

ngayketthuc_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/input')
ngayketthuc_input.send_keys("10-02-2024")
time.sleep(7)

# Lấy nút đăng nhập
tieptuc_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[5]/button')
time.sleep(1)


# Tạo thư mục khối
thumuc_khoi = driver.find_element(By.XPATH, '//*[@id="react-select-2--value-item"]')
tenkhoi = thumuc_khoi.text
# print("Khối")

# Click vào nút đăng nhập
tieptuc_button.click()


time.sleep(2)

if (tenkhoi == "Khối 1"):
    tenkhoahoc = "Toán 1 (VioEdu)\n"
elif (tenkhoi == "Khối 2"):
    tenkhoahoc = "Toán 2 (VioEdu)\n"
elif (tenkhoi == "Khối 3"):
    tenkhoahoc = "Toán 3 (VioEdu)\n"
elif (tenkhoi == "Khối 4"):
    tenkhoahoc = "Toán 4 (VioEdu)\n"
elif (tenkhoi == "Khối 5"):
    tenkhoahoc = "Toán 5 (VioEdu)\n"

tenselect = "Học kì 1\n"

print(tenkhoahoc)
print(tenselect)

# Đóng thẻ tự select ra
dongthe = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[1]")
dongthe.click()


div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
# print("Chủ Đề")          
chude = []                
stt_chude = 1                            
for div in div_baitap_elements:
    tenchude = div.text
    tenchude = clean_folder_name(tenchude)
    # Kiểm tra xem thư mục đã tồn tại hay chưa
    tenchude = tenchude.lower().capitalize()
    tenchude = "Chủ đề " + str(stt_chude) + ": " + tenchude + "\n"
    chude.append(tenchude)
    stt_chude += 1

div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
indexxx = 0
for div in div_baitap_elements:
    print(chude[indexxx])
    img_element = div.find_element(By.TAG_NAME, "div")
    img_element.click()

    time.sleep(1)

    div_click_baitap_elements = driver.find_elements(By.CSS_SELECTOR, "div[style='color: rgb(46, 58, 89); font-size: 16px; margin: 6px 5px 6px 15px; display: flex; align-items: center; cursor: pointer;']")

    dem = 1
    stt_chudiem = 1
    chudiem = []
    mucdo_chudiem = []

    index_chudiem = 0
    for div in div_click_baitap_elements:
        
        # print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        # tenchudiem += "\n"
        chudiem.append(tenchudiem)

        print(tenchudiem)

        mucdo_chudiem.append("(NB) " + tenchudiem)
        mucdo_chudiem.append("(TH) " + tenchudiem)
        mucdo_chudiem.append("(VD) " + tenchudiem)
        mucdo_chudiem.append("(VDC) " + tenchudiem)

        print("(NB) " + tenchudiem)
        print("(TH) " + tenchudiem)
        print("(VD) " + tenchudiem)
        print("(VDC) " + tenchudiem + "\n")


    indexxx += 1
    img_element.click()
    time.sleep(1)


hk2_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div[2]")
hk2_element.click()

print("Học kì 2\n")

time.sleep(2)
# Đóng thẻ tự select ra
dongthe1 = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[1]")                    
dongthe1.click()


div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
# print("Chủ Đề")          
chude = []                
stt_chude = 1                            
for div in div_baitap_elements:
    tenchude = div.text
    tenchude = clean_folder_name(tenchude)
    # Kiểm tra xem thư mục đã tồn tại hay chưa
    tenchude = tenchude.lower().capitalize()
    tenchude = "Chủ đề " + str(stt_chude) + ": " + tenchude + "\n"
    chude.append(tenchude)
    stt_chude += 1

div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
indexxx = 0
for div in div_baitap_elements:
    print(chude[indexxx])
    img_element = div.find_element(By.TAG_NAME, "div")
    img_element.click()

    time.sleep(1)

    div_click_baitap_elements = driver.find_elements(By.CSS_SELECTOR, "div[style='color: rgb(46, 58, 89); font-size: 16px; margin: 6px 5px 6px 15px; display: flex; align-items: center; cursor: pointer;']")

    dem = 1
    stt_chudiem = 1
    chudiem = []
    mucdo_chudiem = []

    index_chudiem = 0
    for div in div_click_baitap_elements:
        
        # print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        # tenchudiem += "\n"
        chudiem.append(tenchudiem)

        print(tenchudiem)

        mucdo_chudiem.append("(NB) " + tenchudiem)
        mucdo_chudiem.append("(TH) " + tenchudiem)
        mucdo_chudiem.append("(VD) " + tenchudiem)
        mucdo_chudiem.append("(VDC) " + tenchudiem)

        print("(NB) " + tenchudiem)
        print("(TH) " + tenchudiem)
        print("(VD) " + tenchudiem)
        print("(VDC) " + tenchudiem + "\n")


    indexxx += 1
    img_element.click()
    time.sleep(1)
    # div.click()
    # time.sleep(4)

    # mucdo = 1
    # while mucdo < 5:
    #     # Nhấn button select ra Lời giải
    #     div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
    #     # print(len(div_button_elements))               
    #     for div_btn in div_button_elements:
    #         if div_btn.find_element(By.TAG_NAME, "div"):
    #             button_elements = div_btn.find_element(By.TAG_NAME, "button")
    #             driver.execute_script("arguments[0].click();", button_elements)
            
    #     time.sleep(3)

    #     # Lấy thẻ div lớn lấy nội dung cần copy
    #     copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
    #     script = "return arguments[0].innerHTML;"
    #     content = driver.execute_script(script, copy_all_element)
    #     # print(content)

    #     # Thay đổi nội dung phân số
    #     # numerator_tags = div.find_elements(By.CLASS_NAME, 'mjx-numerator')
    
    #     # for numerator_tag in numerator_tags:
    #     #     # Thêm dấu '/' vào cuối văn bản trong thẻ
    #     #     numerator_tag.string = str(numerator_tag.string) + '/' 


    #     if mucdo == 1:
    #         dienmucdo = "_NB"
    #     elif mucdo == 2:
    #         dienmucdo = "_TH"
    #     elif mucdo == 3:
    #         dienmucdo = "_VD"
    #     elif mucdo == 4:
    #         dienmucdo = "_VDC"
        
    #     output_path = "VioEdu" + "/" + tenkhoi + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + tenchudiem + dienmucdo + ".txt"
        
    #     # Chuyển đổi HTML thành tập tin Word
    #     html_to_docx(content, output_path)

    #     if mucdo == 1:
    #         to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]")
    #         driver.execute_script("arguments[0].click();", to_mucdo_element)
    #     elif mucdo == 2:
    #         to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]")
    #         driver.execute_script("arguments[0].click();", to_mucdo_element)
    #     elif mucdo == 3:
    #         to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[4]")
    #         driver.execute_script("arguments[0].click();", to_mucdo_element)
    #     mucdo += 1   
    #     time.sleep(2)                                         

    # close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
    # driver.execute_script("arguments[0].click();", close_element)
    # time.sleep(2)

    # # dem += 1
    # # if dem == 3:
    # #     break
    
time.sleep(1)

indexx = 0

# with open("cautructhumuc.txt", "w", encoding="utf-8") as file:
#     file.write(tenkhoahoc)
#     file.write(tenselect)

#     for cd in chude:
#         file.write(cd)
#         for cdiem in chudiem:
#             file.write(cdiem)
#             for mucdo in mucdo_chudiem:
#                 file.write(mucdo)
    

# Tắt trình duyệt
driver.quit()
