$(document).ready(function() {

  var medicalModeImageURL = '../static/images/doctor.png';
  var standardModeImageURL = '../static/images/sinoatrialnode.png';
  var medicalMode = false;

	$(".medical-info").hide();

  $("#medical").click(function() {
  	if (!medicalMode) {
	    $(".medical-info").fadeIn();
	    $("#medical").html("Use Standard Mode");
      $('body').css('background-image', 'url(' + medicalModeImageURL + ')');
      medicalMode = true;
  	} else {
  		$(".medical-info").fadeOut();
  		$("[name='age']").val("None");
  		$("[name='gender']").val("None");
  		$("#medical").html("Use Medical Mode");
      $('body').css('background-image', 'url(' + standardModeImageURL + ')');
      medicalMode = false;
  	}
  });

  $('input:file').change(function() {
      $('#fileName').html($(this).val()); 
      if ($(this).val()) {
        $('input:submit').removeAttr('disabled');
      }
  });

  $('input:submit').click(function() {
      $('#home').fadeOut();
      $("[name='videoFrame']").fadeIn();
      $('#close').fadeIn();
  });


  $('#close').click(function() {
    $("[name='videoFrame']").fadeOut();
    $('#close').fadeOut();
    $('#home').fadeIn();
  })

});