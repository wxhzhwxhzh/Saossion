function loadjQuery() {
    // 创建一个 script 元素
    var script = document.createElement('script');

    // 设置 script 元素的 src 属性为 jQuery 的 CDN 地址
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    script.id = 'jq';

    // 将 script 元素添加到文档的头部或 body 中
    document.head.appendChild(script);
    // 或者使用 document.body.appendChild(script);
}

function makeTextTo(color) {
    // 获取页面上的所有文本元素
    var textElements = document.getElementsByTagName('p'); // 获取所有 <p> 标签的文本
    textElements = Array.from(textElements).concat(Array.from(document.getElementsByTagName('span'))); // 获取所有 <span> 标签的文本并合并
  
    // 将所有文本元素的颜色设置为红色
    textElements.forEach(function(element) {
      element.style.color = color;
    });
  }
 
  
// 定义一个函数，用于设置 HTML 元素的鼠标悬停样式
function setHoverStyle() {
  // 获取所有 class 属性为 "god_class" 的 HTML 元素，并将它们存储在一个数组中
  var elements = document.getElementsByClassName("god_class");
  
  // 使用循环遍历数组中的每一个 HTML 元素
  for (var i = 0; i < elements.length; i++) {
    // 为当前 HTML 元素添加一个鼠标悬停事件监听器
    elements[i].addEventListener("mouseover", function() {
      // 当鼠标悬停在元素上时，将元素的背景颜色设置为深黄色
      this.style.backgroundColor = "rgb(219, 147, 14)";
    });
    
    // 为当前 HTML 元素添加一个鼠标移出事件监听器
    elements[i].addEventListener("mouseout", function() {
    // 当鼠标从元素上移开时，将元素的背景颜色设置为默认值（即空字符串）
      this.style.backgroundColor = "rgba(127, 106, 219, 0.801)";
    });
  }
}

  


function updateRandomUrl() {
  var randomButton = document.getElementById('randomButton');
  if (randomButton) {
    randomButton.parentNode.removeChild(randomButton);
  }
}
function updateRandomUrl3() {
  var randomButton = document.getElementById('randomButton');
  if (randomButton) {
    randomButton.innerHTML= "开启手动";
  }
}

function changeBackgroundColor(cc) {
  document.body.style.backgroundColor = cc;

}
function toggleBackgroundColor() {
  // 获取当前网页的背景颜色
  var currentBgColor = document.body.style.backgroundColor;
  
  
  // 如果当前背景颜色是白色
  if (currentBgColor === 'white') {
    // 切换为绿色背景
    document.body.style.backgroundColor = 'green';
  } else if (currentBgColor === 'green') {
    // 如果当前背景颜色是绿色
    // 切换为白色背景
    document.body.style.backgroundColor = 'white';
  }else {
    // 如果当前背景颜色是其他颜色
    // 切换为白色背景
    document.body.style.backgroundColor = 'white';
  }
}


function parse_vip() {
  // 获取当前网页的URL
  var currentUrl = window.location.href;
  
  // 构建新的URL
  var newUrl = 'https://www.ckplayer.vip/jiexi/?url=' + encodeURIComponent(currentUrl);
  
  // 在新窗口中打开新的URL
  window.open(newUrl);
}


function scrollDownSlowly() {
  // 滚动高度的初始值
  var scrollHeight = 0;
  
  // 每次滚动的距离
  var scrollStep = 10;
  
  // 每次滚动的时间间隔
  var scrollInterval = 50; // 单位：毫秒
  
  // 定时器函数，每隔一段时间执行一次滚动
  var scrollTimer = setInterval(function() {
    // 累加滚动高度
    scrollHeight += scrollStep;
    
    // 滚动到指定高度
    window.scrollTo(0, scrollHeight);
    
    // 如果滚动到页面底部，则清除定时器停止滚动
    if (scrollHeight >= document.documentElement.scrollHeight) {
      clearInterval(scrollTimer);
    }
  }, scrollInterval);
}

function to_top() {
  window.scrollTo(0, 0);
}
// loadjQuery();
// makeTextRed();
// alert(333);