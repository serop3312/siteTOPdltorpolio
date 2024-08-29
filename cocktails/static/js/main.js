$(document).ready(function() {
    $('a[href^="{% url \'add_to_favorites\' cocktail_id="]').on('click', function(e) {
        e.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            url: url,
            method: 'GET',
            success: function(data) {
                alert('Cocktail added to favorites!');
            },
            error: function(xhr, status, error) {
                alert('Failed to add cocktail to favorites.');
            }
        });
    });
});