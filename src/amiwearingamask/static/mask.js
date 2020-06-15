
function trigger_image_analysis(data_uri) {
    // display results in page
    var formdata = new FormData();
    formdata.append('image', data_uri);
    $.ajax({
        url: "/",
        method:"post",
        contentType: false,
        processData: false, // Error building args without
        data: formdata,
        error: function(stuff) {
            console.log(stuff);
        },
        success: function(data, status, jqXHR) {
            var pred = data.prediction;
            var to_display = '';
            console.log('predicted: ' + pred);
            if (pred == 'mask') {
                to_display = 'YES';
            }
            else {
                to_display = 'NO';
            }
            $('#category-name').text(to_display);
        }
    });
    document.getElementById('results').innerHTML =
        '<img src="'+data_uri+'"/>';
}

function loop_snapshot() {
    Webcam.snap(trigger_image_analysis);
    var targetFPS = 3;
    setTimeout(loop_snapshot, 1000 / targetFPS);
}
