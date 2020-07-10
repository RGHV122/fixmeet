 $(function() {
        $("#datepicker").datepicker();
      });


function slotchecker() {
	if(document.getElementById("daychecker").checked){
		var selected =document.getElementById('datepicker').value;
	var today=new Date(),slot=new Date(parseInt(selected.substr(6)),parseInt(selected.substr(0,2))-1,selected.substr(3,2));
	console.log(slot)
	if(today<= slot){
		var starttime=document.getElementById('time');
		starttime.value =document.getElementById('starthour').value + ":"+document.getElementById('minute').value;
		if(parseInt(document.getElementById('starthour').value) >parseInt(document.getElementById('endhour').value)){
			alert("nott valid");
			return false;
		}
		else{
			console.log("valid")
		return true;

		}
		
	}	
	else{
		console.log("Invalid")
		alert("Date Not Valid");
		return false;
	}

	}
	else{
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
	
}

function toggledayselect(box) {

	if(box.checked){
		document.getElementById("timeselect").style="display:none;";
		document.getElementById("dayselect").style="display:block;"
	}
	else{
		document.getElementById("dayselect").style="display:none;";
		document.getElementById("timeselect").style="display:block;";
	}
}