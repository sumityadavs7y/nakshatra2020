//select next and previousbutton
var nextBtn=document.getElementById('nextBtn');
var prevBtn=document.getElementById('prevBtn');

//select submit btn to autosubmit after time is out
var submitBtn=document.getElementById('subBtn');

//select all question
var allques=document.getElementsByClassName("curQues");

//select all question btn
var quesBtn=document.getElementsByClassName("btn-q");



//starting function
hideAllQues(); //hide all questions
var timer=setInterval(timerFun,1000); //start timer 
removeInfoBtnColor(0);
addWarningBtnColor(0);


//hide all curQues
function hideAllQues(){
	for (var i = allques.length - 1; i >= 0; i--) {
		allques[i].style.display='none';
	}
}
//show n'th Ques
function displayNQues(n){
	allques[n].style.display='block';
}


//display 1st question and hide previous btn
allques[0].style.display='block';
prevBtn.style.visibility='hidden';

//this will store n'th question displaying right now from 0 to n-1
var x=0;

//this will remove btn Info color
function removeInfoBtnColor(n){
	quesBtn[n].classList.remove("btn-info");
}

//this will add btn Warning color
function addWarningBtnColor(n){
	quesBtn[n].classList.add("btn-warning");
}

//this will remove btn Warning color
function removeWarningBtnColor(n){
	quesBtn[n].classList.remove("btn-warning");
}

//this will add btn success color
function addSuccessBtnColor(n){
	quesBtn[n].classList.add("btn-success");
}


//check if nth radio btn is checked
function atLeastOneRadio(n) {
    return ($('input[name=radio'+n+']:checked').length > 0);
}

function radioClick(n){
	removeInfoBtnColor(n);
	removeWarningBtnColor(n);
	addSuccessBtnColor(n);
}


//this will run when question button will click
function qBtnClick(n){
	hideAllQues();
	displayNQues(n);
	if(!quesBtn[n].classList.contains('btn-success')){
		removeInfoBtnColor(n);
		addWarningBtnColor(n);
	}

	x=n;
	if(x==allques.length-1){
		nextBtn.style.visibility='hidden';
		prevBtn.style.visibility='visible';
	}else if(x==0){
		prevBtn.style.visibility='hidden';
		nextBtn.style.visibility='visible';
	}else{
		nextBtn.style.visibility='visible';
		prevBtn.style.visibility='visible';
	}
}



//Next Previous btn clicked
function npbtn(str){
	if(str=='next'){
		x++;
		qBtnClick(x);
		hideAllQues();
		displayNQues(x);
		prevBtn.style.visibility='visible';
		// console.log(allques.length-1);
		// console.log(x);
		if(x==allques.length-1){
			nextBtn.style.visibility='hidden';
		}
	}
	if(str=='prev'){
		x--;
		qBtnClick(x);
		hideAllQues();
		displayNQues(x);
		nextBtn.style.visibility='visible';
		if(x==0){
			prevBtn.style.visibility='hidden';
		}
	}
}

//this will run the timer and submit on timeout
function timerFun(){
	var s=document.getElementById('timer-sec');
	var m=document.getElementById('timer-min');
	if(parseInt(s.innerHTML)<=0){
		if(parseInt(m.innerHTML)<=0){
			clearInterval(timer);
			submitBtn.click();
			return;
		}
		else{
			m.innerHTML=(parseInt(m.innerHTML)<=10)?('0'+(parseInt(m.innerHTML)-1)):parseInt(m.innerHTML)-1;
			s.innerHTML=59;
		}
	}
	 s.innerHTML=(parseInt(s.innerHTML)<=10)?('0'+(parseInt(s.innerHTML)-1)):parseInt(s.innerHTML)-1;
}
