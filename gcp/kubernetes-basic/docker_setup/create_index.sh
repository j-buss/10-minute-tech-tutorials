#!/bin/bash
cat << EOF > index.html
<html>
<head><title>Simple Web Server</title></head>
<body><h1>$(hostname)</h1><p>Yeah! Things seem to be functioning</p></body>
</html>
EOF
