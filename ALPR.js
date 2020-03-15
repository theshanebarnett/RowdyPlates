const PiCamera = require('pi-camera');

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

setInterval(function() {

    var path = './notfound/' + getRandomInt(500) + '.jpg';

    const myCamera = new PiCamera({
        mode: 'photo',
        output: path,
        width: 1920,
        height: 1080,
        nopreview: false,
    });


    myCamera.snap()
        .then((result) => {

            var exec = require('child_process').exec;
            var cmd = 'alpr -c us -n 1 --json ' + path;

            exec(cmd, function(error, stdout, stderr) {

                var data = JSON.parse(stdout);
		var tmp = data.results[0].plate;
                if (data.results.length > 0) {
		   //var tmp = data.results[0].plate;
                   console.log("\n\t########################");
		   console.log("\n\tLICENSE PLATE->" + data.results[0].plate);
		   console.log("\n\t########################\n\n");
		   
		   const spawn = require("child_process").spawn;
		   
		   spawn('python',["./licensePlateVehicleInfo.py", tmp]);
		   //console.log("\ndata.result: " + data.result);
		   console.log("\ndata.result[0].plate: " + data.results[0].plate);
		} else {
                    console.log("\n\nNo license plate found.\n");
                }
            });

            console.log(result);

        })
        .catch((error) => {
            console.log("LOOKING FOR LICENSE PLATE...");
        });

}, 2e3);
