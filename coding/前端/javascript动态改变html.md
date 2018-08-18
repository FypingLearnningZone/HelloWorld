把默认显示的文字放在<textarea></textarea>之间即可

 

如<textarea>这就是默认显示的文字</textarea>

```
<textarea id="t1"></textarea>
<script>
document.getElementById("t1").value="hello!"
</script> 

或者直接
<textarea id="t1">hello!</textarea>
```