关闭wifi差号

```
打开再关闭飞行模式
settings put global captive_portal_https_url https://www.google.cn/generate_204
```

adb卸载

```
pm uninstall --user 0 com.amazon.kindle
pm uninstall --user 0 com.amazon.mShop.android.shopping                        //亚马逊
pm uninstall --user 0 com.s.antivirus                                          //avg protection
pm uninstall --user 0 com.facebook.system                                      //fb相关的
pm uninstall --user 0 com.spotify.music                                        //spotify

pm uninstall --user 0 com.sonymobile.moviecreator.rmm                          //短片大师
pm uninstall --user 0 com.sonymobile.entrance                                   //What’s new
pm uninstall --user 0 com.sonymobile.xperiaweather                              //天气
pm uninstall --user 0 com.sonymobile.email                                     //邮件
pm uninstall --user 0 com.sonymobile.support                                   //支持
pm uninstall --user 0 com.sonymobile.xperialounge.services
pm uninstall --user 0 com.sonyericsson.xhs                                    //lounge
pm uninstall --user 0 com.sonymobile.assist                                   //助手
pm uninstall --user 0 com.sonyericsson.usbux                                  //usb连接提示
pm uninstall --user 0 com.sony.tvsideview.videoph                               //视频
pm uninstall --user 0 com.sonymobile.synchub                                   //设定里的xpria备份
pm uninstall --user 0 com.sonymobile.infoapp                                   //设定里的支持
pm uninstall --user 0 com.sonymobile.updatecenter.config.latecmz                          
pm uninstall --user 0 com.sonymobile.updatecenter.config.autoinstall           
pm uninstall --user 0 com.sonyericsson.updatecenter                            //更新
pm uninstall --user 0 com.sonymobile.xperiatransfermobile                      //xperia transfer mobile

pm uninstall --user 0 com.google.android.googlequicksearchbox                 //Google
pm uninstall --user 0 com.google.android.calendar                             //日历
pm uninstall --user 0 com.google.android.apps.maps                            //地图
pm uninstall --user 0 com.google.android.apps.photos                          //谷歌照片
pm uninstall --user 0 com.google.android.apps.docs                            //云端硬盘
pm uninstall --user 0 com.google.android.gm                                   //gmail
pm uninstall --user 0 com.google.android.videos                               //谷歌电影
pm uninstall --user 0 com.sonymobile.music.youtubeplugin
pm uninstall --user 0 com.sonymobile.music.youtubekaraokeplugin
pm uninstall --user 0 com.sonymobile.music.youtubeplugin
pm uninstall --user 0 com.google.android.youtube                              //YouTube
com.facebook.services
com.facebook.katana
com.facebook.system
com.facebook.appmanager
com.spotify.music
com.android.stk
com.google.android.apps.tachyon 
```

pm grant com.fb.fluid android.permission.WRITE_SECURE_SETTINGS



adb -d shell sh /data/data/me.piebridge.brevent/brevent.sh



解锁

```
1.解锁码申请
地址 http://unlockbootloader.sonymobile.com/
需要 挂梯子、手机登录（需是移动页面）
2.安装驱动
安装FlashTool 安装完强刷工具后，找到 X:\Flashtool\drivers 路径 安装驱动
注：win10安装驱动需禁用签名，具体参考：https://jingyan.baidu.com/article/546ae185d818941148f28c6c.html
装Flashmod（绿灯）、Fastboot（蓝灯）驱动
3.解锁
https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader/how-to-unlock-bootloader/
4.刷twrp
fastboot flash recovery twrp.img
```

