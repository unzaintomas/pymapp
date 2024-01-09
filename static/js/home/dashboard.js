document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendario');
    var urlReservas = '/reservas/reservas_json/';
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: urlReservas,
        eventTimeFormat: { // Formato de la hora del evento
          hour: '2-digit',
          minute: '2-digit',
          hour12: false // Mostrar en formato de 24 horas
        },
        locale: 'es',  // Configura el idioma del calendario a español
        buttonText: {
          today: 'Hoy',
          month: 'Mes',
          week: 'Semana',
          day: 'Día',
          list: 'Lista'
        }
    });

    calendar.render();
  });