# coding=utf-8
import requests,wx,json
# 生日，ID，签名，等级，大会员状态 = "https://api.bilibili.com/x/space/acc/info?mid={uid}"
# 关注数，粉丝数 = "https://api.bilibili.com/x/relation/stat?vmid={uid}"
# 投稿信息 = "https://api.bilibili.com/x/space/navnum?mid={uid}"
# 总计播放量 = "https://api.bilibili.com/x/space/upstat?mid={uid}"
# 视频信息 = "https://api.bilibili.com/x/web-interface/archive/stat?aid={aid}"
# 通过av号视频标签 = "https://api.bilibili.com/x/tag/archive/tags?aid={aid}"
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='bilibili-query-information V2.0', size=(500,345))
        panel = wx.Panel(parent=self)
        self.official_logo = wx.Icon('bilibili-official logo.ico',wx.BITMAP_TYPE_ICO)
        self.project_logo = wx.Icon('bilibili-project logo.ico',wx.BITMAP_TYPE_ICO)
        self.state = 0
        self.SetIcon(self.project_logo)
        self.st1 = wx.StaticText(panel,label='用户ID：')
        self.tc = wx.TextCtrl(panel)
        self.tc.SetValue('687889425')
        self.st2 = wx.StaticText(panel,label='TIP：初始ID为作者ID，输入不存在符合标准的ID所有项为0')
        self.button = wx.Button(parent=panel,label='查询',pos=(100,50))
        self.ico = wx.Button(parent=panel,label='更换图标',pos=(100,50))
        self.copyright_notice = wx.Button(parent=panel,label='版权声明(Copyrights Notice)',pos=(100,50))
        self.Bind(wx.EVT_BUTTON, self.on_click,self.button)
        self.Bind(wx.EVT_BUTTON, self.on_ico,self.ico)
        self.Bind(wx.EVT_BUTTON, self.on_con,self.copyright_notice)
        self.fs = wx.StaticText(panel,label='粉丝数：？')
        self.gz = wx.StaticText(panel,label='关注数：？')
        self.nc = wx.StaticText(panel,label='昵称：？')
        self.xb = wx.StaticText(panel,label='性别：？')
        self.txlj = wx.StaticText(panel,label='头像链接：？')
        self.gxqm = wx.StaticText(panel,label='个性签名：？')
        self.dj = wx.StaticText(panel,label='等级：？')
        self.sr = wx.StaticText(panel,label='生日：？')
        self.error = wx.StaticText(panel,label='')

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.st1,flag=wx.LEFT,border=10)
        vbox.Add(self.tc,flag=wx.EXPAND,border=10)
        vbox.Add(self.st2,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        vbox.Add(self.ico,flag=wx.EXPAND,border=10)
        vbox.Add(self.copyright_notice,flag=wx.EXPAND,border=10)
        vbox.Add(self.fs,flag=wx.EXPAND,border=10)
        vbox.Add(self.gz,flag=wx.EXPAND,border=10)
        vbox.Add(self.nc,flag=wx.EXPAND,border=10)
        vbox.Add(self.xb,flag=wx.EXPAND,border=10)
        vbox.Add(self.txlj,flag=wx.EXPAND,border=10)
        vbox.Add(self.gxqm,flag=wx.EXPAND,border=10)
        vbox.Add(self.dj,flag=wx.EXPAND,border=10)
        vbox.Add(self.sr,flag=wx.EXPAND,border=10)
        vbox.Add(self.error,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def apif(self,apit,state):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}
        try:
            data = requests.get(apit,headers=headers)
        except:
            sc = 'error'
        else:
            sc = 200
        if sc == 200:
            self.error.SetLabelText('')
            if state == 0:
                cache = data.text
                cache2 = json.loads(cache)
                cache3 = cache2['data']
                res = []
                res.append(cache3['following'])
                res.append(cache3['follower'])
                return res
            elif state == 1:
                cache = data.text
                cache2 = json.loads(cache)
                cache3 = cache2['data']
                cache4 = cache3['name']
                cache5 = cache3['sex']
                cache6 = cache3['face']
                cache7 = cache3['sign']
                cache8 = cache3['level']
                cache10 = cache3['birthday']
                res = []
                res.append(cache4)
                res.append(cache5)
                res.append(cache6)
                res.append(cache7)
                res.append(cache8)
                res.append(cache10)
                return res
        else:
            self.error.SetLabelText('ERROR：出现错误，可能是程序出错、ID输入错误或未连接网络，请检查后重试！')
            return 'error'
    def on_click(self,event):
        cache = self.apif('https://api.bilibili.com/x/relation/stat?vmid=' + self.tc.GetValue(),0)
        if cache != 'error':
            self.gz.SetLabelText('关注数：' + str(cache[0]))
            self.fs.SetLabelText('粉丝数：' + str(cache[1]))
        cache = self.apif('https://api.bilibili.com/x/space/acc/info?mid=' + self.tc.GetValue(),1)
        if cache != 'error':
            self.nc.SetLabelText('昵称：' + cache[0])
            self.xb.SetLabelText('性别：' + cache[1])
            self.txlj.SetLabelText('头像链接：' + cache[2])
            self.gxqm.SetLabelText('个性签名：' + cache[3])
            self.dj.SetLabelText('等级：' + str(cache[4]))
            self.sr.SetLabelText('生日：' + cache[5])
    def on_ico(self,event):
        self.error.SetLabelText('')
        if self.state == 0:
            self.SetIcon(self.official_logo)
            self.state = 1
        elif self.state == 1:
            self.SetIcon(self.project_logo)
            self.state = 0
        else:
            self.error.SetLabelText('ERROR：出现错误，可能是源代码出错，请报告作者。')
    def on_con(self,event):
        dhk = wx.MessageDialog(parent=self,message="请确保该项目获取渠道为Github或Gitee，其他平台均为盗版！",caption='版权声明(Copyrights Notice)',style=wx.OK | wx.ICON_WARNING)
        if dhk.ShowModal() == wx.ID_OK:
            pass
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()