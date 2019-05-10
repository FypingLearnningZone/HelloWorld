import smtplib
import csv
import time
import os
import random

from email.mime.text import MIMEText
from email.utils import formataddr

content_set = '''{}：

你好！

我多年从事软件著作权的申请工作，经手的软著2000+以上，有丰富的申请经验，可以全程代办申请软件著作权的事项。并可以代写程序和说明书，您只需要提供一个名称或方向即可。

申请软著费用：199元，代写程序说明书：299元。 全包只要498元。百分百拿证，可签订合同，拿到证书后付款。

申请软著可以用于高新企业认定，申请政府补贴，公司资质展示，个人加分项等。

软著拿证速度快（30个工作日左右），无后续费用，申请成本低，是企业个人最有性价比的资质。

如有疑问请随时联系，谢谢！

电话/微信：17157425298
地址：上海市浦东新区浙桥路277号'''

headers = ['发送地址','接收地址','内容','是否成功','时间']

history_filename = time.strftime("%Y-%m-%d-%H-%M", time.localtime())+".csv"

if not os.path.exists(history_filename):#以一分钟为间隔 如果记录文件不存在 创建文件 添加表头 ,如果存在则直接使用
    with open(history_filename,'a') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)

    

def read_send_user_csv():
    '''读取发送用户列表'''
    send_user_list = []
    with open('send_user.csv') as f:
        f_csv = csv.reader(f) 
        # headers = next(f_csv) 去除表头
        for row in f_csv:
            if len(row) != 0:
                send_user_obj = {}
                send_user_obj["user_name"] = row[0]
                send_user_obj["pass_word"] = row[1]
                send_user_list.append(send_user_obj)
    return send_user_list
        

def read_receive_user_csv():
    '''读取接收用户列表'''
    receive_user_list = []
    with open('receive_user.csv') as f:
        f_csv = csv.reader(f) 
        # headers = next(f_csv) 去除表头
        for row in f_csv:
            if len(row) != 0:
                receive_user_obj = {}
                receive_user_obj["user_addr"] = row[1]
                receive_user_obj["user_company"] = row[0]
                receive_user_list.append(receive_user_obj)
    return receive_user_list

def write_csv(rows):
    '''写入发送记录'''
    with open(history_filename,'a') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)

def send_mail(content,my_users,my_sender,my_pass):
    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["软著申请", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["用户", ""])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "软件著作权申请说明"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_users, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    #写入csv记录
    rows = [(my_sender,my_users,"123",ret,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))]
    write_csv(rows)
    print(my_users,my_sender,ret)
    return ret


def main_work():
    while True:
        count = 0
        send_user_list = read_send_user_csv()
        receive_user_list = read_receive_user_csv()
        te_count = 0
        for i in receive_user_list:
            
            count = count +1
            te_count = te_count + 1
            if te_count == 100:
                te_count = 0
                send_mail(content_set.format("te"),"1614056450@qq.com",match_sender["user_name"],match_sender["pass_word"])
            print(count)
            match_sender = send_user_list[random.randint(0,len(send_user_list)-1)]#随机选择用户
            # receive_user = str(i["user_addr"]) 
            # send_mail(content_set.format(receive_user[0:receive_user.index("@")]),receive_user,match_sender["user_name"],match_sender["pass_word"])
            send_mail(content_set.format(i["user_company"]),i["user_addr"],match_sender["user_name"],match_sender["pass_word"])
            time.sleep(random.randint(60,60*10))
        # time.sleep(random.randint(1,5))#暂停随机秒数
        # time.sleep(100) #暂停随机秒数
        break

if __name__ == '__main__':
    main_work()