$(function(){

$address_bar = $('#address_bar');
$input_container = $address_bar.find('.input:first');
$address_input = $input_container.find('input');

$nav_apis = $('.nav-api');
$method_groups = $('.api-methods');
$methods = $('.nav-method');
$descriptions = $('.description');
$address_submit = $address_bar.find('a#submit');
$response_container = $('#api_response_container');
$response_loading = $response_container.find('#response_loading');

$address_submit.click(refreshResponse);


$methods.click(function(){
   $(this).siblings().removeClass('clicked');
  $(this).addClass('clicked'); 
  $address_bar.find('span.path').text($(this).attr('id'));
  $descriptions.filter('[id=' + $(this).attr('id') + ']')
    .siblings().hide().end()
    .show();

  $address_input.attr('value', '/?' + $(this).attr('query'));
   $address_submit.click(); 
  
});

$nav_apis.click(function(){

  $(this).siblings().removeClass('clicked');
  $(this).addClass('clicked');
  
  var $this_group = $method_groups.filter('[id=' + $(this).attr('id') + ']');
  
  $this_group.siblings().hide().removeClass('show');
  
  var $clicked_method = $this_group.find('.nav-method.clicked:first');
  if ($clicked_method.length > 0)
     $clicked_method.click(); 
  else $this_group.find('.nav-method:first').click();
  $this_group.show().addClass('show');
  
  });
  
setTimeout(function(){ $nav_apis.filter(':first').click();  }, 50);





function refreshResponse(){
  $response_container.find('.response_data').hide(150);
  $response_loading.show();
  
  $request_path = $input_container.find('.path').text() + $address_input.val() + '&ov=558232';


$.ajax({
  url: '/ajax',
  data:
  { 
    'request_path': $request_path
  },
  success: function(data) {
     $response_loading.hide();
    $response_container.find('#inner').html(data)
      .find('.response_data').addClass('show').show(500);
   
  }
});

}




});


