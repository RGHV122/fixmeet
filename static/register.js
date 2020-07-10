
var targetInput = document.getElementById('title'),
    results = document.getElementById('titlesugg-results'),
    availtitle = ['Doctor','Engineer','Businessman','housewife','Teacher','Student','Freelancer'],
    matches = [],
    resultsCursor = 0;

// Focus the input

targetInput.addEventListener('keydown', function(event) {
    if (event.keyCode == '13') {
        event.preventDefault();
    }
});

// Add event listener for the input keyup
targetInput.addEventListener('keyup', function(event) {
    /*
    * Key codes
    *
    * Enter: 13
    * Arrow up: 38
    * Arrow down: 40
    */
    console.log(1);
    results.innerHTML = '';
    toggleResults('hide');
    if(this.value == null){
    	return "";
    }
    if (this.value.length > 0) {
        matches = getMatches(this.value);

        if (matches.length > 0) {
            displayMatches(matches);
        }
    }

    if (results.classList.contains('visible')) {
        switch(event.keyCode) {
            case 13:
                targetInput.value = results.children[resultsCursor].innerHTML;
                toggleResults('hide');
                resultsCursor = 0;
                results.innerHTML=""
                break;
            case 38:
                if (resultsCursor > 0) {
                    resultsCursor--;

                    moveCursor(resultsCursor);
                }

                break;
            case 40:
                if (resultsCursor < (matches.length - 1)) {
                    resultsCursor++;

                    moveCursor(resultsCursor);
                }

                break;
        }
    }
});

// Define a function for checking if the input value matches any of the country names
function getMatches(inputText) {
    var matchList = [];

    for (var i = 0; i < availtitle.length; i++) {
        if (availtitle[i].toLowerCase().indexOf(inputText.toLowerCase()) ==0) {
            matchList.push(availtitle[i]);
        }
    }

    return matchList;
}

// Define a function for displaying autocomplete results
function displayMatches(matchList) {
    var j = 0;

    while (j < matchList.length) {
        results.innerHTML += '<li class="result">' + matchList[j] + '</li>';
        j++;
    }

    // The first child gets a class of "highlighted"
    moveCursor(resultsCursor);

    // Show the results
    toggleResults('show');
}

// Define a function for moving the cursor in the results list
function moveCursor(pos) {
    for (var x = 0; x < results.children.length; x++) {
        results.children[x].classList.remove('highlighted');
    }

    results.children[pos].classList.add('highlighted');
}

// Define a function for toggling the results list
function toggleResults(action) {
    if (action == 'show') {
        results.classList.add('visible');
    } else if (action == 'hide') {
        results.classList.remove('visible');
    }
}
function submitcheck(){
	var gender = document.getElementById('gender');
	if(gender==""){
		alert("select gender");
		return false;
	}
	return true;
}

function togglePassword1(icon) {
	icon.classList.toggle("fa-eye-slash");
	var pass =document.getElementById("id_password1");
	if(pass.type=="text"){
		pass.type="password";
	}
	else{
		pass.type="text";
	}
	console.log(icon.class);
}
function togglePassword2(icon) {
	icon.classList.toggle("fa-eye-slash");
	var pass =document.getElementById("id_password2");
	if(pass.type=="text"){
		pass.type="password";
	}
	else{
		pass.type="text";
	}
	console.log(icon.class);
}