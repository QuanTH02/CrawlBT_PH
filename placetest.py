from bs4 import BeautifulSoup
import os

# Giả sử `html_content` là chuỗi HTML bạn muốn xử lý
html_content = """
<div>Khối 1</div>
"""

# Tạo đối tượng BeautifulSoup từ chuỗi HTML
soup = BeautifulSoup(html_content, 'html.parser')
khoi = soup.find('div')

tenkhoi = khoi.text

directory = tenkhoi

# Kiểm tra xem thư mục đã tồn tại hay chưa
if not os.path.exists(directory):
    # Tạo thư mục mới
    os.mkdir(directory)
else:
    print("Thư mục đã tồn tại.")

# Kiểm tra xem thư mục đã tồn tại hay chưa
if not os.path.exists(tenkhoi + '/' + "hehe"):
    # Tạo thư mục mới
    os.mkdir(tenkhoi + '/' + "hehe")
else:
    print("Thư mục đã tồn tại.")

