function downloadLink(Link) {
	// alert("Test");
	var link = document.getElementById('test'); 
	link.setAttribute('href', Link);
	link.disabled = true;
}

function cloakLink() {
	var link = document.getElementById('test'); 
	setTimeout(function () {
		link.setAttribute('href', '#');
		link.setAttribute('disabled', true); 
	}, 10); 
}