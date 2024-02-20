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
    invalid_chars = ['?', '*', ':', '"', '<', '>', '|', '/', '.', ',']
    for char in invalid_chars:
        folder_name = folder_name.replace(char, '')
    return folder_name

def clean_file_name(file_name):
    invalid_chars = ['?', '*', ':', '"', '<', '>', '|', '/', '.', ',']
    for char in invalid_chars:
        file_name = file_name.replace(char, '')
    return file_name[:55]



def html_to_docx(html_string, output_path):
    # Ghi file trống
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("")
    
    html_string = html_string.replace("Đề", "Đê`")
    html_string = html_string.replace("A.", "A,")
    html_string = html_string.replace("B.", "B,")
    html_string = html_string.replace("C.", "C,")
    html_string = html_string.replace("D.", "D,")
    html_string = html_string.replace("E.", "E,")

    soup = BeautifulSoup(html_string, 'html.parser')

    

    # if span_maths:
    #     p_tag = soup.find("p", class_="default_cursor_cs")
    #     p_text = soup.new_tag("p")
    #     p_text = p_tag
    #     new_p_text = p_text.text.replace("A", "A")
    #     p_tag.string = new_p_text

    #     print(p_tag)


    div_all = soup.find_all("div", recursive=False)
    # print(len(div_child))

    div_childs = div_all[0].find_all("div", recursive=False)
    # print(len(div_childs))
    
    print(len(div_childs))
    print("Chủ điểm mới")
    for div_child in div_all:
        print("Duyệt")
        # Xử lý A. B. C. D.
        span_maths = div_child.find_all("span", class_="math-tex")
        for span_math in span_maths:
            # Xử lý "PHÂN SỐ"
            tuso_tags = span_math.find_all(class_="mjx-numerator")
            if tuso_tags:
                mauso_tags = span_math.find_all(class_="mjx-denominator")

                for tuso_tag, mauso_tag in zip(tuso_tags, mauso_tags):
                    div_phanso = soup.new_tag("span")

                    new_tuso_tag = soup.new_tag("sup")
                    new_mauso_tag = soup.new_tag("sub")

                    new_tuso_tag.string = tuso_tag.text
                    new_mauso_tag.string = mauso_tag.text

                    div_phanso.append(new_tuso_tag)
                    div_phanso.append("/")
                    div_phanso.append(new_mauso_tag)

                    # tuso_tag.replace_with(new_tuso_tag)
                    # # tuso_tag.insert_after("/")
                    # mauso_tag.replace_with(new_mauso_tag)

                    tuso_tag.replace_with(div_phanso)
                    mauso_tag.clear()

                    
            else:
                # Truy cập vào nội dung văn bản của thẻ span
                span_text = soup.new_tag("span")
                span_text = span_math
                # Thực hiện thay thế trong nội dung văn bản
                new_span_text = span_text.text.replace("A", "a")
                new_span_text = new_span_text.replace("B", "b")
                new_span_text = new_span_text.replace("C", "c")
                new_span_text = new_span_text.replace("D", "d")
                new_span_text = new_span_text.replace("E", "e")
                # Thay đổi nội dung văn bản của thẻ span
                span_math.string = new_span_text

                # print(span_math)

        

        # Xử lý "SẮP XẾP"
        if "sắp xếp" in div_child.text.lower() and "{}" not in div_child.text.lower():
            panel_body_div_sx = div_child.find("div", class_="panel-body")

            flex_divs = panel_body_div_sx.find_all("div", class_="default_cursor_cs", style="display: flex;")

            for flex_div in flex_divs:
                answer_sx = soup.new_tag("div")
                answer_sx.string = "[(" + flex_div.text + ")]"
                flex_div.replace_with(answer_sx)

                # print(flex_div.text)
            
            # print("\n")

        # Tìm tất cả các phần tử chứa chuỗi "ĐÁP ÁN ĐÚNG: "
        correct_answer_elements = div_child.find_all(string=lambda text: 'ĐÁP ÁN ĐÚNG: ' in text)
        # print("Số đáp án đúng: " + str(len(correct_answer_elements)))
        placeholder_element = div_child.find_all(string=lambda text: '{}' in text)
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

            # Xóa đáp án đúng
            correct_answer_element.parent.extract()
            
        # print(len(results))
        # Thay đổi {}
        index = 0
        # Duyệt qua tất cả các phần tử trong danh sách `div_child.find_all()`
        for tag in div_child.find_all(string=lambda text: '{}' in text):
            if tag.count("{}") > 1:
                # Thực hiện thay thế toàn bộ placeholder cùng một lúc
                new_string = tag.format(*["[[" + value + "]]" for value in results[index:index+tag.count("{}")]])
                tag.replace_with(new_string)
                index += tag.count("{}")
            else:
                # Thay thế nội dung của tag trực tiếp
                if results[index]:
                    new_string = tag.replace("{}", "[[" + results[index] + "]]")
                    tag.replace_with(new_string)
                    index += 1
                else:
                    return

        # CÂU TRẢ LỜI
        panel_body_divs = div_child.find_all('div', class_='panel-body')

        
        # Duyệt qua từng thẻ <div>
        for div in panel_body_divs:
            # Tìm tất cả các thẻ <li> trong thẻ <div> này
            li_elements = div.find_all('li', class_='answerChoice')
            # In ra nội dung của các thẻ <li> tìm được
            k = 1
            for li in li_elements:
                if k == 1:
                    if 'correctAnswer' in li['class']:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                        u_tag.string = "A."  # Đặt nội dung của thẻ <u>        
                        div_tag.append(u_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)                
                    else:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        p_tag = soup.new_tag("p")  # Tạo thẻ <p> mới
                        p_tag.string = "A. "  # Đặt nội dung cho thẻ <p>
                        div_tag.append(p_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)              
                elif k == 2:
                    if 'correctAnswer' in li['class']:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                        u_tag.string = "B."  # Đặt nội dung của thẻ <u>        
                        div_tag.append(u_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)  
                    else:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        p_tag = soup.new_tag("p")  # Tạo thẻ <p> mới
                        p_tag.string = "B. "  # Đặt nội dung cho thẻ <p>
                        div_tag.append(p_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)                            
                elif k == 3:
                    if 'correctAnswer' in li['class']:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                        u_tag.string = "C."  # Đặt nội dung của thẻ <u>        
                        div_tag.append(u_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)  
                    else:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        p_tag = soup.new_tag("p")  # Tạo thẻ <p> mới
                        p_tag.string = "C. "  # Đặt nội dung cho thẻ <p>
                        div_tag.append(p_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)    
                elif k == 4:
                    if 'correctAnswer' in li['class']:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                        u_tag.string = "D."  # Đặt nội dung của thẻ <u>        
                        div_tag.append(u_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)  
                    else:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        p_tag = soup.new_tag("p")  # Tạo thẻ <p> mới
                        p_tag.string = "D. "  # Đặt nội dung cho thẻ <p>
                        div_tag.append(p_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)     
                elif k == 5:
                    if 'correctAnswer' in li['class']:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        u_tag = soup.new_tag("u")  # Tạo thẻ <u>
                        u_tag.string = "E."  # Đặt nội dung của thẻ <u>        
                        div_tag.append(u_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)  
                    else:
                        div_tag = soup.new_tag("div")  # Tạo thẻ <div> mới
                        li.insert_before(div_tag)  # Chèn thẻ <div> vào trước thẻ <li>

                        p_tag = soup.new_tag("p")  # Tạo thẻ <p> mới
                        p_tag.string = "E. "  # Đặt nội dung cho thẻ <p>
                        div_tag.append(p_tag)  # Thêm thẻ <p> vào trong thẻ <div>

                        # Sao chép nội dung từ thẻ <li> sang thẻ <div>
                        for child in li.children:
                            div_tag.append(child.extract())

                        li.replace_with(div_tag)    
                k += 1


        # Thay thế giải thích và xem lời giải
        xemgiaithich_elements = div_child.find_all(string=lambda text: 'Xem giải thích' in text)
        loigiai_elements = div_child.find_all(string=lambda text: 'Lời giải:' in text)

        for loigiai_element in loigiai_elements:
            loigiai_element.replace_with("")

        for xemgiaithich_element in xemgiaithich_elements:
            xemgiaithich_element.replace_with("Lời giải:")

        # Thay thế câu hỏi
        cauhoi_elements = div_child.find_all(string=lambda text: 'Câu hỏi ' in text)
        for cauhoi_element in cauhoi_elements:
            cauhoi_element.replace_with("Câu ")

        # Thay thế Nhận biết, nâng cao, ...
        trinhdo_elements = div_child.find_all(string=lambda text: 'NHẬN BIẾT' in text)
        for trinhdo_element in trinhdo_elements:
            trinhdo_element.replace_with(": [NB]")

        trinhdo_elements = div_child.find_all(string=lambda text: 'THÔNG HIỂU' in text)
        for trinhdo_element in trinhdo_elements:
            trinhdo_element.replace_with(": [TH]")

        trinhdo_elements = div_child.find_all(string=lambda text: 'VẬN DỤNG CAO' in text)
        for trinhdo_element in trinhdo_elements:
            trinhdo_element.replace_with(": [VDC]")

        trinhdo_elements = div_child.find_all(string=lambda text: 'VẬN DỤNG' in text)
        for trinhdo_element in trinhdo_elements:
            trinhdo_element.replace_with(": [VD]")

        # Xóa "Chọn câu hỏi"
        choncauhoi_elements = div_child.find_all(string=lambda text: 'Chọn câu hỏi' in text)
        for choncauhoi_element in choncauhoi_elements:
            choncauhoi_element.replace_with("")

        

        # Ghi cấu trúc HTML đã thay đổi vào file html.txt
        with open(output_path, "a", encoding="utf-8") as file:
            file.write(div_child.prettify())

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
if not os.path.exists("VioEdu"):
    # Tạo thư mục mới
    os.mkdir("VioEdu")
# else:
#     print("Thư mục đã tồn tại.")

# Kiểm tra xem thư mục đã tồn tại hay chưa
if not os.path.exists("VioEdu" + "/" + tenkhoi):
    # Tạo thư mục mới
    os.mkdir("VioEdu" + "/" + tenkhoi)
# else:
#     print("Thư mục đã tồn tại.")


# Click vào nút đăng nhập
tieptuc_button.click()

# 
# 
# 

time.sleep(2)

if (tenkhoi == "Khối 1"):
    chude_dir = "K1_"
elif (tenkhoi == "Khối 2"):
    chude_dir = "K2_"
elif (tenkhoi == "Khối 3"):
    chude_dir = "K3_"
elif (tenkhoi == "Khối 4"):
    chude_dir = "K4_"
elif (tenkhoi == "Khối 5"):
    chude_dir = "K5_"

if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1"):
        # Tạo thư mục mới
    os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1")
# else:
#     print("Thư mục đã tồn tại.")

########################################################################################################################################################################################################################
########################################################################################################################################################################################################################
########################################################################################################################################################################################################################
# QUAN TRỌNG
# HỌC KÌ 1
# Đóng thẻ tự select ra
dongthe = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[1]")
dongthe.click()

div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
# print("Chủ Đề")                                                      
for div in div_baitap_elements:
    tenchude = div.text
    tenchude = clean_folder_name(tenchude)
    # Kiểm tra xem thư mục đã tồn tại hay chưa
    if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude):
        # Tạo thư mục mới
        os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude)
    # else:
    #     print("Thư mục đã tồn tại.")

# BẮT ĐẦU
div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
tieptuc = 0
for div in div_baitap_elements:
    # break
    tenchude = div.text

    # if tenchude == "HÌNH HỌC PHẲNG" or tieptuc == 1:
    #     tieptuc = 1
    # else:
    #     continue

    tenchude = clean_folder_name(tenchude)

    

    img_element = div.find_element(By.TAG_NAME, "div")
    img_element.click()

    
    div_click_baitap_elements = driver.find_elements(By.CSS_SELECTOR, "div[style='color: rgb(46, 58, 89); font-size: 16px; margin: 6px 5px 6px 15px; display: flex; align-items: center; cursor: pointer;']")

    dem = 1

    # Nhận biết
    # 
    # 
    for div in div_click_baitap_elements:
        # print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        div.click()
        time.sleep(4)

        mucdo = 1
        if mucdo == 1:
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(3)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)

            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)
        


    # Thông hiểu
    # 
    # 
    for div in div_click_baitap_elements:
        print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        if tenchudiem == "Các bài toán cấu tạo số":
            continue

        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        time.sleep(1)
        div.click()
        time.sleep(1)
        div.click()
        time.sleep(4)

        mucdo = 2
        if mucdo == 2:
            to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]")
            driver.execute_script("arguments[0].click();", to_mucdo_element)
            time.sleep(2)
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(2)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)

            # if mucdo == 1:
            #     to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]")
            #     driver.execute_script("arguments[0].click();", to_mucdo_element)
            # elif mucdo == 2:
            #     to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]")
            #     driver.execute_script("arguments[0].click();", to_mucdo_element)
            # elif mucdo == 3:
            #     to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[4]")
            #     driver.execute_script("arguments[0].click();", to_mucdo_element)
            # mucdo += 1   
            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)
        


    # Vận dụng
    # 
    # 
    for div in div_click_baitap_elements:
        print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        time.sleep(1)
        div.click()
        time.sleep(1)
        div.click()
        time.sleep(4)

        mucdo = 3
        if mucdo == 3:
            to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]")
            driver.execute_script("arguments[0].click();", to_mucdo_element)
            time.sleep(2)
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(2)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")                                                          
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)
            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)
        
    # Vận dụng cao
    # 
    # 
    for div in div_click_baitap_elements:
        print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)


        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 1"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        time.sleep(1)
        div.click()
        time.sleep(1)
        div.click()
        time.sleep(4)

        mucdo = 4
        if mucdo == 4:
            to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[4]")
            driver.execute_script("arguments[0].click();", to_mucdo_element)
            time.sleep(2)
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(2)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 1" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)
            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)


    img_element.click()


time.sleep(1)

########################################################################################################################################################################################################################
########################################################################################################################################################################################################################
########################################################################################################################################################################################################################
# QUAN TRỌNG
# HỌC KÌ 2
if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2"):
        # Tạo thư mục mới
    os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2")
# else:
#     print("Thư mục đã tồn tại.")


hki2_click_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div[2]")
hki2_click_element.click()
time.sleep(1)

# Đóng thẻ tự select ra
dongthe = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[1]")
dongthe.click()

div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
print("Chủ Đề")                                                      
for div in div_baitap_elements:
    tenchude = div.text
    tenchude = clean_folder_name(tenchude)
    # Kiểm tra xem thư mục đã tồn tại hay chưa
    if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude):
        # Tạo thư mục mới
        os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude)
    # else:
    #     print("Thư mục đã tồn tại.")

div_baitap_elements = driver.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div[3]/div")
tieptucHK2 = 0
for div in div_baitap_elements:
    tenchude = div.text

    # if tenchude == "ÔN TẬP CHỦ ĐỀ \"HÌNH HỌC, ĐO LƯỜNG\"" or tieptucHK2 == 1:
    #     tieptucHK2 = 1
    # else:
    #     continue

    tenchude = clean_folder_name(tenchude)

    img_element = div.find_element(By.TAG_NAME, "div")
    img_element.click()

    
    div_click_baitap_elements = driver.find_elements(By.CSS_SELECTOR, "div[style='color: rgb(46, 58, 89); font-size: 16px; margin: 6px 5px 6px 15px; display: flex; align-items: center; cursor: pointer;']")

    dem = 1

    # Nhận biết
    # 
    # 
    for div in div_click_baitap_elements:
        print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        div.click()
        time.sleep(4)

        mucdo = 1
        if mucdo == 1:
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(3)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)

            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)
        


    # Thông hiểu
    # 
    # 
    for div in div_click_baitap_elements:
        print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        time.sleep(1)
        div.click()
        time.sleep(1)
        div.click()
        time.sleep(4)

        mucdo = 2
        if mucdo == 2:
            to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]")
            driver.execute_script("arguments[0].click();", to_mucdo_element)
            time.sleep(2)
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(2)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)

            # if mucdo == 1:
            #     to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]")
            #     driver.execute_script("arguments[0].click();", to_mucdo_element)
            # elif mucdo == 2:
            #     to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]")
            #     driver.execute_script("arguments[0].click();", to_mucdo_element)
            # elif mucdo == 3:
            #     to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[4]")
            #     driver.execute_script("arguments[0].click();", to_mucdo_element)
            # mucdo += 1   
            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)
        


    # Vận dụng
    # 
    # 
    for div in div_click_baitap_elements:
        print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        time.sleep(1)
        div.click()
        time.sleep(1)
        div.click()
        time.sleep(4)

        mucdo = 3
        if mucdo == 3:
            to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]")
            driver.execute_script("arguments[0].click();", to_mucdo_element)
            time.sleep(2)
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(2)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)
            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)
        
    # Vận dụng cao
    # 
    # 
    for div in div_click_baitap_elements:
        print("Chủ Điểm")
        # Lấy tên Chủ đề
        tenchudiem = div.text
        tenchudiem = clean_folder_name(tenchudiem)
        if not os.path.exists("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem):
            # Tạo thư mục mới
            os.mkdir("VioEdu" + "/" + tenkhoi + "/" + "Học kì 2"  + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem)
        # else:
        #     print("Thư mục đã tồn tại.")

        time.sleep(1)
        div.click()
        time.sleep(1)
        div.click()
        time.sleep(4)

        mucdo = 4
        if mucdo == 4:
            to_mucdo_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div[4]")
            driver.execute_script("arguments[0].click();", to_mucdo_element)
            time.sleep(2)
            # Nhấn button select ra Lời giải
            div_button_elements = div.find_elements(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]/div")
            # print(len(div_button_elements))               
            for div_btn in div_button_elements:
                if div_btn.find_element(By.TAG_NAME, "div"):
                    button_elements = div_btn.find_element(By.TAG_NAME, "button")
                    driver.execute_script("arguments[0].click();", button_elements)
                
            time.sleep(2)

            # Lấy thẻ div lớn lấy nội dung cần copy
            copy_all_element = div.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div[2]")
            script = "return arguments[0].innerHTML;"
            content = driver.execute_script(script, copy_all_element)

            if mucdo == 1:
                dienmucdo = "_NB"
            elif mucdo == 2:
                dienmucdo = "_TH"
            elif mucdo == 3:
                dienmucdo = "_VD"
            elif mucdo == 4:
                dienmucdo = "_VDC"
            
            output_path = "VioEdu" + "/" + tenkhoi + "/" + "Học kì 2" + "/" + chude_dir + tenchude + "/" + chude_dir + tenchudiem + "/" + chude_dir + clean_file_name(tenchudiem) + dienmucdo + ".html"
            
            # Tạo file HTML
            html_to_docx(content, output_path)
            time.sleep(2)                                         

        close_element = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div[3]/div[3]/div/div[3]/div/div[3]/div[3]/div[2]/div[1]/span/i")
        driver.execute_script("arguments[0].click();", close_element)
        time.sleep(2)


    img_element.click()


time.sleep(1)

print("XONG")
# Tắt trình duyệt
driver.quit()
