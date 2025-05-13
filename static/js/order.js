$('.OrderView').click(function (){
$('#save_order').click(function (){
if (! $('#itemOrderModal').html()){
        $.ajax('/', {
          'type': "GET"
          'async': true,
          'dataType': 'json',
          'success': function(response){


           },
        })
    }
});
});
