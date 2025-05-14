$('#save_order').click(function (){
    let btn = $(this);
    $.ajax(btn.data('order-url'), {
        'type': "POST",
        'async': true,
        'dataType': 'json',
        'data': {
          'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
        },
        'success': function(response){
            const modal = bootstrap.Modal.getInstance(document.getElementById('itemOrderModal'));
            modal.hide();

            alert('Success');
        },
        'error': function () {
            alert('Error');
        }
    })
});


