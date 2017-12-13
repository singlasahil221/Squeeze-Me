$(document).ready(function(){
	$('#Custom').on('click',function () {
		$('#custom1').toggle();
	});
});

function myFunction() {
  var copyText = document.getElementById("myInput");
  copyText.select();
  document.execCommand("Copy");
  alert("Copied the text: " + copyText.value);
}