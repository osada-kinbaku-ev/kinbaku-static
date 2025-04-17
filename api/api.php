<?php
header('Content-Type: application/json;charset=utf-8');

// TODO disable CORS
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: *');
header('Access-Control-Allow-Headers: *');

if ($_SERVER['REQUEST_METHOD'] == "OPTIONS") {
    exit();
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")
);

$cwd = '.';
$env = array('QUERY' => $_SERVER['QUERY_STRING']);

$process = proc_open('python3 api.py', $descriptorspec, $pipes, $cwd, $env);

if (is_resource($process)) {
    // $pipes now looks like this:
    // 0 => writeable handle connected to child stdin
    // 1 => readable handle connected to child stdout
    // Any error output will be appended to /tmp/error-output.txt

    fwrite($pipes[0], file_get_contents('php://input')); // write post data into stdin
    fclose($pipes[0]);

    $stdout = stream_get_contents($pipes[1]);
    $stderr = stream_get_contents($pipes[2]);
    fclose($pipes[1]);

    // It is important that you close any pipes before calling
    // proc_close in order to avoid a deadlock
    $return_value = proc_close($process);

    if ($return_value == 2) {
        http_response_code(400);
    } elseif ($return_value != 0) {
        $stdout = "{\"error\": \"python process exit code > 0\", \"stdout\": \"$stdout\", \"stderr\": \"$stderr\"}";
        http_response_code(500);
    }
}

echo $stdout;
?>
