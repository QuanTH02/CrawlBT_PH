from bs4 import BeautifulSoup

html_content = """
<div style="margin-top: 20px; overflow: auto; height: 500px;" class="default_cursor_cs"><div><div class="panel panel-preview-primary panel-preview-question default_cursor_cs"><div class="panel-heading default_cursor_cs">Câu hỏi <strong>1</strong> - VẬN DỤNG</div><div class="panel-body default_cursor_cs"><div><p class="default_cursor_cs">Sắp xếp các số sau theo thứ tự từ bé đến lớn.</p>
</div><div><div style="display: flex;" class="default_cursor_cs"><div><p>1</p>
</div></div><div style="display: flex;" class="default_cursor_cs"><div><p>6</p>
</div></div><div style="display: flex;" class="default_cursor_cs"><div><p>8</p>
</div></div><div style="display: flex;" class="default_cursor_cs"><div><p>10</p>
</div></div><div class="default_cursor_cs"><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Ta có:&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1<6<8<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/737.PNG1565318346463"><br>
Thứ tự đúng là: 1 ;&nbsp;6 ;&nbsp;8 ;&nbsp;10.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div></div><div><div class="panel panel-preview-primary panel-preview-question default_cursor_cs"><div class="panel-heading default_cursor_cs">Câu hỏi <strong>2</strong> -  VẬN DỤNG</div><div class="panel-body default_cursor_cs"><div><p class="default_cursor_cs">Bạn hãy chọn đáp án đúng.<br>
Số nào lớn nhất trong các số <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10,2,5,4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.144em; padding-bottom: 0.519em;">,</span></span><span class="mjx-mn MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.144em; padding-bottom: 0.519em;">,</span></span><span class="mjx-mn MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.144em; padding-bottom: 0.519em;">,</span></span><span class="mjx-mn MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>?<br>
<img class="img-responsive default_cursor_cs" src="https://s3.vio.edu.vn/images/question/749.PNG1565321153699"></p>
</div><li class="answerChoice correctAnswer default_cursor_cs" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false default_cursor_cs" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false default_cursor_cs" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Ta có phép so sánh:&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10>5>4>2 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>.<br>
Số lớn nhất trong các&nbsp;số là số <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/750.PNG1565321315261"><br>
Đáp án: <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>3</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền đáp án đúng vào ô trống.<br>
Có {} hình có ít hơn <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con bò.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/764.PNG1565323749658"></p>
</div><div>ĐÁP ÁN ĐÚNG: 3
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Hình 1 có 7 con bò.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Hình 2 có 9 con bò.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Hình 3 có 5 con bò.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Hình 4 có 10 con bò.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10=10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.077em; padding-bottom: 0.298em;">=</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/802.PNG1565599985373"><br>
Cả 3 hình có ít hơn <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con bò.<br>
Đáp án: <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>4</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ trống.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image.png1565333915318"><br>
Nhà An nuôi <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con thỏ. Hôm nay, An đã cho mỗi con thỏ ăn <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span> củ cà rốt. Số củ cà rốt An đã cho <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con thỏ ăn trong hôm nay là {}.</p>
</div><div>ĐÁP ÁN ĐÚNG: 10
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lời giải: </b><br>
Nhà An nuôi <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con thỏ.<br>
Mỗi con thỏ ăn <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span> củ cà rốt nên số củ cà rốt bằng số con thỏ.<br>
<img src="https://s3.vio.edu.vn/image.png1565334069448"><br>
Vậy số củ cà rốt An đã cho <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con thỏ ăn trong hôm nay là <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>5</strong> -VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng để điền vào ô trống.<br>
Hình vẽ thể hiện: {}<span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label=">3>"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span></span></span></span></span></span>{}.<br>
<img src="https://s3.vio.edu.vn/images/question/748.PNG1565320862682"></p>
</div><div>ĐÁP ÁN ĐÚNG: <span>10, 0</span></div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lí thuyết: </b> Dấu "&gt;" là lớn hơn hay nhiều hơn.<br>
<b>Lời giải: </b><br>
Đếm số dê trong hình ta thấy, hình 1 có 10 con dê. Hình 2 có 3 con dê. Hình thứ 3 không có con dê nào. Ta có phép so sánh:<br>
<span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10>3>0"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">0</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/747.PNG1565320882458"><br>
<strong>Vậy số cần điền là: 10 và 0.</strong><p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>6</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10>2>1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span>.<br>
Câu trên đúng hay sai?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/808.PNG1565662025255"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Đúng.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Sai.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Không xác định.</p>
</div></li><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lí thuyết: </b> Dấu "&gt;" là lớn hơn hay nhiều hơn.<br>
<b>Lời giải: </b><br>
<span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10>2>1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span> là đúng.<br>
<img src="https://s3.vio.edu.vn/image.png1565662093411"><br>
Đáp án: Đúng.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>7</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp&nbsp;vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db3@mtd2@dk1@dpt0@00024_1560398433.png"><br>
Trong các số trên, số lớn nhất là {}.</p>
</div><div>ĐÁP ÁN ĐÚNG: 10
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lời giải: </b><br>
Trong hình trên có tất cả <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span> số là <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>; <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>; <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>; <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>.<br>
Vì <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 > 2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>;&nbsp;<br>
<img src="https://s3.vio.edu.vn/image.png1565334183669"><br>
<span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 > 5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>;<br>
<img src="https://s3.vio.edu.vn/image.png1565334193574"><br>
<span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 > 8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/image.png1565334202256"><br>
Nên&nbsp;số <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> là số lớn nhất trong các số cho trên hình.<br>
<strong>Vậy số cần điền là:&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span></strong><p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>8</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền đáp án đúng vào ô trống.<br>
Hình vẽ thể hiện: <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6<"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span></span></span></span></span></span>{}.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/774.PNG1565333480198"></p>
</div><div>ĐÁP ÁN ĐÚNG: 10
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lí thuyết: </b> Dấu "&lt;" là nhỏ hơn hay bé hơn.<br>
<b>Lời giải: </b><br>
Hình vẽ thể hiện: <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6<10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/image.png1565333553722"><br>
Đáp án: <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>9</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền đáp án đúng vào ô trống.<br>
Hình vẽ thể hiện: <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4<"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span></span></span></span></span></span>{}<span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="=10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.077em; padding-bottom: 0.298em;">=</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span><br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/759.PNG1565322623646"></p>
</div><div>ĐÁP ÁN ĐÚNG: 10
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lí thuyết: </b><br>
Dấu "&lt;" là nhỏ hơn hay bé hơn.<br>
Dấu "=" là bằng nhau.<br>
<b>Lời giải: </b><br>
Hình vẽ thể hiện: <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4<10=10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.077em; padding-bottom: 0.298em;">=</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/760.PNG1565322632958"><br>
Đáp án: <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>10</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền đáp án đúng vào ô trống.<br>
Số bé nhất trong các số: <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4,6,8,10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.144em; padding-bottom: 0.519em;">,</span></span><span class="mjx-mn MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.144em; padding-bottom: 0.519em;">,</span></span><span class="mjx-mn MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="margin-top: -0.144em; padding-bottom: 0.519em;">,</span></span><span class="mjx-mn MJXc-space1"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> là số {}.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/761.PNG1565322791388"></p>
</div><div>ĐÁP ÁN ĐÚNG: 4
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Ta có phép so sánh:&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4<6<8<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Số bé nhất là số <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/762.PNG1565322916751"><br>
Đáp án: <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>11</strong> -VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án thích hợp để điền vào ô trống:<br>
Có <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> chùm nho và <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> chiếc bút chì.<br>
<img alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db7@mtd1@dk1@dpt0@00042_1560398433.png"><br>
Số chùm nho {} số chiếc bút chì.</p>
</div><div>ĐÁP ÁN ĐÚNG: <span>bé hơn</span></div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lời giải: </b><br>
Có <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> chùm nho và <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> chiếc bút chì.<br>
<img src="https://s3.vio.edu.vn/images/question/801.PNG1565599909611"><br>
Vì <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7 < 10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> nên số chùm nho bé hơn số chiếc bút chì.<br>
<img src="https://s3.vio.edu.vn/images/question/752.PNG1565321753284"><br>
Đáp án: bé hơn.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>12</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1=10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.077em; padding-bottom: 0.298em;">=</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Câu trên đúng hay sai?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Đúng</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Sai</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lí thuyết: </b><br>
Dấu "=" là bằng nhau.<br>
Dấu "&lt;" là bé hơn hay nhiều hơn.<br>
<b>Lời giải: </b><br>
Vì <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1<10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> nên <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1=10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.077em; padding-bottom: 0.298em;">=</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> là sai.<br>
<img src="https://s3.vio.edu.vn/image.png1588821489513"><br>
<strong>Đáp án: </strong>Sai.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>13</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db1@mtd2@dk1@dpt0@00004_1560398433.png"><br>
Số nào dưới đây lớn hơn <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span> số đã cho trên hình?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lời giải: </b><br>
Vì:<br>
<span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 > 1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/image.png1565662932730"><br>
<span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 > 4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/image.png1565339950990"><br>
<span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 > 7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/image.png1565339960662"><br>
<span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 > 9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/image.png1565339976456"><br>
Vậy số lớn hơn cả <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span> số đã cho trên hình là <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Đáp án: <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span><p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>14</strong> - VẬN DỤNG</div><div class="panel-body"><div><p>Sắp xếp các số sau theo thứ tự từ lớn đến bé.</p>
</div><div><div style="display: flex;"><div><p>10</p>
</div></div><div style="display: flex;"><div><p>7</p>
</div></div><div style="display: flex;"><div><p>4</p>
</div></div><div style="display: flex;"><div><p>2</p>
</div></div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Ta có:&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10>7>4>2 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&gt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/736.PNG1565317472512"><br>
Thứ tự đúng là: 10 ;&nbsp;7 ;&nbsp;4 ;&nbsp;2.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>15</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.&nbsp;<br>
Có bao nhiêu hình có ít hơn <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> cây nến?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/738.PNG1565319090401"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Hình thứ nhất có 2 cây nến.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Hình thứ 2 có 4 cây nến.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Hình thứ 3 có 7 cây nến.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
Hình thứ tư có 10 cây nến.&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10=10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.077em; padding-bottom: 0.298em;">=</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<br>
<img src="https://s3.vio.edu.vn/images/question/739.PNG1565319099119"><br>
Có <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span> hình có ít hơn <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> cây nến.<br>
<img src="https://s3.vio.edu.vn/images/question/740.PNG1565319246807"><br>
Đáp án: <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>16</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Có bao nhiêu&nbsp;hình có ít hơn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> quả bóng rổ?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db3@mtd2@dk1@dpt0@00112_1569808692.png"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span>&nbsp;hình</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>&nbsp;hình</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>&nbsp;hình</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span>&nbsp;có&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;quả bóng rổ.<br>
Hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>&nbsp;có&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;quả bóng rổ.<br>
Hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>&nbsp;có&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>&nbsp;quả bóng rổ.<br>
Do đó cả&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span> hình đều có ít hơn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> quả bóng rổ.<br>
<strong>Đáp án:</strong> <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>&nbsp;hình.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>17</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db3@mtd2@dk1@dpt0@00102_1_1569808692.png"><br>
Nhà Bình nuôi <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con gà. Mỗi con gà đẻ ra <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span> quả trứng. Số trứng <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con gà đẻ ra là {} quả.</p>
</div><div>ĐÁP ÁN ĐÚNG: 10
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lời giải: </b><br>
Nhà Bình nuôi <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con gà.<br>
Mỗi con gà đẻ ra <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span> quả trứng nên số trứng bằng số con gà.<br>
<img alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db3@mtd2@dk1@dpt0@00102_2_1569808692.png"><br>
Do đó&nbsp;số trứng <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con gà đẻ ra là <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>&nbsp;quả.<br>
<strong>Vậy số thích hợp cần điền là:</strong>&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>18</strong> -  VẬN DỤNG</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db3@mtd2@dk1@dpt0@00101_1_1569808692.png"><br>
Nhà An nuôi <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con khỉ. Hôm nay, An đã cho mỗi con khỉ ăn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span> quả chuối. Số chuối An đã cho <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con khỉ ăn trong hôm nay là {} quả.</p>
</div><div>ĐÁP ÁN ĐÚNG: 10
</div><div><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p><b>Lời giải: </b><br>
Nhà An nuôi <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con khỉ.<br>
Mỗi con khỉ ăn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span> quả chuối nên số quả chuối bằng số con khỉ.<br>
<img alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db3@mtd2@dk1@dpt0@00101_2_1569808692.png"><br>
Do đó&nbsp;số quả chuối An đã cho <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> con khỉ ăn trong hôm nay là <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>&nbsp;quả.<br>
<strong>Vậy số thích hợp cần điền là:</strong>&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>19</strong> -  VẬN DỤNG</div><div class="panel-body default_cursor_cs"><div><p class="default_cursor_cs">Bạn hãy chọn đáp án đúng.<br>
Có bao nhiêu&nbsp;hình có ít hơn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> hình tam giác?<br>
<img class="img-responsive default_cursor_cs" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@21@03@04@db3@mtd2@dk1@dpt0@00111_1569808692.png"></p>
</div><li class="answerChoice false default_cursor_cs" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span>&nbsp;hình</p>
</div></li><li class="answerChoice correctAnswer default_cursor_cs" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>&nbsp;hình</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false default_cursor_cs" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>&nbsp;hình</p>
</div></li><div class="default_cursor_cs"><button class="btn btn-default default_pointer_cs">Xem giải thích</button><div><div><strong>Bước 1:</strong>&nbsp;&nbsp;&nbsp;<span><p></p>Hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span>&nbsp;có&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;hình tam giác. Vì&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>&nbsp;nên hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span>&nbsp;có ít hơn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> hình tam giác.<br>
Hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>&nbsp;có&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>&nbsp;hình tam giác.<br>
Hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>&nbsp;có&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;hình tam giác. Vì&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7<10 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span>&nbsp;nên hình&nbsp;<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>&nbsp;có ít hơn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> hình tam giác.<br>
Do đó có <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span> hình có ít hơn <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="10"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">10</span></span></span></span></span></span></span> hình tam giác.<br>
<strong>Đáp án:</strong> <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span>&nbsp;hình.<p></p>
</span></div></div></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div></div>
"""

# soup = BeautifulSoup(html_content, 'html.parser')

# CHƯA THAY ĐỔI

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

    for div_child in div_childs:
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


html_to_docx(html_content, "html1.html")
