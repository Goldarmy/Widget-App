$(document).ready(function () {

    $('#deleteWidgetModal').on('show.bs.modal', function (e) {
        var button = $(e.relatedTarget); // Button that triggered the modal
        var widget = button.data('widget'); // Extract info from data-* attributes

        // Pass the id to the form action
        $('#deleteForm')[0].action = '/delete/' + widget.id

    });
});

