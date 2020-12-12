function tansuo(){
	var url=new Array();
	url[0]="guichu.html";
	url[1]="haosang.html";
	url[2]="jitang.html";
	url[3]="shehui.html";
	url[4]="shici.html";
	url[5]="tiangou.html";
	url[6]="yingyu.html";
	var ints=parseInt(Math.random()*(url.length));
	window.open(url[ints]);//新窗口打开    
	//window.location=url[ints];//本窗口打开  
	}

