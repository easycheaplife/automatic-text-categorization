# encoding=utf-8
import HTMLParser
import sys
reload(sys)   
sys.setdefaultencoding('utf-8')

buf = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 也许每一个男子全都有过这样的两个女人，至少两个'
buf = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 也许每一个男子全都有过这样的两个女人，至少两个．娶了红玫瑰，久而久之，红的变了墙上的一抹蚊子血，白的还是“床前明月光”；娶了白玫瑰，白的便是衣服上的一粒饭粘子，红的却是心口上的一颗朱砂痣。&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; --【红玫瑰与白玫瑰】原著：&nbsp;&nbsp;&nbsp; 张爱玲编剧：&nbsp;&nbsp;&nbsp; 刘恒林 亦华导演：&nbsp;&nbsp;&nbsp; 关锦鹏摄影：&nbsp;&nbsp;&nbsp; 杜可风美术指导：朴若木色彩：&nbsp;&nbsp;&nbsp; 彩色片长：&nbsp;&nbsp;&nbsp; 110min分级：&nbsp;&nbsp;&nbsp; 芬兰/K-16语言：&nbsp;&nbsp;&nbsp; 粤语外文别名：Red Rose White Rose(1994)主演：&nbsp;&nbsp;&nbsp; 赵文宣&nbsp; 饰&nbsp; 佟振保&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 陈&nbsp; 冲&nbsp; 饰&nbsp; 王娇蕊&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 叶玉卿&nbsp; 饰&nbsp; 孟烟郦获奖：&nbsp;&nbsp; 台湾电影金马奖最佳女主角、最佳剧本、最佳美术设计、最佳造型设计、最佳电影音乐【剧情简介】&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 振保的生命里就有两个女人，他说一个是他的白玫瑰，一个是他的红玫瑰。一个是圣洁的妻，一个是热烈的情妇……留洋回来的振保(赵文瑄饰)在一家外商公司谋了个高职。为了交通方便，他租了老同学王士洪的屋子。振保留学期间，有一个叫玫瑰的初恋情人。他曾因拒绝过玫瑰的求欢而获取了“柳下惠”的好名声。王士洪有一位风情万种的太太，她总令振保想入非非。有一次，士洪去新加坡做生意了，经过几番灵与肉的斗争，在一个乍暖还寒的雨日，振保被这位叫娇蕊(陈冲饰)的太太“囚住”了。令振保所料不及的是娇蕊这次是付出了真爱的。当她提出把真相告诉了王士洪时，振保病倒了。在病房，振保把真实的一面告诉了娇蕊——他不想为此情而承受太多责难。娇蕊收拾她纷乱的泪珠，出奇的冷静起来，从此走出了他的生命。　　在母亲撮合下，振保带着点悲凉的牺牲感，娶了身材单薄、静如止水的孟烟鹂(叶玉卿饰)。新娘给人的感觉只是笼统的白净，她无法唤起振保的性欲。振保开始在外边嫖妓。可是有一天，他竟发现了他的阴影里没有任何光泽的白玫瑰烟鹂，居然和一个形象猬狎的裁缝关系暧昧。从此，振保在外边公开玩女人，一味地放浪形骸起来。有一天，他在公共汽车上巧遇了他生命中的“红玫瑰”娇蕊，她已是一种中年人的俗艳了。岁月无情，花开花落，在泪光中，振保的红玫瑰与白玫瑰已是一种现实中的幻影。旧日的善良一点一点地逼近振保。回到家，在一番歇斯底里的发作后，振保又重新变成了一个好人。 上一页&nbsp;[1]&nbsp;[2]&nbsp;[3]&nbsp;[4]&nbsp;[5]&nbsp;[6]&nbsp;[7]&nbsp;[8]&nbsp;[9]&nbsp;下一页&nbsp;'
html_parser = HTMLParser.HTMLParser()
print html_parser.unescape(buf) 


