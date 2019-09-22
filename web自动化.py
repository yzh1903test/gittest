#!/usr/python
#-*-c0ding:utf-8-*-
#导入webdriver模块
from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
import time
import selenium.webdriver.support.ui as ui
import warnings
warnings.filterwarnings('ignore')
#使用谷歌浏览器操作
dr=webdriver.Chrome()  #谷歌
# dr=webdriver.Firefox() #火狐
# #设置浏览器窗口大小
# dr.set_window_size(1280,1024)
#
# #设置浏览器窗口的位置
# # dr.set_window_position(500,500)
#
# 请求获取url地址
# dr.get('https://www.baidu.com')
# dr.get('https://qzone.qq.com/')#获取QQ网址
# dr.get('file:///C:/Users/yzh2019/Documents/tencent%20files/446794967/filerecv/abc.html')
# time.sleep(3)
#页面最大化
dr.maximize_window()
time.sleep(1)
# dr.minimize_window()
# time.sleep(2)
#切换进入iframe内嵌框架

# dr.switch_to.frame('login_frame') #切换至内嵌框架  值只能是ID，或name  若没有则定位到框架本身，再切换

#退出到原始框架(网站首页)
# dr.switch_to.default_content()

#退出到上一层框架（父框架）
# dr.switch_to.parent_frame()

#获取当前网页窗口的句柄
# print(dr.current_window_handle)

#获取所有网页窗口的句柄
# print(dr.window_handles)

#切换窗口
# dr.switch_to.window('''句柄值''')

# #页面最小化
# # dr.minimize_window()

# dr.get('https://www.jd.com')#获取京东
# #回退到上一个页面
# #dr.back()#回退到百度
# #time.sleep(3)

# #前进到下个页面
# # dr.forward()#前进到京东
#
# #获取标题
# print(dr.title)
#
# # 断言：将实际结果与预期结果做对比
# # assert dr.title=='百度一下，你就知道'
#
# #获取网址
# print(dr.current_url)
#
# #休眠
# time.sleep(3)
#
# #关闭浏览器
# dr.quit()


'''selenumium核心 定位（8中）'''
#1.id定位 唯一的
#动作：点击click(),输入send_keys('内容')
# dr.find_element_by_id('kw').send_keys('python')
# time.sleep(3)
# dr.find_element_by_id('su').click()
# time.sleep(3)
# dr.quit()

# 2.class定位 唯一的
# dr.find_element_by_class_name('s_ipt').send_keys('香港暴乱')
# dr.find_element_by_class_name('s_ipt').click()
# time.sleep(3)
# dr.quit()

# #3.name定位
# s=dr.find_element_by_name('wd').click()
# time.sleep(3)
# dr.quit()

# #4.text文本定位
# x=dr.find_element_by_link_text('新闻').click()
# time.sleep(3)
# dr.quit()

#5.partial_link_text 模糊文本定位
# q=dr.find_element_by_partial_link_text('hao').click()
# time.sleep(3)
# dr.quit()

#6.tag_name 标签定位 不唯一
#dr.find_element_by_tag_name('')

#7.xpath 路径定位 xpath：路径标记语言
# e=dr.find_element_by_xpath('//*[@id="kw"]')
# dr.quit()

#8.css selector 通过css层叠样式表定位
# r=dr.find_element_by_css_selector('#kw')
# dr.quit()

#>>>qq空间登录
# QQ=dr.find_element_by_css_selector('#img_out_446794967').click()
# time.sleep(2)
# ss=dr.find_element_by_css_selector('#QM_Profile_Mood_A > span').click()
# time.sleep(1)
# dr.find_element_by_xpath('//*[@id="qz_poster_v4_editor_container_1"]/div[1]').click()
# dr.find_element_by_css_selector('#\$1_content_content').send_keys('来自自动化测试，请不要关注，不要查看！')











#>>>qq邮箱登录
# QQ=dr.find_element_by_css_selector('#switcher_plogin').click()
# User=dr.find_element_by_css_selector('#u').send_keys('446794967')
# Passwrod=dr.find_element_by_css_selector('#p').send_keys('19951022@@Wbao')
# DengLu=dr.find_element_by_xpath('//*[@id="login_button"]').click()
# time.sleep(5)

#>>>定位一组元素:一次性定位到多个某些属性相同的元素
#层级定位:先定义到大的范围，再从大的范围定位元素
# ww =dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in ww:
#     i.click()
#     print(i.text)
#     time.sleep(3)
# print(len(ww))


#京东层级定位
# jd =dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
# for i in jd:
#     print(i.text)
#     time.sleep(1)
# print(len(jd))


#>>>处理弹出框
# dr.find_element_by_xpath('/html/body/button').click()
# time.sleep(2)

# dr.get('https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_9bae2007e1854cac99a57cdaa67e0234')
# time.sleep(2)
#切换到弹出框
# ww=dr.switch_to_alert()
#
# #获取弹窗上的文本
# t=ww.text
# print(t)
#
# #输入数据
# ww.send_keys('python')
# time.sleep(3)
#
# #点击取消
# # ww.dismiss()
#
# #点击弹出框山的“确定”
# ww.accept()

#控制浏览器内JavaScript的滚动条:"arguments[0].scrollIntoView();"
# dd=dr.find_element_by_xpath('//*[@id="J_seckill"]/div/div/a/div[1]')
# time.sleep(3)
# #执行javas语句
# dr.execute_script('arguments[0].scrollIntoView();',dd)

#根据距离控制浏览器的滚动条
# for i in range(0,10000,200):
#     js=f"var q=document.documentElement.scrollTop={i}"
# #执行javas语句0
#     dr.execute_script(js)
#     time.sleep(2)

#模拟鼠标的操作
#将鼠标移动到元素中心
# ss=dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[12]/a[2]')
# time.sleep(2)
# #鼠标移动动作链
# ActionChains(dr).move_to_element(ss).perform()
                  # 移动到元素            执行
# jd =dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
# time.sleep(1)
# for i in jd:
#     ActionChains(dr).move_to_element(i).perform()

#qq空间拖拽
dr.get('https://qzone.qq.com/')
time.sleep(2)
#创建一个智能等待
until=ui.WebDriverWait(dr,10)
#设置智能等待
un.until(lambda dr:dr.find_element_by_xpath('//*[@id="lay"]/div[2]/div/div[1]/h1/i').is_displayed())
dr.switch_to.frame('login_frame')
time.sleep(2)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
time.sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('7894546')
time.sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('6546jgjgjhf')
time.sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(2)
dr.switch_to.frame('tcaptcha_iframe')
ww=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
time.sleep(2)
'''drag_and_drop 拖拽从起始位置拖到目的位置
 drag_and_drop(起始，目的)
 drag_and_drop_by_offset 拖拽从起始位置拖到某个点的位置
 drg_and_drop_by_offset(起始i,x,y)'''''
ActionChains(dr).drag_and_drop_by_offset(ww,180,0).perform()

