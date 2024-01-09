$(document).ready(function () {
    $("#datatable_clientes").DataTable({
        "responsive": true,
        "lengthChange": false,
        "autoWidth": false
    }).buttons().container().appendTo('#datatable_clientes_wrapper .col-md-6:eq(0)');

    $('.agregar-cliente').on('click', function () {
        // Hacer una solicitud Ajax para obtener el formulario de nuevo cliente
        $.ajax({
            url: '/personas/cliente/new/',
            type: 'GET',
            success: function (data) {
                // Insertar el formulario directamente en el modal
                $('#cliente-modal-nuevo .modal-body-new-cliente').html(data);
                $('#cliente-modal-nuevo').modal('show');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
    

    $('#cliente-modal-reservas').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var clienteId = button.data('cliente-id');

        // Hacer una solicitud Ajax para obtener las reservas del cliente
        $.ajax({
            url: '/personas/cliente/' + clienteId + '/',
            type: 'GET',
            success: function (data) {
                // Limpiar el contenedor de reservas
                $('#reservas-container').empty();

                // Mostrar las reservas
                if (data.reservas.length > 0) {
                    data.reservas.forEach(function (reserva) {
                        var reservaHtml = '<div>';
                        reservaHtml += '<p>- Desde el ' + reserva.fecha_inicio + ' hasta ' + reserva.fecha_fin + '</p>';
                        reservaHtml += '</div>';

                        // Agregar la reserva al contenedor
                        $('#reservas-container').append(reservaHtml);
                    });
                } else {
                    // Mostrar mensaje si no hay reservas
                    $('#reservas-container').html('<p>No tuvo reservas</p>');
                }
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    $('.editar-cliente').on('click', function () {
        var clienteId = $(this).data('cliente-id');

        // Hacer una solicitud Ajax para obtener el formulario de edición
        $.ajax({
            url: '/personas/cliente/' + clienteId + '/edit/',
            type: 'GET',
            success: function (data) {
                // Insertar el formulario directamente en el modal
                $('#cliente-modal-editar .modal-body-editar-cliente').html(data);
                $('#cliente-modal-editar').modal('show');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    $('.eliminar-cliente').on('click', function () {
        var clienteId = $(this).data('cliente-id');
    
        // Hacer una solicitud Ajax para obtener el formulario de confirmación de eliminación
        $.ajax({
            url: '/personas/cliente/' + clienteId + '/delete/',
            type: 'GET',
            success: function (data) {
                // Insertar el formulario directamente en el modal
                $('#cliente-modal-eliminar .modal-body-eliminar-cliente').html(data);
                $('#cliente-modal-eliminar').modal('show');
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});