function togglePassword(icon) {
	icon.classList.toggle("fa-eye-slash");
	var pass =document.getElementById("password");
	if(pass.type=="text"){
		pass.type="password";
	}
	else{
		pass.type="text";
	}
	console.log(icon.class);
}