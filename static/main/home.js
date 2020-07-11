 $(function() {
        $("#datepicker").datepicker();
      });


function slotchecker() {
	
		var hour= document.getElementById('hour').value,minute=document.getElementById('minute').value;
	var time=document.getElementById('time');
	time.value =hour + ":"+minute;
	var selected =document.getElementById('datepicker').value;
	var today=new Date(),slot=new Date(parseInt(selected.substr(6)),parseInt(selected.substr(0,2))-1,selected.substr(3,2),hour,minute);
	console.log(slot)
	if(today<slot){
		console.log("valid")
		return true;
	}	
	else{
		console.log("Invalid")
		alert("Date Not Valid");
		return false;
	}
	
}
