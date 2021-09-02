import kivy  
       
# base Class of your App inherits from the App class.    
# app:always refers to the instance of your application   
from kivy.app import App 
     
# this restrict the kivy version i.e  
# below this kivy version you cannot  
# use the app or software  
kivy.require('1.9.0')
  
# Builder is used when .kv file is
# to be used in .py file
from kivy.lang import Builder
  
# The screen manager is a widget
# dedicated to managing multiple screens for your application.
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition) 
   
# You can create your kv code in the Python file
Builder.load_string("""
<MyButton@Button>
    background_normal: ''
    background_color: 0,0,0,0
    font_name: './yahei.ttf'
<MyTextInput@TextInput>:
    canvas.before:
        # Draw border first
        Color:
            rgba: 1,0,0,1
        Rectangle:
            size: self.size
            pos: self.pos
        # Draw background (covers most of the above border)
        Color:
            rgba: 0,0,0,1
        Rectangle:
            size: (self.width - self.border[1] - self.border[3], self.height - self.border[0] - self.border[2])
            pos: (self.x + self.border[3], self.y + self.border[0])
        # set the color for the text
        Color:
            rgba: 1,1,1,1
<MenuScreen>:
    GridLayout:
        cols:8
        MyButton:  
            text: '乾'
            on_release:
                root.manager.current = 'Screenqian'
                root.manager.transition.direction = 'right'
        MyButton:
            text: '兑'
            on_release:
                root.manager.current = 'Screendui'
                root.manager.transition.direction = 'right'
        MyButton:
            text: '离'
            on_release:
                root.manager.current = 'Screenli'
                root.manager.transition.direction = 'right'
        MyButton:
            text: '震'
            on_release:
                root.manager.current = 'Screenzhen'
                root.manager.transition.direction = 'right'
            
        MyButton:
            text: '巽'
            
        MyButton:
            text: '坎'
            
        MyButton:
            text: '艮'
            
        MyButton:
            text: '坤'
        Button:
            text: '1'
            on_release:
                root.manager.current = 'Screen1'
                root.manager.transition.direction = 'right'
        Button:
            text: '43'
            on_release:
                root.manager.current = 'Screen43'
                root.manager.transition.direction = 'left'
        Button:
            text: '14'
            on_release:
                root.manager.current = 'Screen14'
                root.manager.transition.direction = 'left'
        Button:
            text: '34'
            on_release:
                root.manager.current = 'Screen34'
                root.manager.transition.direction = 'left'
        Button:
            text: '9'
            on_release:
                root.manager.current = 'Screen9'
                root.manager.transition.direction = 'left'
        Button:
            text: '5'
            on_release:
                root.manager.current = 'Screen5'
                root.manager.transition.direction = 'left'
        Button:
            text: '26'
            on_release:
                root.manager.current = 'Screen26'
                root.manager.transition.direction = 'left'
        Button:
            text: '11'
            on_release:
                root.manager.current = 'Screen11'
                root.manager.transition.direction = 'left'
        Button:
            text: '10'
            on_release:
                root.manager.current = 'Screen10'
                root.manager.transition.direction = 'left'
        Button:
            text: '58'
            on_release:
                root.manager.current = 'Screen58'
                root.manager.transition.direction = 'left'
        Button:
            text: '38'
            on_release:
                root.manager.current = 'Screen38'
                root.manager.transition.direction = 'left'
        Button:
            text: '54'
            on_release:
                root.manager.current = 'Screen54'
                root.manager.transition.direction = 'left'
        Button:
            text: '61'
            on_release:
                root.manager.current = 'Screen61'
                root.manager.transition.direction = 'left'
        Button:
            text: '60'
            on_release:
                root.manager.current = 'Screen60'
                root.manager.transition.direction = 'left'
        Button:
            text: '41'
            on_release:
                root.manager.current = 'Screen41'
                root.manager.transition.direction = 'left'
        Button:
            text: '19'
            on_release:
                root.manager.current = 'Screen19'
                root.manager.transition.direction = 'left'
        Button:
            text: '13'
            on_release:
                root.manager.current = 'Screen13'
                root.manager.transition.direction = 'left'
        Button:
            text: '49'
            on_release:
                root.manager.current = 'Screen49'
                root.manager.transition.direction = 'left'
        Button:
            text: '30'
            on_release:
                root.manager.current = 'Screen30'
                root.manager.transition.direction = 'left'
        Button:
            text: '55'
            on_release:
                root.manager.current = 'Screen55'
                root.manager.transition.direction = 'left'
        Button:
            text: '37'
            on_release:
                root.manager.current = 'Screen37'
                root.manager.transition.direction = 'left'
        Button:
            text: '63'
            on_release:
                root.manager.current = 'Screen63'
                root.manager.transition.direction = 'left'
        Button:
            text: '22'
            on_release:
                root.manager.current = 'Screen22'
                root.manager.transition.direction = 'left'
        Button:
            text: '36'
            on_release:
                root.manager.current = 'Screen36'
                root.manager.transition.direction = 'left'
        Button:
            text: '25'
            on_release:
                root.manager.current = 'Screen25'
                root.manager.transition.direction = 'left'
        Button:
            text: '17'
            on_release:
                root.manager.current = 'Screen17'
                root.manager.transition.direction = 'left'
        Button:
            text: '21'
            on_release:
                root.manager.current = 'Screen21'
                root.manager.transition.direction = 'left'
        Button:
            text: '51'
            on_release:
                root.manager.current = 'Screen51'
                root.manager.transition.direction = 'left'
        Button:
            text: '42'
            on_release:
                root.manager.current = 'Screen42'
                root.manager.transition.direction = 'left'
        Button:
            text: '3'
            on_release:
                root.manager.current = 'Screen3'
                root.manager.transition.direction = 'left'
        Button:
            text: '27'
            on_release:
                root.manager.current = 'Screen27'
                root.manager.transition.direction = 'left'
        Button:
            text: '24'
            on_release:
                root.manager.current = 'Screen24'
                root.manager.transition.direction = 'left'
        Button:
            text: '44'
            on_release:
                root.manager.current = 'Screen44'
                root.manager.transition.direction = 'left'
        Button:
            text: '28'
            on_release:
                root.manager.current = 'Screen28'
                root.manager.transition.direction = 'left'
        Button:
            text: '50'
            on_release:
                root.manager.current = 'Screen50'
                root.manager.transition.direction = 'left'
        Button:
            text: '32'
            on_release:
                root.manager.current = 'Screen32'
                root.manager.transition.direction = 'left'
        Button:
            text: '57'
            on_release:
                root.manager.current = 'Screen57'
                root.manager.transition.direction = 'left'
        Button:
            text: '48'
            on_release:
                root.manager.current = 'Screen48'
                root.manager.transition.direction = 'left'
        Button:
            text: '18'
            on_release:
                root.manager.current = 'Screen18'
                root.manager.transition.direction = 'left'
        Button:
            text: '46'
            on_release:
                root.manager.current = 'Screen46'
                root.manager.transition.direction = 'left'
        Button:
            text: '6'
            on_release:
                root.manager.current = 'Screen6'
                root.manager.transition.direction = 'left'
        Button:
            text: '47'
            on_release:
                root.manager.current = 'Screen47'
                root.manager.transition.direction = 'left'
        Button:
            text: '64'
            on_release:
                root.manager.current = 'Screen64'
                root.manager.transition.direction = 'left'
        Button:
            text: '40'
            on_release:
                root.manager.current = 'Screen40'
                root.manager.transition.direction = 'left'
        Button:
            text: '59'
            on_release:
                root.manager.current = 'Screen59'
                root.manager.transition.direction = 'left'
        Button:
            text: '29'
            on_release:
                root.manager.current = 'Screen29'
                root.manager.transition.direction = 'left'
        Button:
            text: '4'
            on_release:
                root.manager.current = 'Screen4'
                root.manager.transition.direction = 'left'
        Button:
            text: '7'
            on_release:
                root.manager.current = 'Screen7'
                root.manager.transition.direction = 'left'
        Button:
            text: '33'
            on_release:
                root.manager.current = 'Screen33'
                root.manager.transition.direction = 'left'
        Button:
            text: '31'
            on_release:
                root.manager.current = 'Screen31'
                root.manager.transition.direction = 'left'
        Button:
            text: '56'
            on_release:
                root.manager.current = 'Screen56'
                root.manager.transition.direction = 'left'
        Button:
            text: '62'
            on_release:
                root.manager.current = 'Screen62'
                root.manager.transition.direction = 'left'
        Button:
            text: '53'
            on_release:
                root.manager.current = 'Screen53'
                root.manager.transition.direction = 'left'
        Button:
            text: '39'
            on_release:
                root.manager.current = 'Screen39'
                root.manager.transition.direction = 'left'
        Button:
            text: '52'
            on_release:
                root.manager.current = 'Screen52'
                root.manager.transition.direction = 'left'
        Button:
            text: '15'
            on_release:
                root.manager.current = 'Screen15'
                root.manager.transition.direction = 'left'
        Button:
            text: '12'
            on_release:
                root.manager.current = 'Screen12'
                root.manager.transition.direction = 'left'
        Button:
            text: '45'
            on_release:
                root.manager.current = 'Screen45'
                root.manager.transition.direction = 'left'
        Button:
            text: '35'
            on_release:
                root.manager.current = 'Screen35'
                root.manager.transition.direction = 'left'
        Button:
            text: '16'
            on_release:
                root.manager.current = 'Screen16'
                root.manager.transition.direction = 'left'
        Button:
            text: '20'
            on_release:
                root.manager.current = 'Screen20'
                root.manager.transition.direction = 'left'
        Button:
            text: '8'
            on_release:
                root.manager.current = 'Screen8'
                root.manager.transition.direction = 'left'
        Button:
            text: '23'
            on_release:
                root.manager.current = 'Screen23'
                root.manager.transition.direction = 'left'
        Button:
            text: '2'
            on_release:
                root.manager.current = 'Screen2'
                root.manager.transition.direction = 'left'
        
        MyButton:  
            text: '三枚'
            on_release:
                root.manager.current = 'Screensanmei'
                root.manager.transition.direction = 'left'
            
        MyButton:
            text: '六枚'
            on_release:
                root.manager.current = 'Screenliumei'
                root.manager.transition.direction = 'left'
            
        MyButton:
            text: '三数'
            on_release:
                root.manager.current = 'Screensanshu'
                root.manager.transition.direction = 'left'
            
        MyButton:
            text: '揲蓍'
            on_release:
                root.manager.current = 'Screensheshi'
                root.manager.transition.direction = 'left'
        MyButton:
            text: '抽签'
            on_release:
                root.manager.current = 'Screenchouqian'
                root.manager.transition.direction = 'left'
            
        MyButton:
            text: ''
            
        MyButton:
            text: '学习'
            color: 0,1,1,1
            
        MyButton:
            text: '退出'
            color: 1,0,0,1
            on_press: app.stop() 
<Screen1>:
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'四月\\n立夏\\n蛇'
                font_name: './yahei.ttf'
                markup: True
            MyButton:
                text: '乾'
                font_size: 60           
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            MyButton:
                text: '困龙得水好运交\\n不由喜气上眉梢\\n一切谋望皆如意\\n向后时运渐渐高'
                
        BoxLayout:
            
            Image:
                id: 1
                source: '1.png'
                allow_stretch: False
            Label:
                text: '乾元亨利贞\\n\\n用九见群龙无首吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40
            BoxLayout:
                orientation: 'vertical'
                
                Label:
                    text: '上九亢龙有悔'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五飞龙在天利见大人'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四或跃在渊无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三君子终日乾乾夕惕若厉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二见龙在田利见大人'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九潜龙勿用'
                    font_name: './yahei.ttf'
        
<Screen43>:
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'三月\\n清明\\n龙'
                font_name: './yahei.ttf'
                markup: True
                
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '夬'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '蜘蛛脱网赛天军\\n粘住游蜂翅翎毛\\n幸有大风吹破网\\n脱离灾难又逍遥'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 43
                source: '43.png'
                allow_stretch: False
            Label:
                text: '夬揚于王庭孚號有厲告自邑不利即戎利有攸往'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六无号终有凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五苋陆夬夬中行无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四臀无肤其行次且牵羊悔亡闻言不信'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三壮于頄有凶君子夬夬独行遇雨若濡有愠无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二惕号莫夜有戎勿恤'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九壮于前趾往不胜为咎'
                    font_name: './yahei.ttf'
<Screen14>:
    name: '14'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''#[b]00[/b]:00:00
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '大有'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '砍树摸雀作事牢\\n是非口舌自然消\\n婚姻合伙来费力\\n若问走失未逃脱'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 14
                source: '14.png'
                allow_stretch: False
            Label:
                text: '大有元亨'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九自天祐之吉无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五厥孚交如威如吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四匪其彭无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三公用亨于天子小人弗克'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二大車以載有攸往无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九无交害匪咎艱則无咎'
                    font_name: './yahei.ttf'
<Screen34>:
    name: '34'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'二月\\n惊蛰\\n兔'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '大壮'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '卦占工师得大木\\n眼前该着走上路\\n时来运转多顺当\\n有事自管放心宽'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 34
                source: '34.png'
                allow_stretch: False
            Label:
                text: '大壮利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六羝羊触藩不能退不能遂无攸利艰则吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五丧羊于易无悔'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四贞吉悔亡藩决不羸壮于大舆之輹'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三小人用壮君子用罔贞厉羝羊触藩羸其角'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九壮于趾征凶有孚'
                    font_name: './yahei.ttf'
<Screen9>:
    name: '9'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '小畜'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '苗逢旱天尽焦梢\\n水想云浓雨不浇\\n农人仰面长吁气\\n是从款来莫心高'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 9
                source: '9.png'
                allow_stretch: False
            Label:
                text: '小畜亨密云不雨自我西郊'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九既雨既处尚德载妇贞厉月几望君子征凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五有孚挛如富以其邻'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四有孚血去惕出无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三舆说辐夫妻反目'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二牵复吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九复自道何其咎吉'
                    font_name: './yahei.ttf'
<Screen5>:
    name: '5'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '需'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '明珠土埋日久深\\n无光无亮到如今\\n忽然大风吹土去\\n自然显露有重新'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 5
                source: '5.png'
                allow_stretch: False
            Label:
                text: '需有孚光亨贞吉利涉大川'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六入于穴有不速之客三人来敬之终吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五需于酒食贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四需于血出自穴'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三需于泥致寇至'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二需于沙小有言终吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九需于郊利用恒无咎'
                    font_name: './yahei.ttf'
<Screen26>:
    name: '26'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '大畜'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '忧愁常锁两眉头\\n千头万绪挂心间\\n从今以后防开阵\\n任意行而不相干'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 26
                source: '26.png'
                allow_stretch: False
            Label:
                text: '大畜利贞不家食吉利涉大川'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九何天之衢亨'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五豮豕之牙吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四童牛之牿元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三良马逐利艰贞曰闲舆卫利有攸往'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二舆说輹'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九有厉利已'
                    font_name: './yahei.ttf'
<Screen11>:
    name: '11'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'正月\\n立春\\n虎'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '泰'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '学文满腹入场闱\\n三元及第得意回\\n从今解去愁和闷\\n喜庆平地一声雷'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 11
                source: '11.png'
                allow_stretch: False
            Label:
                text: '泰小往大来吉亨'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六城复于隍勿用师自邑告命贞吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五帝乙归妹以祉元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四翩翩不富以其邻不戒以孚'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三无平不陂无往不复艰贞无咎勿恤其孚于食有福'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二包荒用冯河不遐遗朋亡得尚于中行'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九拔茅茹以其汇征吉'
                    font_name: './yahei.ttf'
<Screen10>:
    name: '10'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '履'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '凤凰落在西歧山\\n去鸣几声出圣贤\\n天降文王开基业\\n富贵荣华八百年'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 10
                source: '10.png'
                allow_stretch: False
            Label:
                text: '履虎尾不咥人亨'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40
                           
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九视履考祥其旋元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五夬履贞厉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四履虎尾愬愬终吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三眇能视跛能履履虎尾咥人凶武人为于大君'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二履道坦坦幽人贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九素履往无咎'
                    font_name: './yahei.ttf'
<Screen58>:
    name: '58'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '兑'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '这个卦象真可取\\n觉着做事不费力\\n休要错过这机关\\n事事觉得随心意'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 58
                source: '58.png'
                allow_stretch: False
            Label:
                text: '兑亨利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六引兑'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五孚于剥有厉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四商兑未宁介疾有喜'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三来兑凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二孚兑吉悔亡'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九和兑吉'
                    font_name: './yahei.ttf'
<Screen38>:
    name: '38'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '睽'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '此卦占来运气歹\\n如同太公作买卖\\n贩猪牛快贩羊迟\\n猪羊齐贩断了宰'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 38
                source: '38.png'
                allow_stretch: False
            Label:
                text: '睽小事吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九睽孤见豕负涂载鬼一车先张之弧后说之弧匪寇婚媾往遇雨则吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五悔亡厥宗噬肤往何咎斋'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四睽孤遇元夫交孚厉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三见舆曳其牛掣其人天且劓无初有终'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二遇主于巷无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九悔亡丧马勿逐自复见恶人无咎'
                    font_name: './yahei.ttf'
<Screen54>:
    name: '54'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '归妹'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '求鱼须当向水中\\n树上求之不顺情\\n受尽爬揭难随意\\n劳而无功运平平'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 54
                source: '54.png'
                allow_stretch: False
            Label:
                text: '归妹征凶无攸利'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六女承筐无实士刲羊无血无攸利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五帝乙归妹其君之袂不如其娣之袂良月几望吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四归妹愆期迟归有时'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三归妹以须反归以娣'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二眇能视利幽人之贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九归妹以娣跛能履征吉'
                    font_name: './yahei.ttf'
<Screen61>:
    name: '61'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '中孚'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '路上行人色匆匆\\n急忙无桥过薄冰\\n小心谨慎过得去\\n一步错了落水中'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 61
                source: '61.png'
                allow_stretch: False
            Label:
                text: '中孚豚鱼吉利涉大川利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九翰音登于天贞凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五有孚挛如无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四月几望马匹亡无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三得敌或鼓或罢或泣或歌'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二鸣鹤在阴其子和之我有好爵吾与尔靡之'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九虞吉有它不燕'
                    font_name: './yahei.ttf'
<Screen60>:
    name: '60'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '节'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '时来运转喜气生\\n登台封神姜太公\\n到此诸神皆退位\\n纵然有祸不成凶'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 60
                source: '60.png'
                allow_stretch: False
            Label:
                text: '节亨苦节不可贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六苦节贞凶悔亡'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五甘节吉往有尚'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四安节亨'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三不节若则嗟若无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二不出门庭凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九不出户庭无咎'
                    font_name: './yahei.ttf'
<Screen41>:
    name: '41'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '损'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '时动不至费心多\\n比作推车受折磨\\n山路崎岖吊下耳\\n做插右按按不着'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 41
                source: '41.png'
                allow_stretch: False
            Label:
                text: '损有孚元吉无咎'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九弗损益之无咎贞吉利有攸往得臣无家'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五或益之十朋之龟弗克违元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四损其疾使遄有喜无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三三人行则损一人一人行则得其友'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二利贞征凶弗损益之'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九已事遄往无咎酌损之'
                    font_name: './yahei.ttf'
<Screen19>:
    name: '19'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'十二月\\n小寒\\n牛'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '临'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '君王无道民倒悬\\n常想拨云见青天\\n幸逢明主施仁政\\n重又安居乐自然'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 19
                source: '19.png'
                allow_stretch: False
            Label:
                text: '临元亨利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六敦临吉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五知临大君之宜吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四至临无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三甘临无攸利既忧之无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二咸临吉无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九咸临贞吉'
                    font_name: './yahei.ttf'
<Screen13>:
    name: '13'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '同人'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '心中有事犯猜疑\\n谋望从前不着实\\n幸遇明人来指引\\n诸般忧闷自消之'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 13
                source: '13.png'
                allow_stretch: False
            Label:
                text: '同人于野亨利涉大川利君子贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九同人于郊无悔'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五同人先号咷而后笑大师克相遇'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四乘其墉弗克攻吉主'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三伏戎于莽升其高陵三岁不兴'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二同人于宗吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九同人于门无咎'
                    font_name: './yahei.ttf'
<Screen49>:
    name: '49'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '革'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '苗逢旱天渐渐衰\\n幸得天恩降雨来\\n忧去喜来能变化\\n求谋干事遂心怀'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 49
                source: '49.png'
                allow_stretch: False
            Label:
                text: '革已日乃孚元亨利贞悔亡'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六君子豹变小人革面征凶居贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五大人虎变未占有孚'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四悔亡有孚改命吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三征凶贞厉革言三就有孚'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二巳日乃革之征吉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九巩用黄牛之革'
                    font_name: './yahei.ttf'
<Screen30>:
    name: '30'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '离'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '官人来占主高升\\n庄农人家产业增\\n生意买卖利息厚\\n匠艺占之大亨通'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 30
                source: '30.png'
                allow_stretch: False
            Label:
                text: '离利贞亨畜牝牛吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九王用出征有嘉折首获匪其丑无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五出涕沱若戚嗟若吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四突如其来如焚如死如弃如'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三日昃之离不鼓缶而歌则大耋之嗟凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二黄离元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九履错然敬之无咎'
                    font_name: './yahei.ttf'
<Screen55>:
    name: '55'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '丰'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '古镜昏暗好几年\\n一朝磨明似月圆\\n君子谋事逢此卦\\n近来运转喜自然'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 55
                source: '55.png'
                allow_stretch: False
            Label:
                text: '丰亨王假之勿忧宜日中'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六丰其屋蔀其家窥其户阒其无人三岁不觌凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五来章有庆誉吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四丰其蔀日中见斗遇其夷主吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三丰其沛日中见沫折其右肱无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二丰其蔀日中见斗往得疑疾有孚发若吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九遇其配主虽旬无咎往有尚'
                    font_name: './yahei.ttf'
<Screen37>:
    name: '37'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '家人'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '一朵鲜花镜中开\\n看着极好取不来\\n劝君休把镜花恋\\n卦若逢之主可怪'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 37
                source: '37.png'
                allow_stretch: False
            Label:
                text: '家人利女贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九有孚威如终吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五王假有家勿恤吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四富家大吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三家人嗃嗃悔厉吉妇子嘻嘻终吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二无攸遂在中馈贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九闲有家悔亡'
                    font_name: './yahei.ttf'
<Screen63>:
    name: '63'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '既济'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '金榜以上题姓名\\n不负当年苦用功\\n人逢此卦名吉庆\\n一切谋望大亨通'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 63
                source: '63.png'
                allow_stretch: False
            Label:
                text: '既济亨小利贞初吉终乱'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六濡其首厉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五东邻杀牛不如西邻之禴祭实受其福'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四繻有衣袽终日戒'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三高宗伐鬼方三年克之小人勿用'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二妇丧其茀勿逐七日得'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九曳其轮濡其尾无咎'
                    font_name: './yahei.ttf'
<Screen22>:
    name: '22'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '贲'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '近来运转锐气周\\n窈窕淑女君子求\\n钟鼓乐之大吉庆\\n占者逢之喜临头'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 22
                source: '22.png'
                allow_stretch: False
            Label:
                text: '贲亨小利有攸往'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九白贲无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五贲于丘园束帛戋戋吝终吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四贲如皤如白马翰如匪寇婚媾'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三贲如濡如永贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二贲其须'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九贲其趾舍车而徒'
                    font_name: './yahei.ttf'
<Screen36>:
    name: '36'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '明夷'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '时乖运拙走不着\\n急忙过河拆了桥\\n恩人无义反为怨\\n凡事无功枉受劳'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 36
                source: '36.png'
                allow_stretch: False
            Label:
                text: '明夷利艰贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六不明晦初登于天后入于地'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五箕子之明夷利贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四入于左腹获明夷之心于出门庭'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三明夷于南狩得其大首不可疾贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二明夷夷于左股用拯马壮吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九明夷于飞垂其翼君子于行三日不食有攸往主人有言'
                    font_name: './yahei.ttf'
<Screen25>:
    name: '25'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '无妄'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '飞鸟失机落笼中\\n纵然奋飞不能腾\\n目下只宜守本分\\n妄想扒高万不能'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 25
                source: '25.png'
                allow_stretch: False
            Label:
                text: '无妄元亨利贞其匪正有眚不利有攸往'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九无妄行有眚无攸利'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五无妄之疾勿药有喜'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四可贞无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三无妄之灾或系之牛行人之得邑人之灾'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二不耕获不菑畬则利用攸往'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九无妄往吉'
                    font_name: './yahei.ttf'
<Screen17>:
    name: '17'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '随'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '泥里步踏这几年\\n推车靠崖在眼前\\n目下就该再使力\\n扒上崖去发财源'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 17
                source: '17.png'
                allow_stretch: False
            Label:
                text: '随元亨利贞无咎'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六拘系之乃従维之王用亨于西山'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五孚于嘉吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四随有获贞凶有孚在道以明何咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三系丈夫失小子随有求得利居贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二系小子失丈夫'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九官有渝贞吉出门交有功'
                    font_name: './yahei.ttf'
<Screen21>:
    name: '21'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '噬嗑'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '运拙如同身受饥\\n幸得送饭又送食\\n适口充腹心欢喜\\n忧愁从此渐消移'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 21
                source: '21.png'
                allow_stretch: False
            Label:
                text: '噬嗑亨利用狱'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九何校灭耳凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五噬干肉得黄金贞厉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四噬干胏得金矢利艰贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三噬腊肉遇毒小吝无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二噬肤灭鼻无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九屦校灭趾无咎'
                    font_name: './yahei.ttf'
<Screen51>:
    name: '51'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '震'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '一口金钟在淤泥\\n人人拿着当玩石\\n忽然一日钟悬起\\n响亮一声天下知'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 51
                source: '51.png'
                allow_stretch: False
            Label:
                text: '震亨震来虩虩笑言哑哑震惊百里不丧匕鬯'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六震索索视矍矍征凶震不于其躬于其邻无咎婚媾有言'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五震往来厉意无丧有事'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四震遂泥'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三震苏苏震行无眚'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二震来厉亿丧贝跻于九陵勿逐七日得'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九震来虩虩后笑言哑哑吉'
                    font_name: './yahei.ttf'
<Screen42>:
    name: '42'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '益'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '时来运转吉气发\\n多年枯木又开花\\n枝叶重生多茂盛\\n几人见了几人夸'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 42
                source: '42.png'
                allow_stretch: False
            Label:
                text: '益利有攸往利涉大川'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九莫益之或击之立心勿恒凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五有孚惠心勿问元吉有孚惠我德'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四中行告公従利用为依迁国'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三益之用凶事无咎有孚中行告公用圭'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二或益之十朋之龟弗克违永贞吉王用享于帝吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九利用为大作元吉无咎'
                    font_name: './yahei.ttf'
<Screen3>:
    name: '3'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '屯'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '风刮乱丝不见头\\n颠三倒四犯忧愁\\n慢从款来左顺遂\\n急促反惹不自由'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 3
                source: '3.png'
                allow_stretch: False
            Label:
                text: '屯元亨利贞勿用有攸往利建侯'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六乘马班如泣血涟如'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五屯其膏小贞吉大贞凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四乘马班如求婚媾往吉无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三即鹿无虞惟入于林中君子几不如舍往吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二屯如邅如乘马班如匪寇婚媾女子贞不字十年乃字'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九磐桓利居贞利建侯'
                    font_name: './yahei.ttf'
<Screen27>:
    name: '27'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '颐'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '太公独钓渭水河\\n手执丝杆忧愁多\\n时来又遇文王访\\n自此永不受折磨'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 27
                source: '27.png'
                allow_stretch: False
            Label:
                text: '颐贞吉观颐自求口实'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九由颐厉吉利涉大川'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五拂经居贞吉不可涉大川'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四颠颐吉虎视眈眈，其欲逐逐，无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三拂颐贞凶十年勿用无攸利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二颠颐拂经于丘颐征凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九舍尔灵龟观我朵颐凶'
                    font_name: './yahei.ttf'
<Screen24>:
    name: '24'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'十一月\\n大雪\\n鼠'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '复'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '马氏太公不相合\\n世人占之忧疑多\\n恩人无义反为怨\\n是非平地起风波'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 24
                source: '24.png'
                allow_stretch: False
            Label:
                text: '复亨出入无疾朋来无咎反复其道七日来复利有攸往'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 140, 10
                        pos: 140, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六迷复凶有灾眚用行师终有大败以其国君凶至于十年不克征'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五敦复无悔'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四中行独复'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三频复厉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二休复吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初九不远复无祗悔元吉'
                    font_name: './yahei.ttf'
<Screen44>:
    name: '44'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'五月\\n芒种\\n马'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '姤'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '他乡遇友喜气欢\\n须知运气福重添\\n自今交了顺当运\\n向后管保不相干'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 44
                source: '44.png'
                allow_stretch: False
            Label:
                text: '姤女壮勿用取女'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九姤其角吝无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五以杞包瓜含章有陨自天'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四包无鱼起凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三臀无肤其行次且厉无大咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二包有鱼无咎不利宾'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六系于金柅贞吉有攸往见凶羸豕孚蹢躅'
                    font_name: './yahei.ttf'
<Screen28>:
    name: '28'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '大过'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '夜晚梦里梦金银\\n醒来仍不见一文\\n目下只宜求本分\\n思想络是空劳神'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 28
                source: '28.png'
                allow_stretch: False
            Label:
                text: '大过栋挠利有攸往亨'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六过涉灭顶凶无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五枯杨生华老妇得其士夫无咎无誉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四栋隆吉有它吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三栋桡凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二枯杨生稊老夫得其女妻无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六藉用白茅无咎'
                    font_name: './yahei.ttf'
<Screen50>:
    name: '50'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '鼎'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '莺鹜蛤蜊落沙滩\\n蛤蜊莺鹜两翅扇\\n渔人进前双得利\\n失走行人却自在'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 50
                source: '50.png'
                allow_stretch: False
            Label:
                text: '鼎元吉亨'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九鼎玉铉大吉无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五鼎黄耳金铉利贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四鼎折足覆公餗其形渥凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三鼎耳革其行塞雉膏不食方雨亏悔终吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二鼎有实我仇有疾不我能即吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六鼎颠趾利出否得妾以其子无咎'
                    font_name: './yahei.ttf'
<Screen32>:
    name: '32'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '恒'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '鱼翁寻鱼运气好\\n鱼来撞网跑不了\\n别人使本挣不来\\n谁想一到就凑和'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 32
                source: '32.png'
                allow_stretch: False
            Label:
                text: '恒亨无咎利贞利有攸往'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六振恒凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五恒其德贞妇人吉夫子凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四田无禽'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三不恒其德或承之羞贞吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二悔亡'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六浚恒贞凶无攸利'
                    font_name: './yahei.ttf'
<Screen57>:
    name: '57'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '巽'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '一叶孤舟落沙滩\\n有篙无水进退难\\n时逢大雨江湖溢\\n不用费力任往返'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 57
                source: '57.png'
                allow_stretch: False
            Label:
                text: '巽小亨利有攸往利见大人'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九巽在床下丧其资斧贞凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五贞吉悔亡无不利无初有终先庚三日后庚三日吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四悔亡田获三品'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三频巽吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二巽在床下用史巫纷若吉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六进退利武人之贞'
                    font_name: './yahei.ttf'
<Screen48>:
    name: '48'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '井'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '枯井破费已多年\\n一朝流泉出来鲜\\n资生济渴人称羡\\n时来运转喜自然'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 48
                source: '48.png'
                allow_stretch: False
            Label:
                text: '井改邑不改井无丧无得往来井井汔至亦未繘井羸其瓶凶'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六井收勿幕有孚元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五井洌寒泉食'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四井甃无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三井渫不食为我心恻可用汲王明并受其福'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二井谷射鲋瓮敝漏'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六井泥不食旧井无禽'
                    font_name: './yahei.ttf'
<Screen18>:
    name: '18'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '蛊'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '卦中爻象如推磨\\n顺当为福反为祸\\n心中有益且迟迟\\n凡事尽从忙处错'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 18
                source: '18.png'
                allow_stretch: False
            Label:
                text: '蛊元亨利涉大川先甲三日后甲三日'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九不事王侯高尚其事'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五干父之蛊用誉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四裕父之蛊往见吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三干父之蛊小有悔无大咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二干母之蛊不可贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六干父之蛊有子考无咎厉终吉'
                    font_name: './yahei.ttf'
<Screen46>:
    name: '46'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '升'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '士人来占必得名\\n生意买卖也兴隆\\n匠艺逢之交易好\\n农间庄稼亦收成'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 46
                source: '46.png'
                allow_stretch: False
            Label:
                text: '升元亨用见大人勿恤南征吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六冥升利于不息之贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五贞吉升阶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四王用亨于岐山吉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三升虚邑'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二孚乃利用禴无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六允升大吉'
                    font_name: './yahei.ttf'
<Screen6>:
    name: '6'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '讼'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '心中有事事难做\\n恰是二人争路走\\n雨下俱是要占先\\n谁肯让谁走一步'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 6
                source: '6.png'
                allow_stretch: False
            Label:
                text: '讼有孚窒惕中吉终凶利见大人不利涉大川'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九或锡之鞶带终朝三褫之'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五讼元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四不克讼复既命渝安贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三食旧德贞厉终吉或従王事无成'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二不克讼归而逋其邑人三百户无眚'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六不永所事小有言终吉'
                    font_name: './yahei.ttf'
<Screen47>:
    name: '47'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '困'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '时运不来好伤怀\\n撮上押去把梯抬\\n一筒虫翼无到手\\n转了上去下不来'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 47
                source: '47.png'
                allow_stretch: False
            Label:
                text: '困亨贞大人吉无咎有言不信'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六困于葛藟于臲臬兀曰动悔有悔征吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五劓刖困于赤绂乃徐有说利用祭祀'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四来徐徐困于金车吝有终'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三困于石据于蒺藜入于其宫不见其妻凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二困于酒食朱绂方来利用享祀征凶无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六臀困于株木入于幽谷三岁不觌'
                    font_name: './yahei.ttf'
<Screen64>:
    name: '64'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '未济'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '离地着人几丈深\\n是防偷营劫寨人\\n后封太岁为凶煞\\n时加谨慎祸不侵'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 64
                source: '64.png'
                allow_stretch: False
            Label:
                text: '未济亨小狐汔济濡其尾无攸利'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九有孚于饮酒无咎濡其首有孚失是'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五贞吉无悔君子之光有孚吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四贞吉悔亡震用伐鬼方三年有赏于大国'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三未济征凶利涉大川'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二曳其轮贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六濡其尾吝'
                    font_name: './yahei.ttf'
<Screen40>:
    name: '40'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '解'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '目下月令如过关\\n千辛万苦受熬煎\\n时来恰相有人救\\n任意所为不相干'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 40
                source: '40.png'
                allow_stretch: False
            Label:
                text: '解利西南无所往其来复吉有攸往夙吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六公用射隼于高墉之上获之无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五君子维有解吉有孚于小人'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四解而拇朋至斯孚'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三负且乘致寇至贞吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二田获三狐得黄矢贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六无咎'
                    font_name: './yahei.ttf'
<Screen59>:
    name: '59'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '涣'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '隔河望见一锭金\\n欲取岸宽水又深\\n指望资财难到手\\n尽夜资财枉费心'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 59
                source: '59.png'
                allow_stretch: False
            Label:
                text: '涣亨王假有庙利涉大川利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九涣其血去逖出无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五涣汗其大号涣王居无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四涣其群元吉涣有丘匪夷所思'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三涣其躬无悔'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二涣奔其机悔亡'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六用拯马壮吉'
                    font_name: './yahei.ttf'
<Screen29>:
    name: '29'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '坎'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '一轮明月照水中\\n只见影儿不见踪\\n愚夫当财下去取\\n摸来摸去一场空'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 29
                source: '29.png'
                allow_stretch: False
            Label:
                text: '习坎有孚维心亨行有尚'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40     
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六系用徽纆窴于丛棘三岁不得凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五坎不盈祗既平无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四樽酒簋贰用缶纳约自牖终无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三来之坎坎险且枕入于坎窞勿用'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二坎有险求小得'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六习坎入于坎窞凶'
                    font_name: './yahei.ttf'
<Screen4>:
    name: '4'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '蒙'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '卦中爻象犯小耗\\n君子占之运不高\\n婚姻合伙有琐碎\\n做事必然受苦劳'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 4
                source: '4.png'
                allow_stretch: False
            Label:
                text: '蒙亨匪我求童蒙童蒙求我初筮告再三渎渎则不告利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40     
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九击蒙不利为寇利御寇'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五童蒙吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四困蒙吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三勿用取女见金夫不有躬无攸利'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二包蒙吉纳妇吉子克家'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六发蒙利用刑人用说桎梏以往吝'
                    font_name: './yahei.ttf'
<Screen7>:
    name: '7'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '师'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '将帅领旨去出征\\n骑着烈马拉硬弓\\n百步穿杨去得准\\n箭中金钱喜气生'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 7
                source: '7.png'
                allow_stretch: False
            Label:
                text: '师贞丈人吉无咎'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 140, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六大君有命开国承家小人勿用'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五田有禽利执言无咎长子帅师弟子舆尸贞凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四师左次无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三师或舆尸凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九二在师中吉无咎王三锡命'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六师出以律否臧凶'
                    font_name: './yahei.ttf'
<Screen33>:
    name: '33'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'六月\\n小暑\\n羊'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '遁'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '浓云蔽日不光明\\n劝君且莫出远行\\n婚姻求财皆不利\\n提防口舌到门庭'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 33
                source: '33.png'
                allow_stretch: False
            Label:
                text: '遁亨小利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40   
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九肥遁无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五嘉遁贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四好遁君子吉小人否'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三系遁有疾厉畜臣妾吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二执之用黄牛之革莫之胜说'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六遁尾厉勿用有攸往'
                    font_name: './yahei.ttf'
<Screen31>:
    name: '31'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '咸'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '运去黄金失色\\n时来棒槌发芽\\n月令极好无差\\n且喜心宽意大'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 31
                source: '31.png'
                allow_stretch: False
            Label:
                text: '咸亨利贞取女吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六咸其辅颊舌'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五咸其脢无悔'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四贞吉悔亡憧憧往来朋従尔思'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三咸其股执其随往吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二咸其腓凶居吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六咸其拇'
                    font_name: './yahei.ttf'
<Screen56>:
    name: '56'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '旅'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '飞鸟树上垒窝巢\\n小人使计举火烧\\n君占此卦为不吉\\n一切谋望枉徒劳'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 56
                source: '56.png'
                allow_stretch: False
            Label:
                text: '旅小亨旅贞吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九鸟焚其巢旅人先笑后号咷丧牛于易凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五射雉一矢亡终以誉命'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四旅于处得其资斧我心不快'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三旅焚其次丧其童仆贞厉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二旅即次怀其资得童仆贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六旅琐琐斯其所取灾'
                    font_name: './yahei.ttf'
<Screen62>:
    name: '62'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '小过'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '行人路过独木桥\\n心内惶恐眼里瞧\\n爽利保保过得去\\n慢行一定不安牢'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 62
                source: '62.png'
                allow_stretch: False
            Label:
                text: '小过亨利贞可小事不可大事飞鸟遗之音不宜上宜下大吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六弗遇过之飞鸟离之凶是谓灾眚'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五密云不雨自我西郊公弋取彼在穴'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四无咎弗过遇之往厉必戒勿用永贞'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三弗过防之従或戕之凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二过其祖遇其妣不及其君遇其臣无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六飞鸟以凶'
                    font_name: './yahei.ttf'
<Screen53>:
    name: '53'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '渐'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '俊鸟幸得出笼中\\n脱离灾难显威风\\n一朝得意福力至\\n东西南北任意行'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 53
                source: '53.png'
                allow_stretch: False
            Label:
                text: '渐女归吉利贞'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九鸿渐于陆其羽可用为仪吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五鸿渐于陵妇三岁不孕终莫之胜吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四鸿渐于木或得其桷无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三鸿渐于陆夫征不复妇孕不育凶利御寇'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二鸿渐于磐饮食衎衎吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六鸿渐于干小子厉有言无咎'
                    font_name: './yahei.ttf'
<Screen39>:
    name: '39'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '蹇'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '大雨倾地雪满天\\n路上行人苦又寒\\n拖泥带水费尽力\\n事不遂心且耐烦'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 39
                source: '39.png'
                allow_stretch: False
            Label:
                text: '蹇利西南不利东北利见大人贞吉'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六往蹇来硕吉利见大人'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五大蹇朋来'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四往蹇来连'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三往蹇来反'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二王臣蹇蹇匪躬之故'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六往蹇来誉'
                    font_name: './yahei.ttf'
<Screen52>:
    name: '52'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '艮'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '财帛常打心头走\\n可惜眼前难到手\\n不如意时且忍耐\\n逢着闲事休开口'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 52
                source: '52.png'
                allow_stretch: False
            Label:
                text: '艮其背不获其身行其庭不见其人无咎'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九敦艮吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五艮其辅言有序悔亡'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四艮其身无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三艮其限列其夤厉熏心'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二艮其腓不拯其随其心不快'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六艮其趾无咎利永贞'
                    font_name: './yahei.ttf'
<Screen15>:
    name: '15'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:''
                font_name: './yahei.ttf'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '谦'
                font_size: 60
                font_name: './yahei.ttf'
            
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '天赐贫人一封金\\n不争不抢两平分\\n彼此分得金到手\\n一切谋望皆遂心'
                font_name: './yahei.ttf'
                
        BoxLayout:
            
            Image:
                id: 15
                source: '15.png'
                allow_stretch: False
            Label:
                text: '谦亨君子有终'
                font_name: './yahei.ttf'
        BoxLayout:
            
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 140, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40    
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六鸣谦利用行师征邑国'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五不富以其邻利用侵伐无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四无不利捴谦'
                    font_name: './yahei.ttf'
                Label:
                    text: '九三劳谦君子有终吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二鸣谦贞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六谦谦君子用涉大川吉'
                    font_name: './yahei.ttf'
<Screen12>:
    name: '12'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'七月\\n立秋\\n猴' 
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '否'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '虎落陷坑不堪言\\n进前容易退后难\\n谋望不遂自己便\\n疾病口舌事牵连'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 12
                source: '12.png'
                allow_stretch: False
            Label:
                text: '否之匪人不利君子貞大往小來'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九傾否先否後喜'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五休否大人吉其亡其亡繫于苞桑'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四有命无咎疇離祉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三包羞'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二包承小人吉大人否亨'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六拔茅茹以其彙貞吉亨'
                    font_name: './yahei.ttf'
<Screen45>:
    name: '45'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text: ''
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '萃'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '游鱼戏水被网惊\\n跳过龙门身化龙\\n三尺杨柳垂金钱\\n万朵桃花显你能'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 45
                source: '45.png'
                allow_stretch: False
            Label:
                text: '萃亨王假有廟利見大人亨利貞用大牲吉利有攸往'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六齎咨涕洟无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五萃有位无咎匪孚元永貞悔亡'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四大吉无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三萃如嗟如无攸利往无咎小吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二引吉无咎孚乃利用禴'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六有孚不終乃亂乃萃若號一握為笑勿恤往无咎'
                    font_name: './yahei.ttf'
<Screen35>:
    name: '35'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text: ''
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '晋'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '锄地锄去苗里草\\n谁想财帛将人找\\n一锄锄出银子来\\n这个运气也算好'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 35
                source: '35.png'
                allow_stretch: False
            Label:
                text: '晉康侯用錫馬蕃庶晝日三接'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九晉其角維用伐邑厲吉无咎貞吝'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五悔亡失得勿恤往吉无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四晉如鼫鼠貞厲'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三眾允悔亡'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二晉如愁如貞吉受茲介福于其王母'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六晉如摧如貞吉罔孚裕无咎'
                    font_name: './yahei.ttf'
<Screen16>:
    name: '16'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text: ''
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '豫'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '太公插下杏黄旗\\n收妖为徒归西歧\\n自此青龙得了位\\n一旦谋望百事宜'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 16
                source: '16.png'
                allow_stretch: False
            Label:
                text: '豫利建侯行師'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 140, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六冥豫成有渝无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五貞疾恒不死'
                    font_name: './yahei.ttf'
                Label:
                    text: '九四由豫大有得勿疑朋盍簪'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三盱豫悔遲有悔'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二介于石不終日貞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六鳴豫凶'
                    font_name: './yahei.ttf'
<Screen20>:
    name: '20'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'八月\\n白露\\n鸡'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '观'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '卦遇蓬花旱逢河\\n生意买卖利息多\\n婚姻自有人来助\\n出门永不受折磨'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 20
                source: '20.png'
                allow_stretch: False
            Label:
                text: '觀盥而不薦有孚顒若'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九觀其生君子无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五觀我生君子无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四觀國之光利用賓于王'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三觀我生進退'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二闚觀利女貞'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六童觀小人无咎君子吝'
                    font_name: './yahei.ttf'
<Screen8>:
    name: '8'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                #text:'[b]00[/b]:00:00'
                text:'[b]00[/b]:00:00'
                font_size: 60
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '比'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '顺风行船撒起帆\\n上天又助一蓬风\\n不用费力逍遥去\\n任意而行大亨通'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 8
                source: '8.png'
                allow_stretch: False
            Label:
                text: '比吉原筮元永貞无咎不寧方來後夫凶'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 140, 10
                        pos: 140, 200
                    
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六比之无首凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '九五顯比王用三驅失前禽邑人不誡吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四外比之貞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三比之匪人'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二比之自內貞吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六有孚比之无咎有孚盈缶終來有它吉'
                    font_name: './yahei.ttf'
<Screen23>:
    name: '23'
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'九月\\n寒露\\n狗'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '剥'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '鹊遇天晚宿林中\\n不知林内先有鹰\\n虽然同处心生恶\\n卦若逢之是非轻'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 23
                source: '23.png'
                allow_stretch: False
            Label:
                text: '剝不利有攸往'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 140, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上九碩果不食君子得輿小人剝廬'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五貫魚以宮人寵无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四剝床以膚凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三剝之无咎'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二剝床以辨蔑貞凶'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六剝床以足蔑貞凶'
                    font_name: './yahei.ttf'
<Screen2>:
    BoxLayout:
        orientation: 'vertical'
        padding: [10,40,40,30]
        BoxLayout:
            size_hint_y: .3
            Label:
                text:'十月\\n立冬\\n猪'
                font_name: './yahei.ttf'
                markup: True
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '坤'
                font_size: 60
                font_name: './yahei.ttf'
                on_release:
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
            Button:
                background_normal: ''
                background_color: 0,0,0,0
                text: '肥羊失群入山岗\\n饿虎逢之把口张\\n适口充肠心欢喜\\n卦若占之大吉昌'
                font_name: './yahei.ttf'
        BoxLayout:
            Image:
                id: 2
                source: '2.png'
                allow_stretch: False
            Label:
                text: '坤元亨利牝馬之貞君子有攸往先迷後得主利西南得朋東北喪朋安貞吉'
                font_name: './yahei.ttf'
        BoxLayout:
            BoxLayout:
                orientation: 'vertical'
                canvas:
                    Color:
                        rgba: 1,1,1,1
                    Rectangle:
                        size: 60, 10
                        pos: 140, 240
                    Rectangle:
                        size: 60, 10
                        pos: 220, 240
                    Rectangle:
                        size: 60, 10
                        pos: 140, 200
                    Rectangle:
                        size: 60, 10
                        pos: 220, 200
                    Rectangle:
                        size: 60, 10
                        pos: 140, 160
                    Rectangle:
                        size: 60, 10
                        pos: 220, 160
                    Rectangle:
                        size: 60, 10
                        pos: 140, 120
                    Rectangle:
                        size: 60, 10
                        pos: 220, 120
                    Rectangle:
                        size: 60, 10
                        pos: 140, 80
                    Rectangle:
                        size: 60, 10
                        pos: 220, 80
                    Rectangle:
                        size: 60, 10
                        pos: 140, 40
                    Rectangle:
                        size: 60, 10
                        pos: 220, 40
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: '上六龍戰于野其血玄黃'
                    font_name: './yahei.ttf'
                Label:
                    text: '六五黃裳元吉'
                    font_name: './yahei.ttf'
                Label:
                    text: '六四括囊无咎无譽'
                    font_name: './yahei.ttf'
                Label:
                    text: '六三含章可貞或從王事无成有終'
                    font_name: './yahei.ttf'
                Label:
                    text: '六二直方大不習无不利'
                    font_name: './yahei.ttf'
                Label:
                    text: '初六履霜堅冰至'
                    font_name: './yahei.ttf'
<Screensanmei>:
    BoxLayout        
        AnchorLayout
            anchor_x: 'left'
            anchor_y: 'top'
            Button:   
                text: '抛掷'
                font_name: './yahei.ttf'
                size_hint: .3, .2
                on_press: root.new()
        BoxLayout
            orientation: 'vertical'
            Label:
                id: label_san1
                font_size: 60
                text: '上'
                font_name: './yahei.ttf'
            Label:
                id: label_san2
                font_size: 60
                text: '五'
                font_name: './yahei.ttf'
            Label:
                id: label_san3
                font_size: 60
                text: '四'
                font_name: './yahei.ttf'
            Label:
                id: label_san4
                font_size: 60
                text: '三'
                font_name: './yahei.ttf'
            Label:
                id: label_san5
                font_size: 60 
                text: '二'
                font_name: './yahei.ttf'
            Label:
                id: label_san6
                font_size: 60
                text: '初'
                font_name: './yahei.ttf'
        AnchorLayout
            anchor_x: 'right'
            anchor_y: 'bottom'
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .3, .2
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
<Screenliumei>:
    BoxLayout        
        AnchorLayout
            anchor_x: 'left'
            anchor_y: 'top'
            Button:   
                text: '抛掷'
                font_name: './yahei.ttf'
                size_hint: .3, .2
                on_press: root.new()
        BoxLayout
            orientation: 'vertical'
            Label:
                id: label_liu1
                font_size: 60
                text: '上'
                font_name: './yahei.ttf'
            Label:
                id: label_liu2
                font_size: 60
                text: '五'
                font_name: './yahei.ttf'
            Label:
                id: label_liu3
                font_size: 60
                text: '四'
                font_name: './yahei.ttf'
            Label:
                id: label_liu4
                font_size: 60
                text: '三'
                font_name: './yahei.ttf'
            Label:
                id: label_liu5
                font_size: 60 
                text: '二'
                font_name: './yahei.ttf'
            Label:
                id: label_liu6
                font_size: 60
                text: '初'
                font_name: './yahei.ttf'
        AnchorLayout
            anchor_x: 'right'
            anchor_y: 'bottom'
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .3, .2
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'     
<Screensanshu>:
    BoxLayout
        orientation: 'vertical'        
        FloatLayout
            Button:
                text: '易数'
                size_hint: .1, .6
                font_name: './yahei.ttf'
                pos_hint: {'left': 1, 'top': 1}                
                on_press: root.new()
            
        BoxLayout
            BoxLayout
                orientation: 'vertical'
                
                MyTextInput:
                    id: bian
                    text: ''
                    input_filter: 'int'                    
                    halign: 'center'
                    font_size: 60
                    on_text: root.bian()
                    required: True
                MyTextInput:
                    id: shang
                    text: ''
                    input_filter: 'int'                    
                    halign: 'center'
                    font_size: 60
                    cursor_blink: False
                    on_text: root.shang()
                    required: True
                MyTextInput:
                    id: xia
                    text: ''
                    input_filter: 'int'                    
                    halign: 'center'
                    font_size: 60
                    cursor_blink: False
                    on_text: root.xia()
                    required: True
            BoxLayout
                orientation: 'vertical'
                Label:
                    id: label_shu1
                    font_size: 60
                    text: '变'
                    font_name: './yahei.ttf'
                
                Label:
                    id: label_shu2
                    font_size: 60
                    text: '上'
                    font_name: './yahei.ttf'
                
                Label:
                    id: label_shu3
                    font_size: 60
                    text: '下'
                    font_name: './yahei.ttf'
        
        FloatLayout
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .1, .6
                pos_hint: {'right': 1, 'bottom': 1}
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right' 
<Screensheshi>:
    BoxLayout
        orientation: 'vertical'
        FloatLayout
            Button:
                id: ss    
                text: '揲蓍'
                size_hint: .1, .8
                font_name: './yahei.ttf'
                pos_hint: {'left': 1, 'top': 1}
                on_release:
                    root.animate()
            
            Label:
                id: j
                font_size: 60
                pos_hint: {'cent_x': 0.5, 'top': 1}
                text: '太极'
                font_name: './yahei.ttf'
        
        Label:
            id: sheshi
            text: '大衍之数五十，其用四十有九。\\n分而为二以象两，挂一以象三，揲之以四以象四时，归奇于扐以象闰。五岁再闰，故再扐而后挂。\\n乾之策，二百一十有六；坤之策，百四十有四。凡三百有六十，当期之日。\\n二篇之策，万有一千五百二十，当万物之数也。是故，四营而成易，十有八变而成卦。'
            font_name: './yahei.ttf'                       
        
        BoxLayout
            Label:
                id: t
                font_size: 60
                text: '天'
                font_name: './yahei.ttf'
            Label:
                id: r
                font_size: 60
                text: '人'
                font_name: './yahei.ttf'
            Label:
                id: d
                font_size: 60
                text: '地'
                font_name: './yahei.ttf'
        FloatLayout
            Label:
                id: g
                font_size: 60
                font_name: './yahei.ttf'    
                text: '四象'    
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .1, .8
                pos_hint: {'right': 1, 'bottom': 1}
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
<Screenchouqian>:
    BoxLayout
        orientation: 'vertical'
        FloatLayout
            Button:
                text: '筛签'
                size_hint: .1, .6
                font_name: './yahei.ttf'
                pos_hint: {'left': 1, 'top': 1}
                on_press: root.new()
        Label:
            id: label_chouqian
            font_size: 60
            text: '签数'
            font_name: './yahei.ttf'
        FloatLayout
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .1, .6
                pos_hint: {'right': 1, 'bottom': 1}
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
<Screenqian>:
    BoxLayout
        orientation: 'vertical'
        FloatLayout
            Button:
                text: '十六'
                size_hint: .1, .6
                font_name: './yahei.ttf'
                pos_hint: {'left': 1, 'top': 1}
                                
        Label:
            text: root.shiliubian
            font_name: './yahei.ttf'    
        FloatLayout
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .1, .6
                pos_hint: {'right': 1, 'bottom': 1}
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
<Screendui>:
    BoxLayout
        orientation: 'vertical'
        FloatLayout
            Button:
                text: '甲子'
                size_hint: .1, .6
                font_name: './yahei.ttf'
                pos_hint: {'left': 1, 'top': 1}
                                
        Label:
            text: root.liushijiazi
            font_name: './yahei.ttf'    
        FloatLayout
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .1, .6
                pos_hint: {'right': 1, 'bottom': 1}
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right'
<Screenli>:
    BoxLayout
        orientation: 'vertical'
        FloatLayout
            Button:
                
                text: '河洛'
                size_hint: .1, .6
                font_name: './yahei.ttf'
                pos_hint: {'left': 1, 'top': 1}
                on_release:
                    root.heluo()
        BoxLayout:
            
            
            canvas:
                Color:
                    rgba: 1, 1, 1, 1
                Line:                   
                    width: 1
                    rectangle: (325, 280, 150, 150)
                    
            Label:
                id: heluo
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
        FloatLayout
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .1, .6
                pos_hint: {'right': 1, 'bottom': 1}
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right' 
<Screenzhen>:
    BoxLayout
        orientation: 'vertical'
        FloatLayout
            Button:
                
                text: '先后'
                size_hint: .1, .8
                font_name: './yahei.ttf'
                pos_hint: {'left': 1, 'top': 1}
                on_release:
                    root.g()
        Label:
            id: g0
            text: ''
            font_name: './yahei.ttf'
        GridLayout:
            cols: 3
            Label:
                id: g1
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            
            Label:
                id: g2
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            
            
            Label:
                id: g3
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            
            Label:
                id: g4
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            
            
            Label:
                id: g5
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            
            Label:
                id: g6
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            Label:
                id: g7
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            
            
            Label:
                id: g8
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
            
            Label:
                id: g9
                font_name: './yahei.ttf'
                text: ''
                pos_hint: {'x': 0, 'y': 0.6}
        FloatLayout
            Button:    
                text: '学习'
                font_name: './yahei.ttf'
                size_hint: .1, .8
                pos_hint: {'right': 1, 'bottom': 1}
                on_release:
                    #root.clear()
                    root.manager.current = 'menu'
                    root.manager.transition.direction = 'right' 
""")
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class MenuScreen(Screen):
    pass
class Screen1(Screen):
    pass
   
class Screen43(Screen):
    pass
class Screen14(Screen):
    pass
class Screen34(Screen):
    pass
class Screen9(Screen):
    pass
class Screen5(Screen):
    pass
class Screen26(Screen):
    pass
class Screen11(Screen):
    pass
class Screen10(Screen):
    pass
class Screen58(Screen):
    pass
class Screen38(Screen):
    pass
class Screen54(Screen):
    pass
class Screen61(Screen):
    pass
class Screen60(Screen):
    pass
class Screen41(Screen):
    pass
class Screen19(Screen):
    pass
class Screen13(Screen):
    pass
class Screen49(Screen):
    pass
class Screen30(Screen):
    pass
class Screen55(Screen):
    pass
class Screen37(Screen):
    pass
class Screen63(Screen):
    pass
class Screen22(Screen):
    pass
class Screen36(Screen):
    pass
class Screen25(Screen):
    pass
class Screen17(Screen):
    pass
class Screen21(Screen):
    pass
class Screen51(Screen):
    pass
class Screen42(Screen):
    pass
class Screen3(Screen):
    pass
class Screen27(Screen):
    pass
class Screen24(Screen):
    pass
class Screen44(Screen):
    pass
class Screen28(Screen):
    pass
class Screen50(Screen):
    pass
class Screen32(Screen):
    pass
class Screen57(Screen):
    pass
class Screen48(Screen):
    pass
class Screen18(Screen):
    pass
class Screen46(Screen):
    pass
class Screen6(Screen):
    pass
class Screen47(Screen):
    pass
class Screen64(Screen):
    pass
class Screen40(Screen):
    pass
class Screen59(Screen):
    pass
class Screen29(Screen):
    pass
class Screen4(Screen):
    pass
class Screen7(Screen):
    pass
class Screen33(Screen):
    pass
class Screen31(Screen):
    pass
class Screen56(Screen):
    pass
class Screen62(Screen):
    pass
class Screen53(Screen):
    pass
class Screen39(Screen):
    pass
class Screen52(Screen):
    pass
class Screen15(Screen):
    pass
class Screen12(Screen):
    pass
class Screen45(Screen):
    pass
class Screen35(Screen):
    pass
class Screen16(Screen):
    pass
class Screen20(Screen):
    pass
class Screen8(Screen):
    pass
class Screen23(Screen):
    pass
class Screen2(Screen):
    pass
class Screenqian(Screen):
    shiliubian = '''
                    自初至五不动复，下飞四往伏用飞，上飞下飞复本体，便是十六变卦例。
        -------------------------------------------------------------------------------------------
        |八纯|一世|二世|三世|四世|五世|遊魂|外戒|內戒|歸魂|絕命|血脈|肌肉|骸骨|棺犉|墓庫|
        -------------------------------------------------------------------------------------------
        |天天|天风|天山|天地|风地|山地|火地|火山|火风|火天|火火|火雷|山雷|风雷|天雷|天火|
        |乾    |姤    |遁    |否   |观    |剥    |晋   |旅    |鼎    |大有|离    |噬嗑|颐   |益    |无妄|同人|
        -------------------------------------------------------------------------------------------
        |泽泽|泽水|泽地|泽山|水山|地山|雷山|雷地|雷水|雷泽|雷雷|雷火|地火|水火|泽火|泽雷|
        |兑    |困    |萃    |咸   |蹇    |谦    |小过|豫   |解    |归妹|震    |丰    |明夷|既济|革    |随   |
        -------------------------------------------------------------------------------------------
        |火火|火山|火风|火水|山水|风水|天水|天风|天山|天火|天天|天泽|风泽|山泽|火泽|火天|
        |离    |旅    |鼎   |未济|蒙   |涣    |讼    |姤    |遁    |同人|乾    |履    |中孚|损    |睽   |大有|
        -------------------------------------------------------------------------------------------
        |雷雷|雷地|雷水|雷风|地风|水风|泽风|泽水|泽地|泽雷|泽泽|泽天|水天|地天|雷天|雷泽|
        |震    |豫    |解    |恒   |升   |井    |大过|困    |萃    |随   |兑     |夬   |需    |泰    |大壮|归妹|
        -------------------------------------------------------------------------------------------
        |风风|风天|风火|风雷|天雷|火雷|山雷|山火|山天|山风|山山|山地|火地|天地|风地|风山|
        |巽    |小畜|家人|益    |无妄|噬嗑|颐    |贲   |大畜|蛊    |艮    |剥   |晋    |否   |观     |渐   |
        -------------------------------------------------------------------------------------------
        |水水|水泽|水雷|水火|泽火|雷火|地火|地雷|地泽|地水|地地|地山|雷山|泽山|水山|水地|
        |坎    |节    |屯    |既济|革   |丰    |明夷|复    |临   |师    |坤    |谦    |小过|咸   |蹇    |比    |
        -------------------------------------------------------------------------------------------
        |山山|山火|山天|山泽|火泽|天泽|风泽|风天|风火|风山|风风|风水|天水|火水|山水|山风|
        |艮    |贲    |大畜|损    |睽   |履    |中孚|小畜|家人|渐    |巽    |涣   |讼    |未济|蒙   |蛊    |
        -------------------------------------------------------------------------------------------
        |地地|地雷|地泽|地天|雷天|泽天|水天|水泽|水雷|水地|水水|水风|泽风|雷风|地风|地水|
        |坤    |复    |临   |泰    |大壮|夬    |需   |节    |屯    |比    |坎   |井    |大过|恒    |升    |师    |
        -------------------------------------------------------------------------------------------
        |变爻|初爻|二爻|三爻|四爻|五爻|四爻|三爻|二爻|一爻|二爻|三爻|四爻|五爻|四爻|三爻|
        -------------------------------------------------------------------------------------------
'''
class Screendui(Screen):
    liushijiazi = '''
                    
        ---------------------------------------------------------
        |甲子|乙丑|丙寅|丁卯|戊辰|己巳|庚午|辛未|壬申|癸酉|
        |海  中  金 |炉  中  火 |大  林  木|路  旁  土 |剑  锋  金 |
        ---------------------------------------------------------
        |甲戌|乙亥|丙子|丁丑|戊寅|己卯|庚辰|辛巳|壬午|癸未|
        |山  头  火 |涧  下  水 |城  头  土|白  蜡  金 |杨  柳  木 |
        ---------------------------------------------------------
        |甲申|乙酉|丙戌|丁亥|戊子|己丑|庚寅|辛卯|壬辰|癸巳|
        |井  泉  水 |屋  上  土 |霹  雳  火|松  柏  木 |长  流  水 |
        ---------------------------------------------------------
        |甲午|乙未|丙申|丁酉|戊戌|己亥|庚子|辛丑|壬寅|癸卯|
        |砂  中  金 |山  下  火 |平  地  木|壁  上  土 |金  泊  金 |
        ---------------------------------------------------------
        |甲辰|乙巳|丙午|丁未|戊申|己酉|庚戌|辛亥|壬子|癸丑|
        |覆  灯  火 |天  河  水 |大  驿  土|钗  钏  金 |桑  柘  木 |
        ---------------------------------------------------------
        |甲寅|乙卯|丙辰|丁巳|戊午|己未|庚申|辛酉|壬戌|癸亥|
        |大  溪  水 |砂  中  土 |天  上  火|石  榴  木 |大  海  水 |
        ---------------------------------------------------------
'''
from kivy.graphics import Line, Color, Ellipse, Rectangle, PushMatrix, PopMatrix, Rotate
class Screenli(Screen):
    count = 1
    objects = []
    def heluo(self):
        self.count+=1
        
        with self.canvas:
            if self.count % 2 == 0:
                self.ids['heluo'].text = '河图'
                for i in self.objects:
                    self.canvas.remove(i)
                for i in range(0, 6):
                    #self.objects.append(Line(circle=[150+i*100,150, 10, 0, 360,180]))
                    self.objects.append(Ellipse(pos=(150+i*100,100), size=(10, 10)))
                for i in range(0, 8):
                    self.objects.append(Ellipse(pos=(50,150+i*50), size=(10, 10)))
                for i in range(0, 7):
                    self.objects.append(Line(circle=[140+i*80, 550, 5, 0, 360,180]))
                for i in range(0, 9):
                    self.objects.append(Line(circle=[750,150+i*45, 5, 0, 360,180]))
                for i in range(0, 2):
                    self.objects.append(Ellipse(pos=(370+i*50,500), size=(10, 10)))
                for i in range(0, 5):
                    self.objects.append(Ellipse(pos=(250+i*80,450), size=(10, 10)))
                for i in range(0, 1):
                    self.objects.append(Line(circle=[400,150, 5, 0, 360,180]))
                for i in range(0, 5):
                    self.objects.append(Ellipse(pos=(250+i*80,200), size=(10, 10)))
                for i in range(0, 3):
                    self.objects.append(Line(circle=[200,250+i*80, 5, 0, 360,180]))
                for i in range(0, 4):
                    self.objects.append(Ellipse(pos=(650,220+i*60), size=(10, 10)))
                #center cross
                for i in range(0, 1):
                    self.objects.append(Line(circle=[400,400, 5, 0, 360,180]))
                for i in range(0, 3):
                    self.objects.append(Line(circle=[350+i*50,350, 5, 0, 360,180]))
                for i in range(0, 1):
                    self.objects.append(Line(circle=[400,300, 5, 0, 360,180]))
                
            else:
                self.ids['heluo'].text = '洛书'
                for i in self.objects:
                    self.canvas.remove(i)    
                for i in range(0, 9):
                    self.objects.append(Line(circle=[120+i*70, 550, 5, 0, 360,180]))
                for i in range(0, 1):
                    self.objects.append(Line(circle=[400,150, 5, 0, 360,180]))
                for i in range(0, 3):
                    self.objects.append(Line(circle=[50,150+i*150, 5, 0, 360,180]))
                for i in range(0, 7):
                    self.objects.append(Line(circle=[750,150+i*50, 5, 0, 360,180]))
                PushMatrix()
                Rotate(origin=(50, 50), angle=330)
                self.objects.append(Line(rectangle=[50, 50, 60, 120], dash_offset=1))
                PopMatrix()
                self.objects.append(Ellipse(pos=(46,45), size=(10, 10)))
                self.objects.append(Ellipse(pos=(106,148), size=(10, 10)))
                self.objects.append(Ellipse(pos=(96,20), size=(10, 10)))
                self.objects.append(Ellipse(pos=(152,120), size=(10, 10)))
                self.objects.append(Ellipse(pos=(61,70), size=(10, 10)))
                self.objects.append(Ellipse(pos=(84,110), size=(10, 10)))
                self.objects.append(Ellipse(pos=(113,48), size=(10, 10)))
                self.objects.append(Ellipse(pos=(135,83), size=(10, 10)))
                PushMatrix()
                Rotate(origin=(700, 20), angle=30)
                self.objects.append(Line(rectangle=[700, 20, 60, 120], dash_offset=1))
                PopMatrix()
                self.objects.append(Ellipse(pos=(748,45), size=(10, 10)))
                self.objects.append(Ellipse(pos=(685,150), size=(10, 10)))
                self.objects.append(Ellipse(pos=(695,20), size=(10, 10)))
                self.objects.append(Ellipse(pos=(640,120), size=(10, 10)))
                self.objects.append(Ellipse(pos=(664,70), size=(10, 10)))
                self.objects.append(Ellipse(pos=(714,100), size=(10, 10)))
                PushMatrix()
                Rotate(origin=(90, 430), angle=30)
                self.objects.append(Line(rectangle=[90, 430, 60, 120], dash_offset=1))
                PopMatrix()
                self.objects.append(Ellipse(pos=(75,556), size=(10, 10)))
                self.objects.append(Ellipse(pos=(28,527), size=(10, 10)))
                self.objects.append(Ellipse(pos=(85,423), size=(10, 10)))
                self.objects.append(Ellipse(pos=(137,452), size=(10, 10)))
                PushMatrix()
                Rotate(origin=(650, 450), angle=330)
                self.objects.append(Line(rectangle=[650, 450, 0, 120], dash_offset=1))
                PopMatrix()
                self.objects.append(Ellipse(pos=(647,450), size=(10, 10)))
                self.objects.append(Ellipse(pos=(704,550), size=(10, 10)))
                #center cross
                for i in range(0, 1):
                    self.objects.append(Line(circle=[400,400, 5, 0, 360,180]))
                for i in range(0, 3):
                    self.objects.append(Line(circle=[350+i*50,350, 5, 0, 360,180]))
                for i in range(0, 1):
                    self.objects.append(Line(circle=[400,300, 5, 0, 360,180]))
from kivy.animation import Animation
class Screenzhen(Screen):
    
    count = 1
    
    def g(self):
        self.count+=1
        if self.count % 2 == 0:
            self.ids['g1'].text = '兑二'
            self.ids['g2'].text = '乾一'
            self.ids['g3'].text = '巽五'
            self.ids['g4'].text = '离三'
            self.ids['g5'].text = '先天'
            self.ids['g6'].text = '坎六'
            self.ids['g7'].text = '震四'
            self.ids['g8'].text = '坤八'
            self.ids['g9'].text = '艮七'
            self.animate('乾、兑属金，震、巽属木，坤、艮属土，离属火，坎属水。')
        else:
            self.ids['g1'].text = '巽四'
            self.ids['g2'].text = '离九'
            self.ids['g3'].text = '坤二'
            self.ids['g4'].text = '震三'
            self.ids['g5'].text = '后天'
            self.ids['g6'].text = '兑七'
            self.ids['g7'].text = '艮八'
            self.ids['g8'].text = '坎一'
            self.ids['g9'].text = '乾六'
            self.animate('帝出乎震，齐乎巽，相见乎离，致役乎坤，说言乎兑，战乎乾，劳乎坎，成言乎艮。')
            
    def animate(self, val):
        #anim = Animation(opacity=0, duration=2)
        self.ids['g0'].text = val
        #anim.start(self.ids['g0'])
from random import randint
class Screensanmei(Screen):
    def new(self):
        for i in range(1, 7):
            x = randint(6, 9)
            if x == 6:
                r = '老阴'
            elif x == 7:
                r = '少阳'
            elif x == 8:
                r = '少阴'
            elif x == 9:
                r = '老阳'                    
            self.ids['label_san%s' % i].text = r
        
    def clear(self):
        self.ids['label_san1'].text = '^'
        self.ids['label_san2'].text = '-'
        self.ids['label_san3'].text = '-'
        self.ids['label_san4'].text = '-'
        self.ids['label_san5'].text = '-'
        self.ids['label_san6'].text = '-'  
class Screenliumei(Screen):
    def new(self):
        for i in range(1, 7):
            x = randint(0, 1)
            if x == 0:
                r = '阴'
            elif x == 1:
                r = '阳'                                
            self.ids['label_liu%s' % i].text = r
    def clear(self):
        self.ids['label_liu1'].text = '^'
        self.ids['label_liu2'].text = '-'
        self.ids['label_liu3'].text = '-'
        self.ids['label_liu4'].text = '-'
        self.ids['label_liu5'].text = '-'
        self.ids['label_liu6'].text = '-'
class Screensanshu(Screen):
    def xia(self):
        self.tx = self.ids['xia'].text
    def shang(self):
        self.ts = self.ids['shang'].text
    def bian(self):
        self.tb = self.ids['bian'].text 
    def new(self):
        x = int(self.tx) % 8 if hasattr(self, 'tx') else 0
        s = int(self.ts) % 8 if hasattr(self, 'ts') else 0
        b = int(self.tb) % 6 if hasattr(self, 'tb') else 0
        def g(r):
            if r == 0:
                return '地'
            elif r == 1:
                return '天'
            elif r == 2:
                return '泽'
            elif r == 3:
                return '火'
            elif r == 4:
                return '雷'
            elif r == 5:
                return '风'
            elif r == 6:
                return '水'
            elif r == 7:
                return '山'
        def y(r):
            if r == 0:
                return '上'
            elif r == 1:
                return '初'
            elif r == 2:
                return '二'
            elif r == 3:
                return '三'
            elif r == 4:
                return '四'
            elif r == 5:
                return '五'
        self.ids['label_shu1'].text = y(b)
        self.ids['label_shu2'].text = g(s)
        self.ids['label_shu3'].text = g(x)
    def clear(self):
        self.ids['label_shu1'].text = '||'
        self.ids['label_shu2'].text = '/\\'
        self.ids['label_shu3'].text = '\\/'
from kivy.clock import Clock
    
class Screensheshi(Screen):
    r = '|'*50
    public_value = [0, 0, 0]
    #def __call__( self ):
    #    return self.public_value
    def animate(self):
        t = 3
        Clock.schedule_once(self.s1, t)
        Clock.schedule_once(self.s2, t)
        Clock.schedule_once(self.s3, t)
        
        for i in range(0,3):   
            Clock.schedule_once(self.s4, t)
            Clock.schedule_once(self.s5, t)
        Clock.schedule_once(self.s6, t)
    def s1(self, dt):
            
        self.ids['sheshi'].font_size = 60
        self.ids['sheshi'].text = self.r
        print('In s1', dt, self.r.count('|'))
    def s2(self, dt):
            
        x = randint(1,51)
        self.r = self.r[:x]+''+self.r[x+1:]
        self.ids['sheshi'].text = self.r
        self.ids['j'].text = '___'
        
        print('In s2', dt, x, self.r.count('|'))
    def s3(self, dt):
            
        x = randint(1,50)
        self.r = self.r[:x]+'\n'+self.r[x:]
        self.ids['sheshi'].text = self.r
        
        self.public_value[0] = x
        print('In s3', dt, self.public_value[0], self.r.count('|'))
    def s4(self, dt):
        
        x = randint(1,self.public_value[0]) if self.public_value[0] != 1 else 1
        self.ids['r'].text = '___'
        self.r = self.r[:x]+''+self.r[x+1:self.public_value[0]]+'\n'+self.r[self.public_value[0]:]
        public_left = self.r[:self.public_value[0]].count('|')
        public_right = self.r[self.public_value[0]:].count('|')
        self.ids['sheshi'].text = '|'*(public_left) + '\n' + '|'*(public_right)
        self.ids['t'].text = '|*'+str(public_left)
        self.ids['d'].text = '|*'+str(public_right)
        self.public_value[1] = public_left
        self.public_value[2] = public_right
        print('In s4', dt, x, self.public_value[1], self.public_value[2], self.r.count('|'))
    def s5(self, dt):
        x = self.public_value[1] % 4
        self.public_value[1] = 4 if x == 0 else x
        x = self.public_value[2] % 4
        self.public_value[2] = 4 if x == 0 else x
             
        self.ids['t'].text = '|'*self.public_value[1]
        self.ids['d'].text = '|'*self.public_value[2]
        self.ids['sheshi'].text = ''
        self.public_value[0] = self.r.count('|')-self.public_value[1]-self.public_value[2]
        self.ids['g'].text = '|'*(self.public_value[0])
        print('In s5', dt, self.public_value[0], self.r.count('|'))
        
        self.r = '|'*self.public_value[0]
        self.public_value[0]+=1
    def s6(self, dt):
        self.public_value[0]-=1
        x = self.public_value[0]/ 4
        if x == 6:
            r = '老阴'
        elif x == 7:
            r = '少阳'
        elif x == 8:
            r = '少阴'
        elif x == 9:
            r = '老阳'
        self.ids['sheshi'].text = r
        print('In s6', dt, self.public_value[0], self.r.count('|'))
        self.r = '|'*50
    
'''
from kivy.animation import Animation
ao = lambda x: x + 1
from time import strftime
from kivy.clock import Clock
class Screensheshi(Screen):
    variable = 0
    r = '|'*50
    def animate(self):
        Clock.schedule_interval(lambda dt: self.update(), 1)
    def update(self):
        self.variable+=1
        if self.variable==1:            
            self.ids['b'].text = self.r
'''         
        
        
        
class Screenchouqian(Screen):
    def new(self):
        self.ids['label_chouqian'].text = str(randint(1, 65))
    def clear(self):
        self.ids['label_chouqian'].text = ''  
   
# The ScreenManager controls moving between screens
# You can change the transitions accorsingly
sm = ScreenManager(transition = SlideTransition())
   
# Add the screens to the manager and then supply a name
# that is used to switch screens
sm.add_widget(MenuScreen(name ="menu"))
sm.add_widget(Screen1(name ="Screen1"))
sm.add_widget(Screen43(name='Screen43'))
sm.add_widget(Screen14(name='Screen14'))
sm.add_widget(Screen34(name='Screen34'))
sm.add_widget(Screen9(name='Screen9'))
sm.add_widget(Screen5(name='Screen5'))
sm.add_widget(Screen26(name='Screen26'))
sm.add_widget(Screen11(name='Screen11'))
sm.add_widget(Screen10(name='Screen10'))
sm.add_widget(Screen58(name='Screen58'))
sm.add_widget(Screen38(name='Screen38'))
sm.add_widget(Screen54(name='Screen54'))
sm.add_widget(Screen61(name='Screen61'))
sm.add_widget(Screen60(name='Screen60'))
sm.add_widget(Screen41(name='Screen41'))
sm.add_widget(Screen19(name='Screen19'))
sm.add_widget(Screen13(name='Screen13'))
sm.add_widget(Screen49(name='Screen49'))
sm.add_widget(Screen30(name='Screen30'))
sm.add_widget(Screen55(name='Screen55'))
sm.add_widget(Screen37(name='Screen37'))
sm.add_widget(Screen63(name='Screen63'))
sm.add_widget(Screen22(name='Screen22'))
sm.add_widget(Screen36(name='Screen36'))
sm.add_widget(Screen25(name='Screen25'))
sm.add_widget(Screen17(name='Screen17'))
sm.add_widget(Screen21(name='Screen21'))
sm.add_widget(Screen51(name='Screen51'))
sm.add_widget(Screen42(name='Screen42'))
sm.add_widget(Screen3(name='Screen3'))
sm.add_widget(Screen27(name='Screen27'))
sm.add_widget(Screen24(name='Screen24'))
sm.add_widget(Screen44(name='Screen44'))
sm.add_widget(Screen28(name='Screen28'))
sm.add_widget(Screen50(name='Screen50'))
sm.add_widget(Screen32(name='Screen32'))
sm.add_widget(Screen57(name='Screen57'))
sm.add_widget(Screen48(name='Screen48'))
sm.add_widget(Screen18(name='Screen18'))
sm.add_widget(Screen46(name='Screen46'))
sm.add_widget(Screen6(name='Screen6'))
sm.add_widget(Screen47(name='Screen47'))
sm.add_widget(Screen64(name='Screen64'))
sm.add_widget(Screen40(name='Screen40'))
sm.add_widget(Screen59(name='Screen59'))
sm.add_widget(Screen29(name='Screen29'))
sm.add_widget(Screen4(name='Screen4'))
sm.add_widget(Screen7(name='Screen7'))
sm.add_widget(Screen33(name='Screen33'))
sm.add_widget(Screen31(name='Screen31'))
sm.add_widget(Screen56(name='Screen56'))
sm.add_widget(Screen62(name='Screen62'))
sm.add_widget(Screen53(name='Screen53'))
sm.add_widget(Screen39(name='Screen39'))
sm.add_widget(Screen52(name='Screen52'))
sm.add_widget(Screen15(name='Screen15'))
sm.add_widget(Screen12(name='Screen12'))
sm.add_widget(Screen45(name='Screen45'))
sm.add_widget(Screen35(name='Screen35'))
sm.add_widget(Screen16(name='Screen16'))
sm.add_widget(Screen20(name='Screen20'))
sm.add_widget(Screen8(name='Screen8'))
sm.add_widget(Screen23(name='Screen23'))
sm.add_widget(Screen2(name='Screen2'))

sm.add_widget(Screensanmei(name='Screensanmei'))
sm.add_widget(Screenliumei(name='Screenliumei'))
sm.add_widget(Screensanshu(name='Screensanshu'))
sm.add_widget(Screensheshi(name='Screensheshi'))
sm.add_widget(Screenchouqian(name='Screenchouqian'))

sm.add_widget(Screenqian(name='Screenqian'))
sm.add_widget(Screendui(name='Screendui'))
sm.add_widget(Screenli(name='Screenli'))
sm.add_widget(Screenzhen(name='Screenzhen'))
# Create the App class
class GuaApp(App):
    def build(self):
        
        return sm
  
# run the app 
sample_app = GuaApp()
sample_app.run()
