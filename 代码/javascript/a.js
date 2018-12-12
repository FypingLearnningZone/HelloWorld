App({
    options: {
        debug: true
    },
    /**
     * 当wap2app初始化完成时，会触发 onLaunch
     */
		onLaunch: function() {
		console.log('launch');
		//获取cid并发送get请求完成cid与session的绑定
		var xmlhttp;
		function loadXMLDoc(url,cilentid)
		{
			xmlhttp=null;
			if (window.XMLHttpRequest)
			{// code for Firefox, Opera, IE7, etc.
			xmlhttp=new XMLHttpRequest();
			}
			else if (window.ActiveXObject)
			{// code for IE6, IE5
			xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
			if (xmlhttp!=null)
			{
			xmlhttp.onreadystatechange=state_Change;
			xmlhttp.open("GET",url,true);
			xmlhttp.send(null);
			}
			else
			{
			alert("Your browser does not support XMLHTTP.");
			}
		}

		function state_Change()
		{
			if (xmlhttp.readyState==4)
			{// 4 = "loaded"
			if (xmlhttp.status==200 && cilentid != "null" && cilentid != "")
				{// 200 = "OK"
				alert("消息推送启动成功");
				}
			else
				{
				alert("消息推送启动失败,请重启应用");
				}
			}
		}
		
		var info = plus.push.getClientInfo();
		alert(JSON.stringify(info));
		alert(plus.navigator.getCookie('http://iot.scavenger.top/'));
		// 每50毫秒获取一次cilentid
		var Timer = setInterval(function(){
    if(plus.push.getClientInfo().clientid)
    {
        cilentid = plus.push.getClientInfo().clientid;
				loadXMLDoc("http://iot.scavenger.top/cid?cid="+cilentid,cilentid)
				console.log("cilentid=" + cilentid)
        clearInterval(Timer);
    }
    },50);
// 		plus.storage.setItem("test","test with hbuilder!");
// 		var a = plus.storage.getLength();
// 		var b = plus.storage.getItem("test");
		var storage_sessionid = plus.storage.getItem("id_session");
		console.log("storage_sessionid=" + storage_sessionid);
		session_str = 'sessionid='+storage_sessionid+'; expires=Friday,25-Jan-2030 16:24:36 GMT; path=/'
		// console.log(session_str);
		if (storage_sessionid == null)
		{   
			  // 每50毫秒获取一次sessionid
			  // 读取sessionid并存储到本地
			  var Timer2 = setInterval(function(){
			  if(plus.push.getClientInfo().clientid)
			  {
			  	if (plus.navigator.getCookie('http://iot.scavenger.top/') != null)
			  	{
			  		l1 = plus.navigator.getCookie('http://iot.scavenger.top/').split("; ")
			  		for (i in l1)
			  		{
			  			var first = l1[i].split("=")[0]
			  			if (first == "sessionid")
			  			{
			  				id_session = l1[i].split("=")[1]
			  				console.log("id_session == " + id_session)
								// 如果本地的sessionid 等于null,则把sessionid写入到本地
								plus.storage.setItem("id_session",id_session);
								console.log("write");
			  			} 
			  		}
			  	}
			  	clearInterval(Timer2);
			  }
			  },50);
				
		}
		else
		{
			plus.navigator.removeAllCookie();
			// 如果本地sessionid不为null，说明客户端已经启动，本地sessionid为当前app对于服务器的唯一标识，用于实现状态保持
			plus.navigator.setCookie('http://iot.scavenger.top/',session_str);
			console.log("set");
		}
		
		// alert(plus.navigator.getCookie('http://iot.scavenger.top/'));
		// 每次启动从本地读取sessionid并替换掉当前的sessionid
    
		//监听click事件，用户从消息中心点击触发的
		plus.push.addEventListener("click", function (msg) {
    console.log("You clicked: " + msg.title); //推送消息标题
    console.log("You clicked: " + msg.content); //推送消息内容
    //根据payload传递过来的数据，打开一个详情
    var payload = msg.payload;
    if (payload) {
      // payload 按照规范是 Object，但实际推送过来有可能是 String，需要多一步处理；
      if (typeof payload === 'string') {
        payload = JSON.parse(payload);
      }
      if (typeof payload === 'object') {
        //payload是一个json对象，可以传递业务数据，开发者可以根据实际需求自定义参数
        //本示例在payload中传入新闻id，wap2app接收到推送后，直接打开新闻详情
        var detailId = payload.id;
        //wap2app.open(url)可以直接打开对应的webview
        //这里是示例，实际项目中开发者需根据M站的url拼接页面地址
        wap2app.open('http://tx.cheelink.com/xinje/login/');
      }
    }
    }, false);

		//监听receive事件
		plus.push.addEventListener("receive", function (msg) {
			console.log("recieve title: " + msg.title); //推送消息标题
			console.log("recieve content: " + msg.content); //推送消息内容
			//根据payload传递过来的数据，打开一个详情
			var payload;
			if (msg.payload) {
				//如透传消息不符合格式，则“payload”属性为string类型
				//这里的示例以json字符串去解析，实际上也可以做字符串匹配
				if (typeof (msg.payload) == "string") {
					try {
						payload = JSON.parse(msg.payload);
					} catch (error) {
						console.log(error);
					}
				} else if (typeof (msg.payload) == "object") {
					//iOS应用正处于前台运行时收到推送，也触发receive事件，此时payload为json对象
					payload = msg.payload;
				}


				if (payload) {
					//本示例在payload中传入新闻id，wap2app接收到推送后，直接打开新闻详情
					var detailId = payload.id;
					//wap2app.open(url)可以直接打开对应的webview
					//这里是示例，实际项目中开发者需根据M站的url拼接页面地址
					wap2app.open('http://tx.cheelink.com/xinje/login/');
				}
			}

		}, false);
		
		
    },
    /**
     * 当wap2app启动，或从后台进入前台显示，会触发 onShow
     */
    onShow: function() {
        console.log('show');
    },
    /**
     * 当wap2app从前台进入后台，会触发 onHide
     */
    onHide: function() {
        console.log('hide');
    }
});
Page('__W2A__iot.scavenger.top', { //首页扩展配置
    onShow: function() {

	},
    onClose: function() {

    }
});
