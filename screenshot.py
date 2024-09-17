import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()
page_main_url = "https://vi.wikipedia.org/wiki/L%E1%BB%8Bch_s%E1%BB%AD_Vi%E1%BB%87t_Nam"
driver.get(page_main_url)

time.sleep(3)
# Tìm phần tử div bạn muốn trích xuất
div_element = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[5]")
print(div_element.text)

# Cuộn đến phần tử để đảm bảo nó hiển thị trên màn hình
driver.execute_script("arguments[0].scrollIntoView();", div_element)
time.sleep(3)
# Lấy tọa độ của phần tử div trên màn hình
location = div_element.location_once_scrolled_into_view

# Kích thước của phần tử div
size = div_element.size

# Lấy ảnh màn hình và chọn phần tử div
screenshot = pyautogui.screenshot(region=(location['x'] + 65, location['y'] + 165, size['width'], size['height'] + 35))

# Lưu ảnh vào bộ nhớ máy tính
screenshot.save("div_content1.png")

# Đóng trình duyệt
driver.quit()
