from bs4 import BeautifulSoup

html_content = """
<div style="margin-top: 20px; overflow: auto; height: 500px;" class="default_cursor_cs"><div><div class="panel panel-preview-primary panel-preview-question default_cursor_cs"><div class="panel-heading default_cursor_cs">Câu hỏi <strong>1</strong> -  NHẬN BIẾT</div><div class="panel-body default_cursor_cs"><div><p class="default_cursor_cs">Điền số thích hợp vào ô trống&nbsp;để được dãy số tăng dần.<br>
<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="218"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">218</span></span></span></span></span></span></span>; <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="219"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">219</span></span></span></span></span></span></span>; <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="220"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">220</span></span></span></span></span></span></span>; {}; <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="222"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">222</span></span></span></span></span></span></span>; <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="223"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">223</span></span></span></span></span></span></span>; <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="224"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">224</span></span></span></span></span></span></span>.</p>
</div><div class="default_cursor_cs">ĐÁP ÁN ĐÚNG: 221
</div><div class="default_cursor_cs"><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right default_pointer_cs">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading default_cursor_cs">Câu hỏi <strong>2</strong> -NHẬN BIẾT</div><div class="panel-body default_cursor_cs"><div><p class="default_cursor_cs">Hãy chọn đáp án đúng để điền vào ô trống.<br>
Muốn so sánh các số có <span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span> chữ số, ta so sánh các chữ số hàng {}, nếu bằng nhau thì so sánh chữ số hàng chục, nếu các chữ số đó đều bằng nhau thì so sánh chữ số hàng {} (số nào có chữ số ở hàng tương ứng lớn hơn thì số đó lớn hơn).</p>
</div><div class="default_cursor_cs">ĐÁP ÁN ĐÚNG: <span><p>trăm</p>
, <p>đơn vị</p>
</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>3</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>&nbsp;Chọn đáp án đúng điền vào ô trống:<br>
Trong các số sau, số nào là số lớn nhất?<br>
<img alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@050795@03@6@01@07@01@01@db3@mtd1@dk1@dpt0@1_1_1561628115.png"><br>
Số lớn nhất là {}</p>
</div><div>ĐÁP ÁN ĐÚNG: <span>495</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>4</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền&nbsp;số tròn trăm thích hợp vào chỗ trống để được phép so sánh đúng.<br>
{}&nbsp;<span class="math-tex"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="+80<250"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mo"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">80</span></span><span class="mjx-mo MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.225em; padding-bottom: 0.372em;">&lt;</span></span><span class="mjx-mn MJXc-space3"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">250</span></span></span></span></span></span></span></p>
</div><div>ĐÁP ÁN ĐÚNG: 100
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>5</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Số liền trước của số <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="320"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">320</span></span></span></span></span></span></span> là:</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="321"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">321</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="322"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">322</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="325"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">325</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="319"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">319</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>6</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong các số sau, số nào là số nhỏ nhất?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@250495@03@6@01@07@01@01@db1@mtd1@dk1@dpt0@0058_1574329046.png"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="567"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">567</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="454"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">454</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="545"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">545</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>7</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng để điền vào ô trống.<br>
<span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="788"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">788</span></span></span></span></span></span></span> {} <span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="781"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">781</span></span></span></span></span></span></span></p>
</div><div>ĐÁP ÁN ĐÚNG: <span><p>&gt;</p>
</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>8</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Số <span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="784"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">784</span></span></span></span></span></span></span> có chữ số {} là chữ số hàng chục.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>9</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>Số <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="245"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">245</span></span></span></span></span></span></span> có chữ số hàng trăm và chữ số hàng chục lần lượt là:<br></p></div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span> và <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span></p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span> và <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span></p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span> và <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span></p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>10</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>Số liền sau của số <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="238"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">238</span></span></span></span></span></span></span> là {}.<br></p></div><div>ĐÁP ÁN ĐÚNG: 239</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>11</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/.iii.v.1.1.03_1_1700671033.png" alt="img_question"><br>Số thích hợp điền vào dấu hỏi chấm trong hình trên để được ba số liên tiếp là {}.<br></p></div><div>ĐÁP ÁN ĐÚNG: 152</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>12</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>Viết số <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="378"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">378</span></span></span></span></span></span></span> thành tổng các trăm, chục và đơn vị được kết quả là:<br></p></div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="300 + 70 + 8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">300</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">70</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="200 + 70 + 8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">200</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">70</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="300 + 80 + 8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">300</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">80</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>	</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="300 + 70 + 9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">300</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">70</span></span><span class="mjx-mo MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.298em; padding-bottom: 0.446em;">+</span></span><span class="mjx-mn MJXc-space2"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>13</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>Số “Một trăm hai mươi ba” được viết là {}.<br></p></div><div>ĐÁP ÁN ĐÚNG: 123</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>14</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>Chữ số hàng trăm của số <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="382"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">382</span></span></span></span></span></span></span> là chữ số nào?<br>Trả lời: Chữ số {}.<br></p></div><div>ĐÁP ÁN ĐÚNG: 3</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>15</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>Số <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="804"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">804</span></span></span></span></span></span></span> được đọc là:<br></p></div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Tám trăm linh bốn</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Tám không bốn</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Tám trăm bốn đơn vị</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div></div>
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

    if len(div_all) == 0:
        return
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

            flex_divs = panel_body_div_sx.find_all("div", style="display: flex;")

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
                new_values = []
                for value in results[index:index+tag.count("{}")]:
                    if value == "ít hơn":
                        new_values.append("[[" + value + "||" + "<" + "||" + "nhỏ hơn" + "||" + "bé hơn" + "]]")
                    elif value == "bé hơn":
                        new_values.append("[[" + value + "||" + "ít hơn" + "||" + "nhỏ hơn" + "||" + "<" + "]]")
                    elif value == "nhỏ hơn":
                        new_values.append("[[" + value + "||" + "ít hơn" + "||" + "<" + "||" + "bé hơn" + "]]")
                    elif value == "<":
                        new_values.append("[[" + value + "||" + "ít hơn" + "||" + "nhỏ hơn" + "||" + "bé hơn" + "]]")

                    elif value == "nhiều hơn":
                        new_values.append("[[" + value + "||" + ">" + "||" + "lớn hơn" + "||" + "to hơn" + "]]")
                    elif value == "lớn hơn":
                        new_values.append("[[" + value + "||" + ">" + "||" + "nhiều hơn" + "||" + "to hơn" + "]]")
                    elif value == "to hơn":
                        new_values.append("[[" + value + "||" + ">" + "||" + "lớn hơn" + "||" + "nhiều hơn" + "]]")
                    elif value == ">":
                        new_values.append("[[" + value + "||" + "nhiều hơn" + "||" + "lớn hơn" + "||" + "to hơn" + "]]")

                    elif value == "bằng nhau":
                        new_values.append("[[" + value + "||" + "=" + "||" + "bằng" + "]]")
                    elif value == "bằng":
                        new_values.append("[[" + value + "||" + "=" + "||" + "bằng nhau" + "]]")
                    elif value == "=":
                        new_values.append("[[" + value + "||" + "bằng" + "||" + "bằng nhau" + "]]")

                    elif value == "Đúng":
                        new_values.append("[[" + value + "||" + "Chính xác" + "||" + "True" + "]]")
                    elif value == "Chính xác":
                        new_values.append("[[" + value + "||" + "Đúng" + "||" + "True" + "]]")
                    elif value == "True":
                        new_values.append("[[" + value + "||" + "Chính xác" + "||" + "Đúng" + "]]")

                    elif value == "Sai":
                        new_values.append("[[" + value + "||" + "Không chính xác" + "||" + "False" + "||" + "Chưa chính xác" + "]]")
                    elif value == "Không chính xác":
                        new_values.append("[[" + value + "||" + "Sai" + "||" + "False" + "||" + "Chưa chính xác" + "]]")
                    elif value == "False":
                        new_values.append("[[" + value + "||" + "Sai" + "||" + "Không chính xác" + "||" + "Chưa chính xác" + "]]")

                    elif value == "Phải":
                        new_values.append("[[" + value + "||" + "Bên phải" + "||" + "Phía bên phải" + "]]")
                    elif value == "Bên phải":
                        new_values.append("[[" + value + "||" + "Phải" + "||" + "Phía bên phải" + "]]")
                    elif value == "Phía bên phải":
                        new_values.append("[[" + value + "||" + "Phải" + "||" + "Bên phải" + "]]")

                    elif value == "Trái":
                        new_values.append("[[" + value + "||" + "Bên trái" + "||" + "Phía bên trái" + "]]")
                    elif value == "Bên trái":
                        new_values.append("[[" + value + "||" + "Trái" + "||" + "Phía bên trái" + "]]")
                    elif value == "Phía bên trái":
                        new_values.append("[[" + value + "||" + "Trái" + "||" + "Bên trái" + "]]")
                    
                    elif value == "Trên":
                        new_values.append("[[" + value + "||" + "Phía trên" + "||" + "Bên trên" + "]]")
                    elif value == "Phía trên":
                        new_values.append("[[" + value + "||" + "Trên" + "||" + "Bên trên" + "]]")
                    elif value == "Bên trên":
                        new_values.append("[[" + value + "||" + "Trên" + "||" + "Phía trên" + "]]")
                    
                    elif value == "Dưới":
                        new_values.append("[[" + value + "||" + "Phía dưới" + "||" + "Bên dưới" + "]]")
                    elif value == "Phía dưới":
                        new_values.append("[[" + value + "||" + "Dưới" + "||" + "Bên dưới" + "]]")
                    elif value == "Bên dưới":
                        new_values.append("[[" + value + "||" + "Dưới" + "||" + "Phía dưới" + "]]")
                    
                    elif value == "Trước":
                        new_values.append("[[" + value + "||" + "Phía trước" + "||" + "Đằng trước" + "]]")
                    elif value == "Phía trước":
                        new_values.append("[[" + value + "||" + "Trước" + "||" + "Đằng trước" + "]]")
                    elif value == "Đằng trước":
                        new_values.append("[[" + value + "||" + "Trước" + "||" + "Phía trước" + "]]")
                    
                    elif value == "Sau":
                        new_values.append("[[" + value + "||" + "Phía sau" + "||" + "Đằng sau" + "]]")
                    elif value == "Phía sau":
                        new_values.append("[[" + value + "||" + "Sau" + "||" + "Đằng sau" + "]]")
                    elif value == "Đằng sau":
                        new_values.append("[[" + value + "||" + "Sau" + "||" + "Phía sau" + "]]")

                    else:
                        new_values.append("[[" + value + "]]")
                new_string = tag.format(*new_values)

                tag.replace_with(new_string)
                index += tag.count("{}")
            else:
                # Thay thế nội dung của tag trực tiếp
                if results[index]:
                    if results[index] == "ít hơn":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "<" + "||" + "nhỏ hơn" + "||" + "bé hơn" + "]]")
                    elif results[index] == "bé hơn":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "ít hơn" + "||" + "nhỏ hơn" + "||" + "<" + "]]")
                    elif results[index] == "nhỏ hơn":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "ít hơn" + "||" + "<" + "||" + "bé hơn" + "]]")
                    elif results[index] == "<":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "ít hơn" + "||" + "nhỏ hơn" + "||" + "bé hơn" + "]]")
                    
                    elif results[index] == "nhiều hơn":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + ">" + "||" + "lớn hơn" + "||" + "to hơn" + "]]")
                    elif results[index] == "lớn hơn":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + ">" + "||" + "nhiều hơn" + "||" + "to hơn" + "]]")
                    elif results[index] == "to hơn":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + ">" + "||" + "lớn hơn" + "||" + "nhiều hơn" + "]]")
                    elif results[index] == ">":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "nhiều hơn" + "||" + "lớn hơn" + "||" + "to hơn" + "]]")
                    
                    elif results[index] == "bằng nhau":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "=" + "||" + "bằng" + "]]")
                    elif results[index] == "bằng":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "=" + "||" + "bằng nhau" + "]]")
                    elif results[index] == "=":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "bằng" + "||" + "bằng nhau" + "]]")
                    
                    elif results[index] == "Đúng":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Chính xác" + "||" + "True" + "]]")
                    elif results[index] == "Chính xác":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Đúng" + "||" + "True" + "]]")
                    elif results[index] == "True":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Chính xác" + "||" + "Đúng" + "]]")
                    
                    elif results[index] == "Sai":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Không chính xác" + "||" + "False" + "||" + "Chưa chính xác" + "]]")
                    elif results[index] == "Không chính xác":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Sai" + "||" + "False" + "||" + "Chưa chính xác" + "]]")
                    elif results[index] == "False":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Sai" + "||" + "Không chính xác" + "||" + "Chưa chính xác" + "]]")
                    
                    elif results[index] == "Phải":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Bên phải" + "||" + "Phía bên phải" + "]]")
                    elif results[index] == "Bên phải":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Phải" + "||" + "Phía bên phải" + "]]")
                    elif results[index] == "Phía bên phải":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Phải" + "||" + "Bên phải" + "]]")
                    
                    elif results[index] == "Trái":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Bên trái" + "||" + "Phía bên trái" + "]]")
                    elif results[index] == "Bên trái":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Trái" + "||" + "Phía bên trái" + "]]")
                    elif results[index] == "Phía bên trái":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Trái" + "||" + "Bên trái" + "]]")
                    
                    elif results[index] == "Trên":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Phía trên" + "||" + "Bên trên" + "]]")
                    elif results[index] == "Phía trên":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Trên" + "||" + "Bên trên" + "]]")
                    elif results[index] == "Bên trên":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Trên" + "||" + "Phía trên" + "]]")
                    
                    elif results[index] == "Dưới":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Phía dưới" + "||" + "Bên dưới" + "]]")
                    elif results[index] == "Phía dưới":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Dưới" + "||" + "Bên dưới" + "]]")
                    elif results[index] == "Bên dưới":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Dưới" + "||" + "Phía dưới" + "]]")
                    
                    elif results[index] == "Trước":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Phía trước" + "||" + "Đằng trước" + "]]")
                    elif results[index] == "Phía trước":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Trước" + "||" + "Đằng trước" + "]]")
                    elif results[index] == "Đằng trước":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Trước" + "||" + "Phía trước" + "]]")
                    
                    elif results[index] == "Sau":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Phía sau" + "||" + "Đằng sau" + "]]")
                    elif results[index] == "Phía sau":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Sau" + "||" + "Đằng sau" + "]]")
                    elif results[index] == "Đằng sau":
                        new_string = tag.replace("{}", "[[" + results[index] + "||" + "Sau" + "||" + "Phía sau" + "]]")
                    
                    else:
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


html_to_docx(html_content, "html.html")
