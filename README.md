BJTU2018-2019学年新教务系统抢课脚本
======
## 环境要求：
  请先确保电脑已有python安装环境
  * selenium库
  * chrome webdriver
  * 耐得住寂寞的性子
  
------
## 文件配置：
  * ### user_id_str：<br>
     学号
  * ### password_str：<br>
     mis系统登陆密码
  * ### 要选的课(此处以chrome为例)：<br>
     f12选择该课程的最左侧一栏，右键copy Xpath，将def duoxuan()中<br>
     driver.find_element_by_xpath()中的内容替换即可
  * ### delta:
     刷新间隔，1秒足矣
     
------
## 声明：
  * 感谢几位大佬的合作，不胜荣幸
  * ### 该脚本仅供技术交流使用，请勿用于实际抢课操作
  * 欢迎各位多多探讨，从而能够对该脚本进行进一步优化
