$(function () {
    $("#datatable_reservas").DataTable({
        "responsive": true,
        "lengthChange": false,
        "autoWidth": false
    }).buttons().container().appendTo('#datatable_reservas_wrapper .col-md-6:eq(0)');

    $('.agregar-reserva').on('click', function () {
        // Hacer una solicitud Ajax para obtener el formulario de nuevo cliente
        $.ajax({
            url: '/reservas/reserva/new/',
            type: 'GET',
            success: function (data) {
                // Insertar el formulario directamente en el modal
                $('#reserva-modal-nuevo .modal-body-new-reserva').html(data);
                $('#reserva-modal-nuevo').modal('show');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    $('.editar-reserva').on('click', function () {
        var reservaId = $(this).data('reserva-id');

        // Hacer una solicitud Ajax para obtener el formulario de edición
        $.ajax({
            url: '/reservas/reserva/' + reservaId + '/edit/',
            type: 'GET',
            success: function (data) {
                // Insertar el formulario directamente en el modal
                $('#reserva-modal-editar .modal-body-editar-reserva').html(data);
                $('#reserva-modal-editar').modal('show');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    $('.eliminar-reserva').on('click', function () {
        var reservaId = $(this).data('reserva-id');
    
        // Hacer una solicitud Ajax para obtener el formulario de confirmación de eliminación
        $.ajax({
            url: '/reservas/reserva/' + reservaId + '/delete/',
            type: 'GET',
            success: function (data) {
                // Insertar el formulario directamente en el modal
                $('#reserva-modal-eliminar .modal-body-delete-reserva').html(data);
                $('#reserva-modal-eliminar').modal('show');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});