---
title: django_全局搜索
date: 2018/7/25 12:12:12
---

##### 通过url传递参数

- js代码

```js
//顶部搜索栏搜索方法
function search_click(){
    var type = $('#jsSelectOption').attr('data-value'),
        keywords = $('#search_keywords').val(),
        request_url = '';
    if(keywords == ""){
        return
    }
    if(type == "course"){
        request_url = "/course/list?keywords="+keywords
    }else if(type == "teacher"){
        request_url = "/org/teacher/list?keywords="+keywords
    }else if(type == "org"){
        request_url = "/org/list?keywords="+keywords
    }
    window.location.href = request_url
}
```

- html

  ```html
  <div class="middle">
                  <div class="wp">
                      <a href="/"><img class="fl" src="/static/images/logo.jpg"/></a>
                      <div class="searchbox fr">
                          <div class="selectContainer fl">
                              <span class="selectOption" id="jsSelectOption" data-value="course">
                                  公开课
                              </span>
                              <ul class="selectMenu" id="jsSelectMenu">
                                  <li data-value="course">公开课</li>
                                  <li data-value="org">课程机构</li>
                                  <li data-value="teacher">授课老师</li>
                              </ul>
                          </div>
                          <input id="search_keywords" class="fl" type="text" value="" placeholder="请输入搜索内容"/>
                          <img class="search_btn fr" id="jsSearchBtn" src="/static/images/search_btn.png"/>
                      </div>
                  </div>
              </div>
  
  ```

  > 通过js代码将搜索框内的关键字与选定的类别进行拼接，然后访问拼接好的url
  >
  > 后端，获取关键字后进行相应的操作，并返回查询的数据