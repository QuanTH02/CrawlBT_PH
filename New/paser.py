from bs4 import BeautifulSoup

html_content = """

<div style="margin-top: 20px; overflow: auto; height: 500px;" class="default_cursor_cs"><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading default_cursor_cs">Câu hỏi <strong>1</strong> -  NHẬN BIẾT</div><div class="panel-body default_cursor_cs"><div><p class="default_cursor_cs">Bạn hãy điền đáp án đúng vào ô trống.<br>
Trong hình có {} con bướm.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/582.PNG1565162491473"></p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>2</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền đáp án đúng vào ô trống.<br>
Trong hình có {} quả táo.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/580.PNG1565162428661"></p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>3</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình dưới đây có bao nhiêu cây xương rồng ?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/526.PNG1564979400193"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>7</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>6</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>5</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>4</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu chiếc bánh?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/619.PNG1565169051064"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>5</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình có {} chiếc ô tô.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@00031_1560398433.png"></p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>6</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/592.PNG1565164529892"><br>
Hình trên có {} quả xoài.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>7</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có {} quả bóng bay.<br>
<img src="https://s3.vio.edu.vn/images/question/422.PNG1564712631304"></p>
</div><div>ĐÁP ÁN ĐÚNG: <span>7</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>8</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu bông hoa?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/609.PNG1565167254501"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>9</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn cách viết của số “chín”.</p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>10</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án thích hợp để điền vào ô trống:<br>
<img src="https://s3.vio.edu.vn/images/question/440.PNG1564715481849"><br>
Trong hình có {} quả dâu.</p>
</div><div>ĐÁP ÁN ĐÚNG: <span>7</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>11</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Số trong hình sau là số nào?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00010_1560398433.png"><br>
&nbsp;</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Bảy</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Tám</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Chín</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>12</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/626.PNG1565231606369"><br>
Hình trên có bao nhiêu quả dứa?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>13</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn câu trả lời đúng.<br>
Có bao nhiêu bông hoa hướng dương trong hình sau?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@20@03@02@db1@mtd2@dk1@dpt0@00008_1560398433.png"><br>
&nbsp;</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>14</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Số trong hình sau là số nào?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/502.PNG1564733204918"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Sáu</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Bảy</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Bốn</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>15</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền đáp án đúng.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@00022_1560398433.png"><br>
Trong hình có {} cái kem.</p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>16</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình dưới đây có tất cả {} chiếc bút chì.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/538.PNG1565161176566"></p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>17</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@181096@01@13@01@20@03@02@db7@mtd1@dk1@dpt0@00048_1560398433.png"><br>
<br>
Hình trên có bao nhiêu&nbsp;con chim ?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>7</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>8</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>9</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>18</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn cách viết của số “tám”.</p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>19</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu con ong?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/images/question/607.PNG1565167111124"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>20</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image.png1617592441471"><br>
Hình trên có bao nhiêu con cừu?<br>
Trả lời: {} con cừu.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>21</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ trống.<br>
<img src="https://s3.vio.edu.vn/images/question/555.PNG1565151153464"><br>
Trong hình có {} quả bóng.</p>
</div><div>ĐÁP ÁN ĐÚNG: <span>8</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>22</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu bông hoa?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db1@mtd1@dk1@dpt0@00063_1569724125.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;bông hoa.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;bông hoa.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;bông hoa.</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>23</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image.png1587200888826"><br>
Trong hình có bao nhiêu cậu bé?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;cậu bé.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;cậu bé.</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;cậu bé.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>24</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db1@mtd1@dk1@dpt0@00095_1569724125.png"><br>
Trong hình có bao nhiêu cái đồng hồ?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>&nbsp;cái đồng hồ</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;cái đồng hồ</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;cái đồng hồ</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>25</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image.png1587201950638"><br>
Số trong hình được đọc là:</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Sáu</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Bảy</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Năm</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>26</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ&nbsp;trống.<br>
Trong đĩa có {} con tôm.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@00086_1569724125.png"></p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>27</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình dưới đây có bao nhiêu chậu hoa?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db1@mtd1@dk1@dpt0@000105_1569724125.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;chậu hoa.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;chậu hoa.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;chậu&nbsp;hoa.</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>28</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu cây nến?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db1@mtd1@dk1@dpt0@000103_1569724125.png"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;cây nến.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;cây nến.</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;cây nến.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>29</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@000114_1569724125.png"><br>
Hình trên có {}&nbsp;cái phong bì.</p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>30</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Số bảy được viết là</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>31</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image.png1587174946132"><br>
Trong hình trên có bao nhiêu con gấu?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="3"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">3</span></span></span></span></span></span></span>&nbsp;con gấu.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>&nbsp;&nbsp;con gấu.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;con gấu.</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;con gấu.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>32</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@000122_1569724125.png"><br>
Hình trên có {}&nbsp;cái ô tô.</p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>33</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@00078_1569724125.png"><br>
Trong hình có {} con gà trống.</p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>34</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu quả cà chua?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db1@mtd1@dk1@dpt0@00072_1569724125.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;quả cà chua.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;quả cà chua.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;quả cà chua.</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>&nbsp;quả cà chua.</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>35</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ&nbsp;trống.<br>
Trong hình có {} miếng dưa hấu.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@00088_1569724125.png"></p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>36</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp&nbsp;vào chỗ&nbsp;trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@00085_2_1569724125.png"><br>
Trong hình&nbsp;có bao nhiêu&nbsp;cây kem?<br>
Trả lời: {} cây kem.</p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>37</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db1@mtd1@dk1@dpt0@000118_1569724125.png"><br>
Trong hình có bao nhiêu con cá?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;con cá</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;con cá</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;con cá</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>38</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào chỗ&nbsp;trống.<br>
Trong hình có {} chiếc ô.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@00087_1569724125.png"></p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>39</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@130497@01@13@01@17@03@01@db3@mtd1@dk1@dpt0@000123_1569724125.png"><br>
Hình trên có {}&nbsp;cái túi.</p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>40</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image.png1587460497223"><br>
Hình trên&nbsp;có bao nhiêu quyển vở?<br>
Trả lời: {} quyển vở.</p>
</div><div>ĐÁP ÁN ĐÚNG: 7
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>41</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án thích hợp để điền vào ô trống.<br>
Cho hình vẽ sau:<br>
<img alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00123_2_1569808692.png"><br>
Số người tuyết trên hình là: {}.</p>
</div><div>ĐÁP ÁN ĐÚNG: <span><p>8</p>
</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>42</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Cách đọc đúng của số sau là:<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00066_1569808692.png"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div>Bảy</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Tám</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Chín</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>43</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu cái cây?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00112_1569808692.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;cái cây</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;cái cây</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;cái cây</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>44</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án&nbsp;đúng.<br>
Có bao nhiêu cái ô tô trong hình sau?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd2@dk1@dpt0@00063_1569808692.png"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;cái ô tô</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;cái ô tô</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;cái ô tô</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;cái ô tô</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>45</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00102_1569808692.png"><br>
Hình trên có bao nhiêu&nbsp;cái kem?<br>
Trả lời: {} cái kem.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>46</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>&nbsp;Bạn hãy điền số&nbsp;thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00077_1569808692.png"><br>
Số thích hợp điền vào dấu hỏi chấm là {}.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>47</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình sau&nbsp;có bao nhiêu quyển vở?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00100_1569808692.png"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;quyển vở</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8 "><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;quyển vở</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;quyển vở</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span>&nbsp;quyển vở</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>48</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu khúc xương?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00119_1569808692.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>49</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Cho hình sau:<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620525369755.png"><br>
Trong hình trên có bao nhiêu chậu cây?<br>
Trả lời: {} chậu cây.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>50</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Cho hình vẽ:<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620521926851.png"><br>
Hình đã cho có bao nhiêu cục tẩy?<br>
Trả lời: {} cục tẩy.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>51</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Cho hình sau:<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620379931581.png"><br>
Trong hình trên&nbsp;có bao nhiêu hộp sữa?<br>
Trả lời: {} hộp sữa.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>52</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00103_1569808692.png"><br>
Hình trên có bao nhiêu&nbsp;chiếc đàn?<br>
Trả lời: {} chiếc đàn.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>53</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00120_1569808692.png"><br>
Hình trên có bao nhiêu&nbsp;chai nước ngọt?<br>
Trả lời: {} chai nước ngọt.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>54</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình có bao nhiêu&nbsp;con bò sữa?<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620357717163.png"><br>
Trả lời: {} con bò sữa.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>55</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00137_1569808692.png"><br>
Hình trên có bao nhiêu&nbsp;quả lê?<br>
Trả lời: {} quả lê.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>56</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu quả cà chua?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00065_1569808692.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;quả cà chua</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;quả cà chua</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;quả cà chua</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>57</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình có bao nhiêu&nbsp;con chó?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00080_1569808692.png"><br>
Trả lời: {} con chó.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>58</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu con chim?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00070_1569808692.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> con chim</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;con chim</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;con chim</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;con chim</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>59</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620359449716.png"><br>
Hình nào trong các hình trên có <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> quả bóng?</p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Hình <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="1"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">1</span></span></span></span></span></span></span></p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Hình <span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="2"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">2</span></span></span></span></span></span></span></p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>60</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong bể nước có bao nhiêu&nbsp;con cá vàng?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00122_1569808692.png"><br>
Trả lời: {} con cá vàng.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>61</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00093_1569808692.png"><br>
Trong hình có bao nhiêu chiếc&nbsp;máy bay?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;chiếc máy bay</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;chiếc máy bay</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;chiếc máy bay</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>&nbsp;chiếc máy bay</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>62</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình sau có bao nhiêu&nbsp;chiếc đồng hồ đeo tay?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00131_1569808692.png"><br>
Trả lời: {} chiếc đồng hồ đeo tay.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>63</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình sau có bao nhiêu&nbsp;cây xương rồng?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00085_1569808692.png"><br>
Trả lời: {} cây xương rồng.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>64</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu bắp ngô?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00069_1569808692.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;bắp ngô</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;bắp ngô</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;bắp ngô</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;bắp ngô</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>65</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu cốc&nbsp;nước?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00101_1569808692.png"></p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;cốc nước</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;cốc nước</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="4"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">4</span></span></span></span></span></span></span>&nbsp;cốc nước</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;cốc nước</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>66</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình có bao nhiêu&nbsp;cái ghế?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00081_1569808692.png"><br>
Trả lời: {} cái ghế.</p>
</div><div>ĐÁP ÁN ĐÚNG: 8
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>67</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Cho hình vẽ:<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620521732676.png"><br>
Hình đã cho có bao nhiêu hình trái tim?<br>
Trả lời: {} hình trái tim.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>68</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng để điền vào ô trống.<br>
<img src="https://s3.vio.edu.vn/image_1620370347969.png"><br>
Số thích hợp điền vào dấu hỏi chấm là: {}.</p>
</div><div>ĐÁP ÁN ĐÚNG: <span><p>8</p>
</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>69</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
Trong hình có bao nhiêu con cá?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00111_1569808692.png"></p>
</div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;con cá</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;con cá</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;con cá</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>70</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620294631169.png"><br>
Hình trên có bao nhiêu chậu hoa?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;chậu hoa</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;chậu hoa</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;chậu hoa</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>71</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình dưới đây có tất cả bao nhiêu cái tên lửa?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00127_1569808692.png"><br>
Trả lời: {} cái tên lửa.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>72</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@0@100397@01@13@01@20@03@02@db1@mtd1@dk1@dpt0@00057_1569808692.png"><br>
Hình trên có bao nhiêu con bò?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span>&nbsp;con bò</p>
</div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span>&nbsp;con bò</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span>&nbsp;con bò</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span>&nbsp;con bò</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>73</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
Trong hình có bao nhiêu&nbsp;cái ô?<br>
<img class="img-responsive" alt="img_question" src="https://s3.vio.edu.vn/image_question/@2@0@100397@01@13@01@20@03@02@db3@mtd1@dk1@dpt0@00084_1569808692.png"><br>
Trả lời: {} cái ô.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>74</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620359368033.png"><br>
Khẳng định nào dưới đây đúng?</p>
</div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Trong hình có&nbsp;<span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> cái váy.</p>
</div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Trong hình có&nbsp;<span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> cái váy.</p>
</div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Trong hình có&nbsp;<span class="math-tex" style="font-size: 18px;;;;;"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> cái váy.</p>
</div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>75</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>
<img class="img-responsive" src="https://s3.vio.edu.vn/image_1620356527783.png"><br>
Hình vẽ trên có bao nhiêu bông hoa?<br>
Trả lời: {} bông hoa.</p>
</div><div>ĐÁP ÁN ĐÚNG: 9
</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>76</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br><img class="img-responsive" src="https://s3.vio.edu.vn/image_question/a1311_1700703757.png" alt="img_question">  <br>Có mấy ngón tay đang được giơ lên?<br>Trả lời: {} ngón tay.<br></p></div><div>ĐÁP ÁN ĐÚNG: 7</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>77</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br><img class="img-responsive" src="https://s3.vio.edu.vn/image_question/a1321_1700703757.png" alt="img_question">  <br>Trong khay có mấy quả trứng?<br>Trả lời: {} quả trứng.<br></p></div><div>ĐÁP ÁN ĐÚNG: 8</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>78</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br><img class="img-responsive" src="https://s3.vio.edu.vn/image_question/a1331_1700703757.png" alt="img_question">  <br>Trong hình có mấy chú lùn?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="5"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">5</span></span></span></span></span></span></span> chú lùn</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> chú lùn </p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> chú lùn</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>79</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>Em hãy chọn tên con vật có <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> chân.<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Mèo</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Cá hề</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Nhện</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>80</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br><img class="img-responsive" src="https://s3.vio.edu.vn/image_question/a1351_1700703757.png" alt="img_question">  <br>Có mấy bạn nhỏ đang băng qua đường?<br></p></div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> bạn nhỏ</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> bạn nhỏ</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> bạn nhỏ</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>81</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng để điền vào ô trống.<br><img src="https://s3.vio.edu.vn/image_question/a1361_1700703757.png" alt="img_question">  <br>Trong thực đơn có mấy món ăn?<br>Trả lời: {} món ăn.<br></p></div><div>ĐÁP ÁN ĐÚNG: <span>8</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>82</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy điền số thích hợp vào ô trống.<br>Cho hình sau:<br><img class="img-responsive" src="https://s3.vio.edu.vn/image_question/a1371_1700703757.png" alt="img_question">  <br>Trên cánh con bọ có bao nhiêu chấm tròn? <br>Trả lời: {} chấm tròn.<br></p></div><div>ĐÁP ÁN ĐÚNG: 9</div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>83</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>Cho hình sau:<br><img class="img-responsive" src="https://s3.vio.edu.vn/image_question/a1381_1700703757.png" alt="img_question">  <br>Đáp án nào dưới đây đúng?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><img src="https://s3.vio.edu.vn/image_question/a1382_1700703757.png" alt="img_question">  <br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><img src="https://s3.vio.edu.vn/image_question/a1383_1700703757.png" alt="img_question">  <br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>84</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br>Bạn Lan cần vẽ <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> quả táo.<br>Hình bạn Lan cần vẽ là:<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><img src="https://s3.vio.edu.vn/image_question/a1391_1700703757.png" alt="img_question">  <br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><img src="https://s3.vio.edu.vn/image_question/a1392_1700703757.png" alt="img_question">  <br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>85</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án thích hợp điền vào ô trống.<br><img src="https://s3.vio.edu.vn/image_question/a13101_1700703757.png" alt="img_question">  <br>Vỉ thuốc trên có {} viên thuốc.<br></p></div><div>ĐÁP ÁN ĐÚNG: <span>9</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>86</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br><img class="img-responsive" src="https://s3.vio.edu.vn/image_question/a13121_1700703757.png" alt="img_question">  <br>Mũi tên đang chỉ vào tầng mấy?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Tầng <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span></p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p>Tầng <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span></p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p>Tầng <span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span></p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>87</strong> -NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án thích hợp để điền vào ô trống.<br><img src="https://s3.vio.edu.vn/image_question/a13131_1700703757.png" alt="img_question">  <br>Nhà bạn Hoa ở tầng {}.<br></p></div><div>ĐÁP ÁN ĐÚNG: <span>bảy</span></div><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>88</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h1_1708417504.png" alt="img_question"><br>Con bạch tuộc trên có mấy cái tua?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> cái tua</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> cái tua</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> cái tua</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> cái tua</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>89</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h3_1708417504.png" alt="img_question"><br>Con gà trên đẻ được mấy quả trứng?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> quả trứng</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> quả trứng</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> quả trứng</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> quả trứng</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>90</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h5_1708417504.png" alt="img_question"><br>Hình trên có mấy con bướm?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> con bướm</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> con bướm</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> con bướm</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> con bướm</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>91</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h7_1708417504.png" alt="img_question"><br>Hình trên có mấy con bướm?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> con bướm</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> con bướm</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> con bướm</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> con bướm</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>92</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h9_1708417504.png" alt="img_question"><br>Hình trên có bao nhiêu quả bưởi?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> quả</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> quả</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> quả</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>93</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h11_1708417504.png" alt="img_question"><br>Hình trên có bao nhiêu quả bưởi?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> quả</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> quả</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> quả</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>94</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h13_1708417504.png" alt="img_question"><br>Hình trên có bao nhiêu củ cà rốt?<br></p></div><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> củ cà rốt</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> củ cà rốt</p><br></div></li><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> củ cà rốt</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> củ cà rốt</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div><div><div class="panel panel-preview-primary panel-preview-question"><div class="panel-heading">Câu hỏi <strong>95</strong> -  NHẬN BIẾT</div><div class="panel-body"><div><p>Bạn hãy chọn đáp án đúng.<br> <img class="img-responsive" src="https://s3.vio.edu.vn/image_question/cs789h15_1708417504.png" alt="img_question"><br>Bông hoa trên có bao nhiêu cánh?<br></p></div><li class="answerChoice correctAnswer" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="8"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">8</span></span></span></span></span></span></span> cánh hoa</p><br></div><span class="answerChoiceCorrect"><i class="fa fa-check-circle-o" style="color: rgb(133, 192, 86); margin-left: 5px;"></i></span></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="6"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">6</span></span></span></span></span></span></span> cánh hoa</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="7"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">7</span></span></span></span></span></span></span> cánh hoa</p><br></div></li><li class="answerChoice false" style="list-style: none; display: flex; align-items: center;"><div><p><span class="math-tex" style="font-size: 18px"><span class="mjpage"><span class="mjx-chtml"><span class="mjx-math" aria-label="9"><span class="mjx-mrow" aria-hidden="true"><span class="mjx-mn"><span class="mjx-char MJXc-TeX-main-R" style="padding-top: 0.372em; padding-bottom: 0.372em;">9</span></span></span></span></span></span></span> cánh hoa</p><br></div></li><div><button class="btn btn-default">Xem giải thích</button></div><button class="btn btn-default pull-right">Chọn câu hỏi</button></div></div></div></div>
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
