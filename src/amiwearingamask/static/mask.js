
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
            console.log(data);
            console.log('status was: ' + status);
            $('#category-name').text(data.prediction);
        }
    }).done(function() {
        console.log('Done with request');
    });
    document.getElementById('results').innerHTML =
        '<h2>Here is your image:</h2>' +
        '<img src="'+data_uri+'"/>';
}

function loop_snapshot() {
    console.log("Looping snapshot.");
    // take snapshot and get image data
    Webcam.snap(trigger_image_analysis);
    var targetFPS = 10;
    setTimeout(loop_snapshot, 1000 / targetFPS);
}
