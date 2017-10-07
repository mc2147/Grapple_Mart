function downloadLink() {
	var link = document.getElementById('test'); 
	link.setAttribute('href', '../Desktop/lion.png');
	link.disabled = true;
}

function cloakLink() {
	var link = document.getElementById('test'); 
	setTimeout(function () {
		link.setAttribute('href', '#');
		link.setAttribute('disabled', true); 
	}, 10); 
}