$(document).ready(function () {
    $(window).on('keyup', function (e) {
        var left_key = 'left'
        var right_key = 'right'
        var both_win_key = 'both_win'
        var both_lose_key = 'both_lose'

        var key_dict = {
            37: left_key,
            38: both_win_key,
            39: right_key,
            40: both_lose_key
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
                    if (data.is_complete) {
                        window.location.href = '/image_list';
                    }
                    else {
                        $("#left_image").attr("src", data.left_image)
                        $("#right_image").attr("src", data.right_image)
                        $("#count").text(data.count)
                    }
                })
        }
        e.preventDefault();
    })
})