# coding=utf-8
import requests
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='查询Bilibili基本数据', size=(500,250))
        panel = wx.Panel(parent=self)
        self.icon = wx.Icon('bilibili-logo.ico',wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.st1 = wx.StaticText(panel,label='用户ID：')
        self.tc = wx.TextCtrl(panel)
        self.tc.SetValue('687889425')
        self.st2 = wx.StaticText(panel,label='TIP：初始ID为作者ID')
        self.button = wx.Button(parent=panel,label='查询',pos=(100,50))
        self.Bind(wx.EVT_BUTTON, self.on_click,self.button)
        self.fs = wx.StaticText(panel,label='粉丝数：？')
        self.gz = wx.StaticText(panel,label='关注数（不包括悄悄关注）：？')
        self.hzs = wx.StaticText(panel,label='获赞数：？')
        self.bfs = wx.StaticText(panel,label='播放数：？')
        self.yds = wx.StaticText(panel,label='阅读量：？')
        self.error = wx.StaticText(panel,label='')

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.st1,flag=wx.LEFT,border=10)
        vbox.Add(self.tc,flag=wx.EXPAND,border=10)
        vbox.Add(self.st2,flag=wx.EXPAND,border=10)
        vbox.Add(self.button,flag=wx.EXPAND,border=10)
        vbox.Add(self.fs,flag=wx.EXPAND,border=10)
        vbox.Add(self.gz,flag=wx.EXPAND,border=10)
        vbox.Add(self.hzs,flag=wx.EXPAND,border=10)
        vbox.Add(self.bfs,flag=wx.EXPAND,border=10)
        vbox.Add(self.yds,flag=wx.EXPAND,border=10)
        vbox.Add(self.error,flag=wx.EXPAND,border=10)
        panel.SetSizer(vbox)
    def on_click(self,event):
        api = 'https://api.bilibili.com/x/relation/stat?vmid=' + self.tc.GetValue()
        try:
            requests.get(api)
        except:
            sc = 'error'
        else:
            sc = 200
        if sc == 200:
            self.error.SetLabelText('')
            xx = requests.get(api)
            xx_t = xx.text
            xx_tl = []
            i = 0
            for i in range(len(xx_t)):
                xx_tl.append(xx_t[i])
            i = 0
            del xx_tl[0:46]
            print(xx_tl)
            for i in range(2):
                del xx_tl[-1]
            print(xx_tl)
            i = 0
            while 1:
                i += 1
                if xx_tl[i] == ',':
                    break
            i += 1
            del xx_tl[0:i]
            del xx_tl[0:12]
            print(xx_tl)
            i = 0
            while 1:
                i += 1
                if xx_tl[i] == ',':
                    break
            i += 1
            by = xx_tl[0:i]
            i = 0
            gzs = ''
            for i in range(len(by) - 1):
                gzs += by[i]
            self.gz.SetLabelText('关注数（不包括悄悄关注）：' + str(gzs))
            del xx_tl[0:i]
            del xx_tl[0:10]
            print(xx_tl)
            i = 0
            while 1:
                i += 1
                if xx_tl[i] == ',':
                    break
            i += 1
            del xx_tl[0:i]
            del xx_tl[0:8]
            print(xx_tl)
            i = 0
            while 1:
                i += 1
                if xx_tl[i] == ',':
                    break
            i += 1
            del xx_tl[0:i]
            del xx_tl[0:11]
            print(xx_tl)
            fcs = ''
            i = 0
            for i in range(len(xx_tl)):
                fcs += xx_tl[i]
            self.fs.SetLabelText('粉丝数：' + fcs)
        else:
            self.error.SetLabelText('ERROR：出现错误，可能是程序出错、ID输入错误或未连接网络，请检查后重试！')
app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()