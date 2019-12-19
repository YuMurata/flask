$(document).ready(function () {
    $(window).on('keyup', function (e) {
        var left_key = 'F'
        var right_key = 'J'
        var both_win_key = 'G'
        var both_lose_key = 'H'

        var key_dict = {
            70: left_key,
            74: right_key,
            71: both_win_key,
            72: both_lose_key
        }

        key = String(e.which)
        var is_valid_input = Object.keys(key_dict).indexOf(key) >= 0
        if (is_valid_input) {
            $.ajax({
                url: '/compare',
                type: 'POST',
                dataType: 'json',
                data: { 'key': key_dict[key] },
            })
                .done(function (data) {
                    $("#left_image").attr("src", data.left_image)
                    $("#right_image").attr("src", data.right_image)
                    $("#count").text(data.count)
                })
        }
        e.preventDefault();
    })
})